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
      monthlyAmount: '0',
      weeklyAmount: '0',
      chart: null
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
    }
  },
  mounted() {
    // Remove auto-calculation on mount
  },
  methods: {
    calculateSavings() {
      const goal = this.savingsGoalNum
      const initial = this.initialDepositNum
      const rate = parseFloat(this.interestRate) || 0
      const duration = this.timelineNum
      
      let months = duration
      if (this.timeUnit === 'weeks') {
        months = duration / 4.33
      } else if (this.timeUnit === 'years') {
        months = duration * 12
      }
      
      const monthlyRate = rate / 100 / 12
      const amountNeeded = goal - initial
      
      if (rate > 0) {
        // With interest calculation
        const futureValueOfInitial = initial * Math.pow(1 + monthlyRate, months)
        const remainingAmount = goal - futureValueOfInitial
        this.monthlyAmount = Math.round(remainingAmount / (((Math.pow(1 + monthlyRate, months) - 1) / monthlyRate))).toString()
      } else {
        // Without interest
        this.monthlyAmount = Math.round(amountNeeded / months).toString()
      }
      
      this.weeklyAmount = Math.round(parseFloat(this.monthlyAmount) / 4.33).toString()
      
      this.$nextTick(() => {
        this.initChart()
      })
    },
    
    initChart() {
      if (this.chart) {
        this.chart.dispose()
      }
      
      const chartDom = this.$refs.chartCanvas
      if (!chartDom) return
      
      this.chart = echarts.init(chartDom)
      
      // 固定显示12个月的数据，与设计图一致
      const data = []
      const categories = []
      let accumulated = this.initialDepositNum
      
      for (let i = 0; i <= 12; i++) {
        categories.push(i)
        data.push(accumulated)
        if (i < 12) {
          accumulated += parseFloat(this.monthlyAmount) || 750
        }
      }
      
      const option = {
        grid: {
          left: '8%',
          right: '8%',
          bottom: '15%',
          top: '8%'
        },
        xAxis: {
          type: 'category',
          data: categories,
          name: 'Months',
          nameLocation: 'middle',
          nameGap: 20,
          nameTextStyle: {
            color: '#666',
            fontSize: 12
          },
          axisLine: {
            show: true,
            lineStyle: {
              color: '#ddd'
            }
          },
          axisTick: {
            show: true,
            lineStyle: {
              color: '#ddd'
            }
          },
          axisLabel: {
            color: '#666',
            fontSize: 11
          }
        },
        yAxis: {
          type: 'value',
          name: 'Amount ($)',
          nameLocation: 'middle',
          nameGap: 35,
          nameTextStyle: {
            color: '#666',
            fontSize: 12
          },
          min: 0,
          max: 12000,
          interval: 2000,
          axisLine: {
            show: true,
            lineStyle: {
              color: '#ddd'
            }
          },
          axisTick: {
            show: true,
            lineStyle: {
              color: '#ddd'
            }
          },
          axisLabel: {
            color: '#666',
            fontSize: 11,
            formatter: '{value}'
          },
          splitLine: {
            show: true,
            lineStyle: {
              color: '#f0f0f0',
              type: 'solid'
            }
          }
        },
        series: [{
          data: data,
          type: 'line',
          smooth: true,
          lineStyle: {
            color: '#28a745',
            width: 2
          },
          itemStyle: {
            color: '#28a745',
            borderWidth: 0
          },
          symbol: 'circle',
          symbolSize: 3,
          showSymbol: true,
          areaStyle: {
            color: {
              type: 'linear',
              x: 0,
              y: 0,
              x2: 0,
              y2: 1,
              colorStops: [{
                offset: 0, color: 'rgba(40, 167, 69, 0.15)'
              }, {
                offset: 1, color: 'rgba(40, 167, 69, 0.02)'
              }]
            }
          }
        }]
      }
      
      this.chart.setOption(option)
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
    grid-template-columns: 400px 1fr;
    gap: 40px;
    align-items: start;
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
</style>