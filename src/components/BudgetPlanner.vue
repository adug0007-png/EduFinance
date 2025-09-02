<template>
  <div class="budget-planner">
    <!-- Header -->
    <div class="header">
      <div class="header-content">
        <div class="logo">
          <div class="logo-icon">💰</div>
          <span class="logo-text">Budget & Savings Tools</span>
        </div>
        <div class="nav-links">
          <!-- 导航链接已移除 -->
        </div>


      </div>
    </div>

    <!-- Main Content -->
    <div class="main-content">
      <div class="container">
        <!-- Title Section -->
        <div class="title-section">
          <h1>Personal Budget Planner</h1>
          <p>Track your income and expenses with our intuitive planner to maintain perfect financial balance</p>
        </div>

        <!-- Budget Form and Summary -->
        <div class="budget-section">
          <!-- Left Side - Form -->
          <div class="form-section">
            <!-- Monthly Income -->
            <div class="income-section">
              <div class="section-header">
                <div class="section-icon green">●</div>
                <h3>Monthly Income</h3>
              </div>
              
              <div class="form-group">
                <label>Salary</label>
                <input type="text" v-model="income.salary" placeholder="Enter your monthly salary">
              </div>
              
              <div class="form-group">
                <label>Investments</label>
                <input type="text" v-model="income.investments" placeholder="Investment returns">
              </div>
              
              <div class="form-group">
                <label>Other Income</label>
                <input type="text" v-model="income.other" placeholder="Freelance, side jobs, etc.">
              </div>
            </div>

            <!-- Monthly Expenses -->
            <div class="expenses-section">
              <div class="section-header">
                <div class="section-icon red">●</div>
                <h3>Monthly Expenses</h3>
              </div>
              
              <div class="form-group">
                <label>Housing</label>
                <input type="text" v-model="expenses.housing" placeholder="Rent, mortgage, utilities">
              </div>
              
              <div class="form-group">
                <label>Transportation</label>
                <input type="text" v-model="expenses.transportation" placeholder="Car payments, gas, public transport">
              </div>
              
              <div class="form-group">
                <label>Food & Dining</label>
                <input type="text" v-model="expenses.food" placeholder="Groceries, restaurants">
              </div>
              
              <div class="form-group">
                <label>Entertainment</label>
                <input type="text" v-model="expenses.entertainment" placeholder="Movies, subscriptions, hobbies">
              </div>
              
              <div class="form-group">
                <label>Healthcare</label>
                <input type="text" v-model="expenses.healthcare" placeholder="Insurance, medical expenses">
              </div>
            </div>

            <button class="calculate-btn" @click="calculateBudget">Calculate Budget</button>
          </div>

          <!-- Right Side - Summary and Chart -->
          <div class="summary-section">
            <!-- Budget Summary -->
            <div class="budget-summary">
              <h3>Budget Summary</h3>
              <div class="summary-item">
                <span>Total Income</span>
                <span class="amount green">${{ totalIncome.toLocaleString() }}</span>
              </div>
              <div class="summary-item">
                <span>Total Expenses</span>
                <span class="amount red">${{ totalExpenses.toLocaleString() }}</span>
              </div>
              <div class="summary-item balance">
                <span>Balance</span>
                <span class="amount" :class="balance >= 0 ? 'green' : 'red'">${{ balance.toLocaleString() }}</span>
              </div>
            </div>

            <!-- Expense Distribution Chart -->
            <div class="chart-section">
              <div ref="chartRef" class="chart-container" style="width: 100%; height: 500px; background: #f8f9fa;"></div>
            </div>
          </div>
        </div>

        <!-- Overspending Alerts -->
        <div class="alerts-section">
          <h2>Overspending Alerts</h2>
          <p>Real-time monitoring of your spending patterns to help you stay within budget limits</p>
          
          <div class="alerts-grid">
            <div
              v-for="cat in categories"
              :key="cat.key"
              class="alert-card"
              :class="statusClass(cat)"
            >
              <div class="alert-header">
                <h4>{{ cat.name }}</h4>
                <div class="alert-icon">{{ statusIcon(cat) }}</div>
              </div>
              <div class="alert-content">
                <template v-if="!cat.isEditing">
                  <div class="alert-row">
                    <span>Spent</span>
                    <span>${{ formatNumber(cat.spent) }}</span>
                  </div>
                  <div class="alert-row">
                    <span>Budget</span>
                    <span>${{ formatNumber(cat.budget) }}</span>
                  </div>
                  <div class="progress-bar">
                    <div
                      class="progress-fill"
                      :class="barClass(cat)"
                      :style="{ width: progressWidth(cat) }"
                    ></div>
                  </div>
                  <div class="alert-status">{{ percentUsed(cat) }}% used - {{ statusText(cat) }}</div>
                  <button class="adjust-btn" @click="startEdit(cat)">Adjust Budget</button>
                </template>
                <template v-else>
                  <div class="form-group">
                    <label>Spent</label>
                    <input type="number" v-model="cat.formSpent" placeholder="Enter spent">
                  </div>
                  <div class="form-group">
                    <label>Budget</label>
                    <input type="number" v-model="cat.formBudget" placeholder="Enter budget">
                  </div>
                  <div class="adjust-buttons">
                    <button class="adjust-btn primary" @click="applyEdit(cat)">Calculate</button>
                    <button class="adjust-btn secondary" @click="cancelEdit(cat)">Cancel</button>
                  </div>
                </template>
              </div>
            </div>
          </div>
        </div>

        <!-- Savings Goal Calculator Section -->
        <div class="savings-calculator-section">
          <div class="calc-header">
            <h2>Savings Goal Calculator</h2>
            <p>Set your financial goals and discover how much you need to save</p>
          </div>
          <div class="calculator-card">
            <div class="calculator-container">
              <div class="calculator-left">
                <div class="form-section">
                  <div class="form-group">
                    <label>Savings Goal</label>
                    <input type="text" v-model="savingsGoal" placeholder="Enter your target amount">
                  </div>
                  
                  <div class="form-group">
                    <label>Timeline</label>
                    <div class="timeline-group">
                      <input type="number" v-model="duration" placeholder="Duration">
                      <select v-model="timeUnit">
                        <option value="weeks">Weeks</option>
                        <option value="months">Months</option>
                        <option value="years">Years</option>
                      </select>
                    </div>
                  </div>
                  
                  <div class="form-group">
                    <label>Initial Deposit (Optional)</label>
                    <input type="text" v-model="initialDeposit" placeholder="Amount you already have saved">
                  </div>
                  
                  <div class="form-group">
                    <label>Interest Rate (Annual %)</label>
                    <input type="text" v-model="interestRate" placeholder="Expected annual interest rate">
                  </div>
                  
                  <button class="calculate-savings-btn" @click="calculateSavings">Calculate Savings Plan</button>
                </div>
              </div>
              
              <div class="calculator-right">
                <div class="savings-plan-card">
                  <h3>Your Savings Plan</h3>
                  <div class="plan-box">
                    <div class="plan-amount">
                      <span class="currency">$</span>
                      <span class="amount">{{ formatNumber(monthlyAmount) }}</span>
                    </div>
                    <p class="plan-description">Required savings per month</p>
                  </div>
                  <div class="stat-pills">
                    <div class="stat-pill">
                      <div class="pill-amount blue">${{ formatNumber(weeklyAmount) }}</div>
                      <div class="pill-label">Per Week</div>
                    </div>
                    <div class="stat-pill">
                      <div class="pill-amount purple">${{ formatNumber(monthlyAmount) }}</div>
                      <div class="pill-label">Per Month</div>
                    </div>
                  </div>
                </div>
                
                <div class="chart-section">
                  <h4>Progress Visualization</h4>
                  <div ref="savingsChartRef" class="savings-chart"></div>
                </div>
                
                <div class="goal-breakdown">
                  <h4>Goal Breakdown</h4>
                  <div class="breakdown-table">
                    <div class="breakdown-row">
                      <span class="breakdown-label">Target Amount</span>
                      <span class="breakdown-value">${{ formatNumber(savingsGoal) }}</span>
                    </div>
                    <div class="breakdown-row">
                      <span class="breakdown-label">Initial Deposit</span>
                      <span class="breakdown-value">${{ formatNumber(initialDeposit) }}</span>
                    </div>
                    <div class="breakdown-row">
                      <span class="breakdown-label">Amount to Save</span>
                      <span class="breakdown-value">${{ formatNumber(amountToSave) }}</span>
                    </div>
                    <div class="breakdown-row">
                      <span class="breakdown-label">Timeline</span>
                      <span class="breakdown-value">{{ duration }} {{ timeUnit }}</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

      </div>
    </div>

    <!-- Footer -->
    <div class="footer">
      <div class="footer-content">
        <div class="footer-left">
          <div class="footer-logo">
            <span class="footer-icon">📊</span>
            <span class="footer-text">© 2025 Budget & Savings Tools. All rights reserved.</span>
          </div>
        </div>
        <div class="footer-right">
          <div class="payment-icons">
            <div class="payment-icon visa">VISA</div>
            <div class="payment-icon mastercard">MC</div>
            <div class="payment-icon paypal">P</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { onMounted, ref, watch, computed } from 'vue'
import * as echarts from 'echarts'

export default {
  name: 'BudgetPlanner',
  setup() {
    const chartRef = ref(null)
    let chart = null
    
    const income = ref({
      salary: '',
      investments: '',
      other: ''
    })
    
    const expenses = ref({
      housing: '',
      transportation: '',
      food: '',
      entertainment: '',
      healthcare: ''
    })
    
    // Savings Goal Calculator data
    const savingsChartRef = ref(null)
    let savingsChart = null
    
    const savingsGoal = ref('10000')
    const duration = ref('12')
    const timeUnit = ref('months')
    const initialDeposit = ref('1000')
    const interestRate = ref('5')
    
    const monthlyAmount = ref('750')
    const weeklyAmount = ref('173')
    const amountToSave = ref('9000')
    
    const initChart = () => {
      console.log('initChart called', chartRef.value)
      if (chartRef.value && !chart) {
        console.log('Initializing chart...')
        // 添加小延迟确保DOM完全渲染
        setTimeout(() => {
          chart = echarts.init(chartRef.value)
          console.log('Chart initialized:', chart)
          updateChart()
          window.addEventListener('resize', () => chart.resize())
        }, 100)
      }
    }
    
    const updateChart = () => {
      if (!chart) return
      
      const data = [
        { value: parseFloat(expenses.value.housing) || 0, name: 'Housing', itemStyle: { color: '#4285F4' } },
        { value: parseFloat(expenses.value.transportation) || 0, name: 'Transportation', itemStyle: { color: '#34A853' } },
        { value: parseFloat(expenses.value.food) || 0, name: 'Food & Dining', itemStyle: { color: '#FBBC05' } },
        { value: parseFloat(expenses.value.entertainment) || 0, name: 'Entertainment', itemStyle: { color: '#EA4335' } },
        { value: parseFloat(expenses.value.healthcare) || 0, name: 'Healthcare', itemStyle: { color: '#9C27B0' } }
      ].filter(item => item.value > 0)
      
      const option = {
        title: {
          text: 'Expense Distribution',
          left: 'center',
          top: 15,
          textStyle: {
            fontSize: 18,
            fontWeight: 'bold',
            color: '#333'
          }
        },
        tooltip: {
          trigger: 'item',
          formatter: '{a} <br/>{b}: ${c} ({d}%)'
        },
        legend: {
          orient: 'horizontal',
          bottom: 10,
          left: 'center',
          itemWidth: 14,
          itemHeight: 14,
          textStyle: {
            fontSize: 12
          }
        },
        series: [
            {
              name: 'Expenses',
              type: 'pie',
              radius: ['40%', '75%'],
              center: ['50%', '55%'],
              avoidLabelOverlap: true,
            itemStyle: {
              borderRadius: 8,
              borderColor: '#fff',
              borderWidth: 2
            },
            label: {
              show: true,
              position: 'outside',
              fontSize: 11,
              formatter: '{b}\n${c}'
            },
            emphasis: {
              label: {
                show: true,
                fontSize: 13,
                fontWeight: 'bold'
              }
            },
            labelLine: {
              show: true,
              length: 15,
              length2: 10
            },
            data: data.length > 0 ? data : [{ value: 1, name: 'No Data', itemStyle: { color: '#e2e8f0' } }]
          }
        ]
      }
      
      chart.setOption(option)
    }
    
    // 初始化为0，只有点击Calculate Budget后才计算
    const totalIncome = ref(0)
    const totalExpenses = ref(0)
    const balance = ref(0)

    // Overspending Alerts - dynamic categories with edit/apply flow
    const categories = ref([
      { key: 'housing', name: 'Housing', spent: 1800, budget: 2000, isEditing: false, formSpent: '', formBudget: '' },
      { key: 'transportation', name: 'Transportation', spent: 650, budget: 500, isEditing: false, formSpent: '', formBudget: '' },
      { key: 'food', name: 'Food & Dining', spent: 400, budget: 600, isEditing: false, formSpent: '', formBudget: '' },
      { key: 'entertainment', name: 'Entertainment', spent: 200, budget: 300, isEditing: false, formSpent: '', formBudget: '' },
      { key: 'healthcare', name: 'Healthcare', spent: 150, budget: 200, isEditing: false, formSpent: '', formBudget: '' },
      { key: 'shopping', name: 'Shopping', spent: 450, budget: 400, isEditing: false, formSpent: '', formBudget: '' }
    ])

    const percentUsed = (cat) => {
      const spent = parseFloat(cat.spent) || 0
      const budget = parseFloat(cat.budget) || 0
      if (budget <= 0) return spent > 0 ? 100 : 0
      return Math.round((spent / budget) * 100)
    }

    const statusClass = (cat) => {
      const p = percentUsed(cat)
      if (p > 100) return 'exceeded'
      if (p >= 90) return 'warning'
      return 'good'
    }

    const barClass = (cat) => {
      const cls = statusClass(cat)
      if (cls === 'exceeded') return 'exceeded'
      if (cls === 'warning') return 'warning'
      return 'good'
    }

    const progressWidth = (cat) => {
      const p = percentUsed(cat)
      return Math.min(p, 100) + '%'
    }

    const statusText = (cat) => {
      const p = percentUsed(cat)
      if (p > 100) return 'Exceeded'
      if (p >= 90) return 'Warning'
      return 'Good'
    }

    const statusIcon = (cat) => {
      const p = percentUsed(cat)
      if (p > 100) return '🚫'
      if (p >= 90) return '⚠️'
      return '✅'
    }

    const startEdit = (cat) => {
      cat.formSpent = cat.spent.toString()
      cat.formBudget = cat.budget.toString()
      cat.isEditing = true
    }

    const cancelEdit = (cat) => {
      cat.formSpent = ''
      cat.formBudget = ''
      cat.isEditing = false
    }

    const applyEdit = (cat) => {
      const s = parseFloat(cat.formSpent) || 0
      const b = parseFloat(cat.formBudget) || 0
      cat.spent = s
      cat.budget = b
      cat.formSpent = ''
      cat.formBudget = ''
      cat.isEditing = false
      console.log(`Updated ${cat.name}: spent=${s}, budget=${b}`)
    }
    

    
    // Set default values
    income.value.salary = '5800'
    income.value.investments = '0'
    income.value.other = '0'
    expenses.value.housing = '1800'
    expenses.value.transportation = '650'
    expenses.value.food = '400'
    expenses.value.entertainment = '200'
    expenses.value.healthcare = '150'
    
    // 初始计算一次，显示默认值
    const salaryVal = parseFloat(income.value.salary) || 0
    const investmentsVal = parseFloat(income.value.investments) || 0
    const otherVal = parseFloat(income.value.other) || 0
    totalIncome.value = salaryVal + investmentsVal + otherVal
    
    const housingVal = parseFloat(expenses.value.housing) || 0
    const transportationVal = parseFloat(expenses.value.transportation) || 0
    const foodVal = parseFloat(expenses.value.food) || 0
    const entertainmentVal = parseFloat(expenses.value.entertainment) || 0
    const healthcareVal = parseFloat(expenses.value.healthcare) || 0
    totalExpenses.value = housingVal + transportationVal + foodVal + entertainmentVal + healthcareVal
    
    balance.value = totalIncome.value - totalExpenses.value
    
    const calculateBudget = () => {
      // Calculate totals
      const salaryVal = parseFloat(income.value.salary) || 0
      const investmentsVal = parseFloat(income.value.investments) || 0
      const otherVal = parseFloat(income.value.other) || 0
      totalIncome.value = salaryVal + investmentsVal + otherVal
      
      const housingVal = parseFloat(expenses.value.housing) || 0
      const transportationVal = parseFloat(expenses.value.transportation) || 0
      const foodVal = parseFloat(expenses.value.food) || 0
      const entertainmentVal = parseFloat(expenses.value.entertainment) || 0
      const healthcareVal = parseFloat(expenses.value.healthcare) || 0
      totalExpenses.value = housingVal + transportationVal + foodVal + entertainmentVal + healthcareVal
      
      balance.value = totalIncome.value - totalExpenses.value
      
      console.log('Budget calculated!')
      updateChart()
    }
    
    const calculateSavings = () => {
      const goal = parseFloat(savingsGoal.value) || 0
      const initial = parseFloat(initialDeposit.value) || 0
      const rate = parseFloat(interestRate.value) || 0
      const time = parseFloat(duration.value) || 1
      
      const remaining = goal - initial
      amountToSave.value = remaining.toString()
      
      if (timeUnit.value === 'months') {
        monthlyAmount.value = Math.round(remaining / time).toString()
        weeklyAmount.value = Math.round(remaining / (time * 4.33)).toString()
      } else if (timeUnit.value === 'weeks') {
        weeklyAmount.value = Math.round(remaining / time).toString()
        monthlyAmount.value = Math.round(remaining / (time / 4.33)).toString()
      } else if (timeUnit.value === 'years') {
        monthlyAmount.value = Math.round(remaining / (time * 12)).toString()
        weeklyAmount.value = Math.round(remaining / (time * 52)).toString()
      }
      
      updateSavingsChart()
    }
    
    const formatNumber = (value) => {
      const num = parseFloat(value) || 0
      return num.toLocaleString()
    }
    
    const initSavingsChart = () => {
      if (savingsChartRef.value && !savingsChart) {
        setTimeout(() => {
          console.log('Initializing savings chart...', savingsChartRef.value)
          savingsChart = echarts.init(savingsChartRef.value)
          console.log('Savings chart initialized:', savingsChart)
          updateSavingsChart()
          window.addEventListener('resize', () => savingsChart.resize())
        }, 200) // 增加延迟时间
      }
    }
    
    const updateSavingsChart = () => {
      if (!savingsChart) {
        console.log('Savings chart not initialized yet')
        return
      }
      
      const months = 12
      const monthlyTarget = parseFloat(monthlyAmount.value) || 750
      const initial = parseFloat(initialDeposit.value) || 1000
      
      const data = []
      for (let i = 0; i <= months; i++) {
        data.push(initial + (monthlyTarget * i))
      }
      
      console.log('Chart data:', data)
      
      const option = {
        grid: {
          left: '15%',
          right: '10%',
          top: '10%',
          bottom: '20%'
        },
        xAxis: {
          type: 'category',
          data: Array.from({length: 13}, (_, i) => i.toString()),
          axisLine: { show: false },
          axisTick: { show: false },
          axisLabel: {
            color: '#666',
            fontSize: 10
          }
        },
        yAxis: {
          type: 'value',
          axisLine: { show: false },
          axisTick: { show: false },
          splitLine: {
            lineStyle: {
              color: '#f0f0f0',
              type: 'solid'
            }
          },
          axisLabel: {
            color: '#666',
            fontSize: 10,
            formatter: function(value) {
              return '$' + (value/1000).toFixed(0) + 'k'
            }
          }
        },
        series: [{
          data: data,
          type: 'line',
          smooth: true,
          lineStyle: {
            color: '#28a745',
            width: 3
          },
          itemStyle: {
            color: '#28a745'
          },
          symbol: 'circle',
          symbolSize: 6,
          areaStyle: {
            color: {
              type: 'linear',
              x: 0,
              y: 0,
              x2: 0,
              y2: 1,
              colorStops: [{
                offset: 0, color: 'rgba(40, 167, 69, 0.3)'
              }, {
                offset: 1, color: 'rgba(40, 167, 69, 0.05)'
              }]
            }
          }
        }]
      }
      
      savingsChart.setOption(option, true) // 强制重新渲染
      console.log('Chart option set')
    }
    
    onMounted(() => {
      initChart()
      initSavingsChart()
    })
    
    return {
      chartRef,
      savingsChartRef,
      income,
      expenses,
      totalIncome,
      totalExpenses,
      balance,
      categories,
      calculateBudget,
      savingsGoal,
      duration,
      timeUnit,
      initialDeposit,
      interestRate,
      monthlyAmount,
      weeklyAmount,
      amountToSave,
      calculateSavings,
      formatNumber,
      percentUsed,
      statusClass,
      statusText,
      barClass,
      progressWidth,
      statusIcon,
      startEdit,
      cancelEdit,
      applyEdit
    }
  }
}
</script>

<style scoped>
.budget-planner {
  min-height: 100vh;
  background: #f8fafc;
}

.header {
  background: white;
  border-bottom: 1px solid #e2e8f0;
  padding: 1rem 0;
}

.header-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.logo-icon {
  font-size: 1.5rem;
}

.logo-text {
  font-size: 1.25rem;
  font-weight: 600;
  color: #4F46E5;
}

.nav-links {
  display: flex;
  align-items: center;
  gap: 2rem;
}

.nav-link {
  color: #64748b;
  text-decoration: none;
  font-weight: 500;
}

.nav-link:hover {
  color: #334155;
}

.get-started-btn {
  background: #4F46E5;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 6px;
  font-size: 0.875rem;
  cursor: pointer;
}

.get-started-btn:hover {
  background: #4338CA;
}

.main-content {
  padding: 3rem 0;
}

.container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 2rem;
}

.title-section {
  text-align: center;
  margin-bottom: 3rem;
}

.title-section h1 {
  font-size: 2.5rem;
  font-weight: 700;
  color: #1e293b;
  margin-bottom: 1rem;
}

.title-section p {
  font-size: 1.125rem;
  color: #64748b;
  max-width: 600px;
  margin: 0 auto;
}

.budget-section {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 3rem;
  margin-bottom: 4rem;
}

.form-section {
  background: white;
  padding: 2rem;
  border-radius: 12px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.income-section,
.expenses-section {
  margin-bottom: 2rem;
}

.section-header {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 1.5rem;
}

.section-icon {
  width: 12px;
  height: 12px;
  border-radius: 50%;
}

.section-icon.green {
  background: #10B981;
}

.section-icon.red {
  background: #EF4444;
}

.section-header h3 {
  font-size: 1.25rem;
  font-weight: 600;
  color: #1e293b;
  margin: 0;
}

.form-group {
  margin-bottom: 1rem;
}

.form-group label {
  display: block;
  font-size: 0.875rem;
  font-weight: 500;
  color: #374151;
  margin-bottom: 0.5rem;
}

.form-group input {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #d1d5db;
  border-radius: 6px;
  font-size: 0.875rem;
  background: white;
}

.form-group input:focus {
  outline: none;
  border-color: #4F46E5;
  box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.1);
}

.calculate-btn {
  width: 100%;
  background: #4F46E5;
  color: white;
  border: none;
  padding: 0.875rem;
  border-radius: 6px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
}

.calculate-btn:hover {
  background: #4338CA;
}

.summary-section {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.budget-summary {
  background: white;
  padding: 1.5rem;
  border-radius: 12px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.budget-summary h3 {
  font-size: 1.125rem;
  font-weight: 600;
  color: #1e293b;
  margin-bottom: 1rem;
}

.summary-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.75rem 0;
  border-bottom: 1px solid #f1f5f9;
}

.summary-item:last-child {
  border-bottom: none;
}

.summary-item.balance {
  font-weight: 600;
  font-size: 1.125rem;
}

.amount.green {
  color: #10B981;
}

.amount.red {
  color: #EF4444;
}

.chart-section {
  background: white;
  padding: 1.5rem;
  border-radius: 12px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.chart-section h3 {
  font-size: 1.125rem;
  font-weight: 600;
  color: #1e293b;
  margin-bottom: 1rem;
}

.chart-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
}

.pie-chart {
  position: relative;
}

.pie-chart circle {
  fill: none;
  stroke-width: 40;
}

.chart-legend {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.legend-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.875rem;
}

.legend-color {
  width: 12px;
  height: 12px;
  border-radius: 2px;
}

.alerts-section {
  margin-bottom: 3rem;
}

.alerts-section h2 {
  font-size: 2rem;
  font-weight: 700;
  color: #1e293b;
  text-align: center;
  margin-bottom: 0.5rem;
}

.alerts-section p {
  font-size: 1.125rem;
  color: #64748b;
  text-align: center;
  margin-bottom: 2rem;
}

.alerts-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
}

.alert-card {
  background: white;
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  border-left: 4px solid;
}

.alert-card.warning {
  border-left-color: #F59E0B;
}

.alert-card.exceeded {
  border-left-color: #EF4444;
}

.alert-card.good {
  border-left-color: #10B981;
}

.alert-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.alert-header h4 {
  font-size: 1.125rem;
  font-weight: 600;
  color: #1e293b;
  margin: 0;
}

.alert-content {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.alert-row {
  display: flex;
  justify-content: space-between;
  font-size: 0.875rem;
  color: #64748b;
}

.progress-bar {
  width: 100%;
  height: 8px;
  background: #f1f5f9;
  border-radius: 4px;
  overflow: hidden;
}

.progress-fill {
  height: 100%;
  border-radius: 4px;
}

.progress-fill.warning {
  background: #F59E0B;
}

.progress-fill.exceeded {
  background: #EF4444;
}

.progress-fill.good {
  background: #10B981;
}

.alert-status {
  font-size: 0.875rem;
  font-weight: 500;
}

.alert-card.warning .alert-status {
  color: #F59E0B;
}

.alert-card.exceeded .alert-status {
  color: #EF4444;
}

.alert-card.good .alert-status {
  color: #10B981;
}

.adjust-btn {
  background: #f8fafc;
  color: #64748b;
  border: 1px solid #e2e8f0;
  padding: 0.5rem 1rem;
  border-radius: 6px;
  font-size: 0.875rem;
  cursor: pointer;
  flex: 1;
}

.adjust-btn:hover {
  background: #f1f5f9;
}

.adjust-btn.primary {
  background: #4F46E5;
  color: white;
  border-color: #4F46E5;
}

.adjust-btn.primary:hover {
  background: #4338CA;
}

.adjust-btn.secondary {
  background: #ef4444;
  color: white;
  border-color: #ef4444;
}

.adjust-btn.secondary:hover {
  background: #dc2626;
}

.adjust-buttons {
  display: flex;
  gap: 0.5rem;
  margin-top: 0.5rem;
}

/* Fix form inputs in alert cards */
.alert-card .form-group {
  margin-bottom: 0.75rem;
}

.alert-card .form-group input {
  width: 100%;
  box-sizing: border-box;
  padding: 0.5rem;
  border: 1px solid #d1d5db;
  border-radius: 6px;
  font-size: 0.875rem;
}

.alert-card .form-group label {
  display: block;
  font-size: 0.75rem;
  font-weight: 500;
  color: #374151;
  margin-bottom: 0.25rem;
}

.chart-center-text {
  font-size: 14px;
  fill: #64748b;
  font-weight: 500;
}

.chart-container {
  width: 100%;
  height: 500px;
  min-height: 500px;
}

@media (max-width: 1024px) {
  .budget-section {
    grid-template-columns: 1fr;
    gap: 2rem;
  }
  
  .alerts-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

/* Footer Styles */
.footer {
  background: #1f2937;
  color: white;
  padding: 2rem 0;
  margin-top: 4rem;
}

.footer-content {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.footer-left {
  display: flex;
  align-items: center;
}

.footer-logo {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.footer-icon {
  font-size: 1.5rem;
}

.footer-text {
  font-size: 0.9rem;
  color: #d1d5db;
}

.footer-right {
  display: flex;
  align-items: center;
}

.payment-icons {
  display: flex;
  gap: 1rem;
}

.payment-icon {
  padding: 0.5rem 1rem;
  border-radius: 6px;
  font-size: 0.8rem;
  font-weight: 600;
  color: white;
}

.payment-icon.visa {
  background: #1a1f71;
}

.payment-icon.mastercard {
  background: #eb001b;
}

.payment-icon.paypal {
  background: #003087;
}

/* Savings Goal Calculator Section */
.savings-calculator-section {
  margin-top: 3rem;
  background: transparent;
}

/* Centered header above card */
.calc-header {
  text-align: center;
  margin-bottom: 0.75rem;
}
.calc-header h2 {
  font-size: 1.5rem;
  font-weight: 800;
  color: #111827;
}
.calc-header p {
  margin-top: 0.25rem;
  color: #6b7280;
  font-size: 0.92rem;
}

/* White card wrapper that contains the two columns */
.calculator-card {
  background: #ffffff;
  border-radius: 14px;
  box-shadow: 0 12px 24px rgba(0,0,0,0.08);
  padding: 0.75rem 0.75rem 1.25rem;
}

/* Layout */
.calculator-container {
  display: grid;
  grid-template-columns: 400px 1fr;
  min-height: 560px;
}

.calculator-left {
  padding: 1.5rem;
  background: #f8f9fa;
  border-right: 1px solid #e9ecef;
}

/* 调整储蓄计算器布局为左右各占一半 */
.savings-calculator-section .calculator-container { grid-template-columns: 1fr 1fr; }
.calculator-left {
  padding: 1.5rem;
  background: #f8f9fa;
  border-right: 1px solid #e9ecef;
}

/* Make left column blend with card; remove divider */
.savings-calculator-section .calculator-left { background: transparent; border-right: 0; }
/* Inner form becomes subtle white card (no heavy shadow) */
.savings-calculator-section .calculator-left .form-section { background: #ffffff; border: 1px solid #e5e7eb; border-radius: 10px; box-shadow: none; padding: 1rem; }
/* Larger green amount like mock */
.plan-amount .amount { font-size: 2rem; font-weight: 800; }
.timeline-group {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 0.5rem;
}
.timeline-group input,
.timeline-group select {
  padding: 0.75rem;
  border: 1px solid #d1d5db;
  border-radius: 6px;
  font-size: 0.9rem;
  background: #fff;
}
.timeline-group select { min-width: 100px; }

/* Right plan card styles */
.savings-plan-card {
  background: linear-gradient(180deg, #effaf3 0%, #f3fbf6 100%);
  border-radius: 10px;
  padding: 1rem;
}
.savings-plan-card h3 {
  font-size: 1rem;
  font-weight: 700;
  color: #1f2937;
  margin-bottom: 0.75rem;
}

.plan-box {
  background: #ffffff;
  border: 1px solid #e5e7eb;
  border-radius: 10px;
  padding: 1rem;
}
.plan-amount .currency { color: #16a34a; font-weight: 700; }
.plan-amount .amount { color: #16a34a; font-size: 1.75rem; font-weight: 800; }
.plan-description { margin-top: 0.25rem; color: #6b7280; font-size: 0.85rem; }

.stat-pills { display: grid; grid-template-columns: 1fr 1fr; gap: 0.75rem; margin-top: 0.75rem; }
.stat-pill { background: #ffffff; border: 1px solid #e5e7eb; border-radius: 10px; padding: 0.75rem; text-align: center; }
.pill-amount { font-weight: 800; }
.pill-amount.blue { color: #2563eb; }
.pill-amount.purple { color: #7c3aed; }
.pill-label { font-size: 0.75rem; color: #6b7280; }

/* Chart and breakdown keep previous spacing */
.savings-chart { 
  width: 100%; 
  height: 200px; 
  background: #f8f9fa;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
}

/* 修复输入框布局问题 */
.savings-calculator-section .form-group input {
  width: 100%;
  box-sizing: border-box;
  border: 1px solid #e5e7eb;
  border-radius: 10px;
  padding: 0.75rem;
  font-size: 0.9rem;
}

.savings-calculator-section .form-group input::placeholder {
  color: #9ca3af;
}

.timeline-group {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 0.5rem;
}

.timeline-group input {
  min-width: 0; /* 防止输入框溢出 */
}
.timeline-group select { min-width: 100px; }

/* Right plan card styles */
.savings-plan-card {
  background: linear-gradient(180deg, #effaf3 0%, #f3fbf6 100%);
  border-radius: 10px;
  padding: 1rem;
}
.savings-plan-card h3 {
  font-size: 1rem;
  font-weight: 700;
  color: #1f2937;
  margin-bottom: 0.75rem;
}

.plan-box {
  background: #ffffff;
  border: 1px solid #e5e7eb;
  border-radius: 10px;
  padding: 1rem;
}
.plan-amount .currency { color: #16a34a; font-weight: 700; }
.plan-amount .amount { color: #16a34a; font-size: 1.75rem; font-weight: 800; }
.plan-description { margin-top: 0.25rem; color: #6b7280; font-size: 0.85rem; }

.stat-pills { display: grid; grid-template-columns: 1fr 1fr; gap: 0.75rem; margin-top: 0.75rem; }
.stat-pill { background: #ffffff; border: 1px solid #e5e7eb; border-radius: 10px; padding: 0.75rem; text-align: center; }
.pill-amount { font-weight: 800; }
.pill-amount.blue { color: #2563eb; }
.pill-amount.purple { color: #7c3aed; }
.pill-label { font-size: 0.75rem; color: #6b7280; }

/* Chart section title for h4 */
.chart-section h4 {
  font-size: 0.95rem;
  font-weight: 700;
  color: #1f2937;
  margin-bottom: 0.75rem;
}

/* Calculate Savings Plan 按钮样式 */
.calculate-savings-btn {
  width: 100%;
  background: #16a34a;
  color: white;
  border: none;
  padding: 0.875rem;
  border-radius: 10px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  margin-top: 1rem;
}

.calculate-savings-btn:hover {
  background: #15803d;
}

/* Goal Breakdown 样式调整 */
.goal-breakdown {
  margin-top: 1rem;
}

.goal-breakdown h4 {
  font-size: 0.95rem;
  font-weight: 700;
  color: #1f2937;
  margin-bottom: 0.75rem;
}

.breakdown-table {
  background: #ffffff;
  border: 1px solid #e5e7eb;
  border-radius: 10px;
  padding: 1rem;
}

.breakdown-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.5rem 0;
  border-bottom: 1px solid #f3f4f6;
}

.breakdown-row:last-child {
  border-bottom: none;
}

.breakdown-label {
  font-size: 0.875rem;
  color: #6b7280;
  font-weight: 500;
}

.breakdown-value {
  font-size: 0.875rem;
  color: #1f2937;
  font-weight: 600;
}

/* Responsive tweak for mobile (keep) */
@media (max-width: 768px) {
  .calculator-right { padding: 0.75rem; }
  .calculator-container { grid-template-columns: 1fr; }
  .calculator-left { border-right: none; border-bottom: 1px solid #e9ecef; }
}

@media (max-width: 768px) {
  .alerts-grid {
    grid-template-columns: 1fr;
  }
  
  .header-content {
    flex-direction: column;
    gap: 1rem;
  }
  
  .nav-links {
    gap: 1rem;
  }
  

  
  .footer-content {
    flex-direction: column;
    gap: 1rem;
    text-align: center;
  }
  
  .payment-icons {
    justify-content: center;
  }
  
  .calculator-container {
    grid-template-columns: 1fr;
  }
  
  .calculator-left {
    border-right: none;
    border-bottom: 1px solid #e9ecef;
  }
  
  .breakdown-cards {
    grid-template-columns: 1fr;
  }
  
  .savings-chart {
    height: 150px;
  }
}
</style>