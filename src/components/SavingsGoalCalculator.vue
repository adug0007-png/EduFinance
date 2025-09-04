<template>
  <div class="savings-goal-calculator">
    <!-- Main Content -->
    <div class="main-content">
      <!-- Left Side - Form -->
      <div class="form-section">
        <div class="form-group">
          <label>Savings Goal</label>
          <input
            type="text"
            v-model="savingsGoal"
            placeholder="Enter your target amount"
            class="form-input"
          />
        </div>

        <div class="form-row">
          <div class="form-group timeline-group">
            <label>Timeline</label>
            <input
              type="text"
              v-model="timeline"
              placeholder="Duration"
              class="form-input timeline-input"
            />
          </div>
          <div class="form-group unit-group">
            <select v-model="timeUnit" class="form-select">
              <option value="weeks">Weeks</option>
              <option value="months">Months</option>
              <option value="years">Years</option>
            </select>
          </div>
        </div>

        <div class="form-group">
          <label>Initial Deposit (Optional)</label>
          <input
            type="text"
            v-model="initialDeposit"
            placeholder="Amount you already have saved"
            class="form-input"
          />
        </div>

        <div class="form-group">
          <label>Interest Rate (Annual %)</label>
          <input
            type="text"
            v-model="interestRate"
            placeholder="Expected annual interest rate"
            class="form-input"
          />
        </div>

        <button
          type="button"
          class="calculate-btn"
          @click="calculateSavings"
        >
          Calculate Savings Plan
        </button>
        <!-- Status messages (sits under the button) -->
<div class="status-wrap" aria-live="polite">
  <p v-if="statusMessage" class="status-msg" :class="statusClass">
    {{ statusMessage }}
  </p>
</div>

      </div>

      <!-- Right Side - Results -->
      <div class="results-section">
        <div class="savings-plan">
          <h3>Your Savings Plan</h3>
          <div class="monthly-amount">
            <span class="amount">${{ monthlyAmount }}</span>
            <span class="label">Required savings per month</span>
          </div>
          <div class="breakdown">
            <div class="breakdown-item blue">
              <span class="value">${{ weeklyAmount }}</span>
              <span class="label">Per Week</span>
            </div>
            <div class="breakdown-item purple">
              <span class="value">${{ monthlyAmount }}</span>
              <span class="label">Per Month</span>
            </div>
          </div>
        </div>

        <div class="progress-visualization">
          <h4>Progress Visualization</h4>
          <div class="chart-container">
            <canvas ref="chartCanvas" width="400" height="200"></canvas>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import * as echarts from 'echarts'

export default {
  name: 'SavingsGoalCalculator',
  data() {
    return {
      savingsGoal: '10,000',
      timeline: '12',
      timeUnit: 'months',
      initialDeposit: '1,000',
      interestRate: '3.5',
      // keep numeric
      monthlyAmount: 0,
      weeklyAmount: 0,
      chart: null,

      // NEW: status UI
      statusMessage: '',
      statusType: '' // '', 'info', 'success', 'warn', 'error'
    }
  },
  computed: {
    savingsGoalNum() {
      return parseFloat(this.savingsGoal.replace(/,/g, '')) || 0
    },
    initialDepositNum() {
      return parseFloat(this.initialDeposit.replace(/,/g, '')) || 0
    },
    timelineNum() {
      return parseFloat(this.timeline) || 0
    },
    amountToSave() {
      return Math.max(0, this.savingsGoalNum - this.initialDepositNum)
    },
    // NEW: class for message badge
    statusClass() {
      return this.statusType ? `is-${this.statusType}` : ''
    }
  },
  methods: {
    // NEW: helper to set/clear status
    setStatus(type = '', msg = '') {
      this.statusType = type
      this.statusMessage = msg
    },

    // stability patch (guards, clamping, weeks handling, ceil) + messages
    calculateSavings() {
      // clear any previous message
      this.setStatus('', '')

      const goal = Math.max(0, this.savingsGoalNum)
      const initial = Math.max(0, this.initialDepositNum)
      const ratePct = Math.max(0, parseFloat(this.interestRate) || 0)
      const duration = Math.max(0, this.timelineNum)

      // normalise periods
      let months
      let weeks
      if (this.timeUnit === 'weeks') {
        weeks = duration
        months = duration / 4.333 // months only for interest math
      } else if (this.timeUnit === 'years') {
        months = duration * 12
        weeks = months * 4.333
      } else {
        months = duration // months
        weeks = months * 4.333
      }

      // invalid / zero-duration -> fail safe
      if (!isFinite(months) || months <= 0) {
        this.monthlyAmount = 0
        this.weeklyAmount = 0
        this.setStatus('error', 'Please enter a timeline greater than 0.')
        return
      }

      const mRate = (ratePct / 100) / 12

      // growth of initial alone
      const fvInitial = mRate > 0 ? initial * Math.pow(1 + mRate, months) : initial
      if (fvInitial >= goal) {
        this.monthlyAmount = 0
        this.weeklyAmount = 0
        this.setStatus('success', 'Great news — your current savings already meet this goal. No monthly contributions needed.')
        return
      }

      // required payments
      const remaining = Math.max(0, goal - fvInitial)
      let monthly

      if (mRate > 0) {
        // ordinary annuity (end of month)
        const factor = (Math.pow(1 + mRate, months) - 1) / mRate
        monthly = Math.ceil(remaining / factor)
      } else {
        monthly = Math.ceil((goal - initial) / months)
      }

      // weekly: compute directly if user selected weeks; else derive from monthly
      const weekly =
        this.timeUnit === 'weeks'
          ? Math.ceil((goal - initial) / Math.max(1, weeks))
          : Math.ceil(monthly / 4.333)

      this.monthlyAmount = monthly
      this.weeklyAmount = weekly

      // context notes
      const notes = []
      if (this.timeUnit === 'weeks') notes.push('Using weeks; weekly amount is computed directly.')
      if (mRate === 0) notes.push('Interest rate is 0%, plan assumes no growth.')
      if (months < 2) notes.push('Very short timeline — monthly amount may be high.')

      if (notes.length) {
        const hasWarn = months < 2
        this.setStatus(hasWarn ? 'warn' : 'info', notes.join(' '))
      }

      this.$nextTick(() => {
        this.initChart(months, monthly, initial, mRate, goal)
      })
    },

    // dynamic, safe chart that follows the plan (interest + contributions)
    initChart(months, monthly, initial, mRate, goal) {
      if (this.chart) {
        this.chart.dispose()
        this.chart = null
      }

      const el = this.$refs.chartCanvas
      if (!el) return

      const steps = Math.min(Math.max(Math.round(months), 1), 60) // cap for readability
      const categories = Array.from({ length: steps + 1 }, (_, i) => i)
      const data = []

      let bal = initial
      data.push(bal)
      for (let i = 0; i < steps; i++) {
        // end-of-period contribution, then interest
        bal = (bal + monthly) * (1 + mRate)
        data.push(bal)
      }

      const yMaxRaw = Math.max(goal, ...data)
      const yMax = Math.ceil((yMaxRaw * 1.1) / 1000) * 1000
      const interval = Math.max(1000, Math.ceil(yMax / 6 / 1000) * 1000)

      const chart = echarts.init(el)
      chart.setOption({
        grid: { left: '8%', right: '8%', bottom: '15%', top: '8%' },
        xAxis: {
          type: 'category',
          data: categories,
          name: 'Months',
          nameLocation: 'middle',
          nameGap: 20,
          nameTextStyle: { color: '#666', fontSize: 12 },
          axisLine: { show: true, lineStyle: { color: '#ddd' } },
          axisTick: { show: true, lineStyle: { color: '#ddd' } },
          axisLabel: { color: '#666', fontSize: 11 }
        },
        yAxis: {
          type: 'value',
          name: 'Amount ($)',
          nameLocation: 'middle',
          nameGap: 35,
          min: 0,
          max: yMax,
          interval,
          axisLine: { show: true, lineStyle: { color: '#ddd' } },
          axisTick: { show: true, lineStyle: { color: '#ddd' } },
          axisLabel: { color: '#666', fontSize: 11, formatter: '{value}' },
          splitLine: { show: true, lineStyle: { color: '#f0f0f0', type: 'solid' } }
        },
        series: [{
          data,
          type: 'line',
          smooth: true,
          lineStyle: { color: '#28a745', width: 2 },
          itemStyle: { color: '#28a745', borderWidth: 0 },
          symbol: 'circle',
          symbolSize: 3,
          showSymbol: true,
          areaStyle: {
            color: {
              type: 'linear', x: 0, y: 0, x2: 0, y2: 1,
              colorStops: [
                { offset: 0, color: 'rgba(40, 167, 69, 0.15)' },
                { offset: 1, color: 'rgba(40, 167, 69, 0.02)' }
              ]
            }
          }
        }]
      })

      this.chart = chart
    },

    formatNumber(num) {
      return new Intl.NumberFormat().format(num || 0)
    }
  },

  beforeUnmount() {
    if (this.chart) {
      this.chart.dispose()
    }
  }
}
</script>


<style scoped>
  .savings-goal-calculator {
    min-height: 100vh;
    background: #f8f9fa;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    padding: 40px 20px;
  }

  .header {
    text-align: center;
    margin-bottom: 40px;
  }

  .header h1 {
    font-size: 32px;
    font-weight: 600;
    color: #333;
    margin: 0 0 8px 0;
  }

  .header p {
    font-size: 16px;
    color: #666;
    margin: 0;
  }

  .main-content {
    max-width: 1200px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 40px;
    align-items: stretch; /* CHANGED: equal height columns */
  }

  .form-section {
    background: white;
    padding: 30px;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  }

  .form-group {
    margin-bottom: 20px;
  }

  .form-group label {
    display: block;
    font-size: 14px;
    font-weight: 500;
    color: #333;
    margin-bottom: 6px;
  }

  .form-input {
    width: 100%;
    padding: 12px 16px;
    border: 1px solid #ddd;
    border-radius: 6px;
    font-size: 14px;
    background: white;
    box-sizing: border-box;
  }

  .form-input:focus {
    outline: none;
    border-color: #007bff;
    box-shadow: 0 0 0 2px rgba(0,123,255,0.25);
  }

  .form-row {
    display: grid;
    grid-template-columns: 1fr 120px;
    gap: 12px;
    align-items: end;
  }

  .timeline-group {
    margin-bottom: 0;
  }

  .unit-group {
    margin-bottom: 0;
  }

  .unit-group label {
    visibility: hidden;
    height: 20px;
    margin-bottom: 6px;
  }

  .timeline-input {
    width: 100%;
  }

  .form-select {
    padding: 12px 16px;
    border: 1px solid #ddd;
    border-radius: 6px;
    font-size: 14px;
    background: white;
    cursor: pointer;
    box-sizing: border-box;
  }

  .form-select:focus {
    outline: none;
    border-color: #007bff;
    box-shadow: 0 0 0 2px rgba(0,123,255,0.25);
  }

  .calculate-btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    height: 48px;
    padding: 0 16px;
    border-radius: 8px;
    line-height: 1;
    background: #4F46E5;
    border: 1px solid #4F46E5;
    color: #fff;
    cursor: pointer;
    font-size: 16px;
    font-weight: 600;
    letter-spacing: .2px;
    transition: background-color .2s, box-shadow .2s;
  }

  .calculate-btn:hover {
    background: #4338CA;
    color: #fff;
  }

  .calculate-btn:focus-visible {
    outline: 3px solid rgba(79, 70, 229, .35);
    outline-offset: 2px;
  }

  .results-section {
    display: flex;
    flex-direction: column;
    gap: 24px;
  }

  .savings-plan {
    background: #e8f5e8;
    padding: 24px;
    border-radius: 12px;
  }

  .savings-plan h3 {
    font-size: 18px;
    font-weight: 600;
    color: #333;
    margin: 0 0 16px 0;
  }

  .monthly-amount {
    text-align: center;
    margin-bottom: 20px;
  }

  .monthly-amount .amount {
    display: block;
    font-size: 36px;
    font-weight: 700;
    color: #28a745;
    margin-bottom: 4px;
  }

  .monthly-amount .label {
    font-size: 14px;
    color: #666;
  }

  .breakdown {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
  }

  .breakdown-item {
    text-align: center;
    padding: 16px;
    border-radius: 8px;
  }

  .breakdown-item.blue {
    background: rgba(0, 123, 255, 0.1);
  }

  .breakdown-item.purple {
    background: rgba(108, 117, 125, 0.1);
  }

  .breakdown-item .value {
    display: block;
    font-size: 20px;
    font-weight: 600;
    margin-bottom: 4px;
  }

  .breakdown-item.blue .value {
    color: #007bff;
  }

  .breakdown-item.purple .value {
    color: #6c757d;
  }

  .breakdown-item .label {
    font-size: 12px;
    color: #666;
  }

  .progress-visualization {
    background: white;
    padding: 24px;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  }

  .progress-visualization h4 {
    font-size: 16px;
    font-weight: 600;
    color: #333;
    margin: 0 0 16px 0;
  }

  .chart-container {
    width: 100%;
    height: 200px;
  }

  .goal-breakdown {
    background: white;
    padding: 24px;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  }

  .goal-breakdown h4 {
    font-size: 16px;
    font-weight: 600;
    color: #333;
    margin: 0 0 16px 0;
  }

  .breakdown-table {
    display: flex;
    flex-direction: column;
    gap: 12px;
  }

  .breakdown-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 8px 0;
  }

  .breakdown-row .label {
    font-size: 14px;
    color: #666;
  }

  .breakdown-row .value {
    font-size: 14px;
    font-weight: 600;
    color: #333;
  }

  @media (max-width: 768px) {
    .main-content {
      grid-template-columns: 1fr;
      gap: 24px;
    }

    .form-row {
      grid-template-columns: 1fr;
      gap: 12px;
    }

    .breakdown {
      grid-template-columns: 1fr;
    }
  }

  .status-wrap {
  min-height: 18px;          /* keeps space even when empty */
  margin-top: 10px;
}

.status-msg {
  margin: 0;
  padding: 10px 12px;
  border-radius: 8px;
  font-size: 14px;
  line-height: 1.3;
  border: 1px solid transparent;
}

/* Variants */
.is-info {
  background: #eef2ff;
  border-color: #c7d2fe;
  color: #3730a3;
}
.is-success {
  background: #ecfdf5;
  border-color: #a7f3d0;
  color: #065f46;
}
.is-warn {
  background: #fffbeb;
  border-color: #fde68a;
  color: #92400e;
}
.is-error {
  background: #fef2f2;
  border-color: #fecaca;
  color: #991b1b;
}

</style>
