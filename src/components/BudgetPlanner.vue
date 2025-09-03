<template>
  <div class="budget-planner">
    <div class="main-content">
      <div class="container">
        <!-- 上：左表单 + 右 Flashcards -->
        <div class="budget-section">
          <!-- 左：预算表单 -->
          <div class="form-section">
            <!-- 收入 -->
            <div class="income-section">
              <div class="section-header">
                <div class="section-icon green"></div>
                <h3>Monthly Income</h3>
              </div>
              <div class="form-group">
                <label>Salary</label>
                <input type="text" v-model="income.salary" placeholder="Enter your monthly salary" />
              </div>
              <div class="form-group">
                <label>Investments</label>
                <input type="text" v-model="income.investments" placeholder="Investment returns" />
              </div>
              <div class="form-group">
                <label>Other Income</label>
                <input type="text" v-model="income.other" placeholder="Freelance, side jobs, etc." />
              </div>
            </div>

            <!-- 支出 -->
            <div class="expenses-section">
              <div class="section-header">
                <div class="section-icon red"></div>
                <h3>Monthly Expenses</h3>
              </div>
              <div class="form-group">
                <label>Housing</label>
                <input type="text" v-model="expenses.housing" placeholder="Rent, mortgage, utilities" />
              </div>
              <div class="form-group">
                <label>Transportation</label>
                <input type="text" v-model="expenses.transportation" placeholder="Car payments, gas, public transport" />
              </div>
              <div class="form-group">
                <label>Food & Dining</label>
                <input type="text" v-model="expenses.food" placeholder="Groceries, restaurants" />
              </div>
              <div class="form-group">
                <label>Entertainment</label>
                <input type="text" v-model="expenses.entertainment" placeholder="Movies, subscriptions, hobbies" />
              </div>
              <div class="form-group">
                <label>Healthcare</label>
                <input type="text" v-model="expenses.healthcare" placeholder="Insurance, medical expenses" />
              </div>
            </div>

            <button class="calculate-btn" @click="calculateBudget">Calculate Budget</button>
          </div>

          <!-- 右：Flashcards（图表 <-> Alerts） -->
          <div class="summary-section">
            <div class="flashcard">
              <div class="flashcard-header">
                <h3>{{ activeIndex === 0 ? 'Expense Distribution' : 'Overspending Alerts' }}</h3>
                <div class="nav">
                  <button class="nav-btn" @click="prevCard" aria-label="Previous">‹</button>
                  <button class="nav-btn" @click="nextCard" aria-label="Next">›</button>
                </div>
              </div>

              <!-- 用 v-show 不销毁 DOM，保持 ECharts 实例 -->
              <div class="flashcard-body">
                <!-- 卡片 1：支出分布（饼图） -->
                <div v-show="activeIndex === 0" class="pane">
                  <div class="chart-section">
                    <div ref="chartRef" class="chart-container"></div>
                  </div>
                </div>

                <!-- 卡片 2：Overspending Alerts（Spent 取左侧；Budget 可编辑） -->
                <div v-show="activeIndex === 1" class="pane">
                  <div class="alerts-intro">
                    <p class="muted">Real-time monitoring of your spending patterns</p>
                  </div>
                  <div class="alerts-grid compact">
                    <div
                      v-for="item in alertCards"
                      :key="item.key"
                      class="alert-card"
                      :class="statusClass(item)"
                    >
                      <div class="alert-header">
                        <h4>{{ item.name }}</h4>
                        <div class="alert-icon">{{ statusIcon(item) }}</div>
                      </div>

                      <div class="alert-content">
                        <div class="alert-row">
                          <span>Spent</span>
                          <span>${{ formatNumber(item.spent) }}</span>
                        </div>

                        <div class="alert-row editable">
                          <span>Budget</span>
                          <div class="budget-edit">
                            <span class="currency">$</span>
                            <input
                              type="number"
                              class="budget-input"
                              v-model.number="budgets[item.key]"
                              min="0"
                            />
                          </div>
                        </div>

                        <div class="progress-bar">
                          <div
                            class="progress-fill"
                            :class="barClass(item)"
                            :style="{ width: progressWidth(item) }"
                          ></div>
                        </div>
                        <div class="alert-status">
                          {{ percentUsed(item) }}% - {{ statusText(item) }}
                        </div>
                      </div>
                    </div>
                  </div>
                </div> <!-- /pane -->
              </div> <!-- /flashcard-body -->
            </div>
          </div>
        </div>

        <!-- 下：Savings Goal Calculator（右侧：进度环 + 堆叠面积图） -->
        <div class="savings-calculator-section">
          <div class="calc-header">
            <h2>Savings Goal Calculator</h2>
            <p>Set your financial goals and discover how much you need to save</p>
          </div>
          <div class="calculator-card">
            <div class="calculator-container">
              <!-- 左：表单（定宽） -->
              <div class="calculator-left">
                <div class="form-section">
                  <div class="form-group">
                    <label>Savings Goal</label>
                    <input type="text" v-model="savingsGoal" placeholder="Enter your target amount" />
                  </div>
                  <div class="form-group">
                    <label>Timeline</label>
                    <div class="timeline-group">
                      <input type="number" v-model="duration" placeholder="Duration" />
                      <select v-model="timeUnit">
                        <option value="weeks">Weeks</option>
                        <option value="months">Months</option>
                        <option value="years">Years</option>
                      </select>
                    </div>
                  </div>
                  <div class="form-group">
                    <label>Initial Deposit (Optional)</label>
                    <input type="text" v-model="initialDeposit" placeholder="Amount already saved" />
                  </div>
                  <div class="form-group">
                    <label>Interest Rate (Annual %)</label>
                    <input type="text" v-model="interestRate" placeholder="e.g. 5" />
                  </div>
                  <button class="calculate-savings-btn" @click="calculateSavings">Calculate Savings Plan</button>
                </div>
              </div>

              <!-- 右：结果 + 可视化 -->
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

                <div class="viz-grid">
                  <div class="viz-card ring-card">
                    <h4>Goal Progress</h4>
                    <div ref="goalRingRef" class="goal-ring"></div>
                    <div class="ring-caption">
                      <div class="ring-line"><span>Current</span><strong>${{ formatNumber(currentProjected) }}</strong></div>
                      <div class="ring-line"><span>Target</span><strong>${{ formatNumber(+savingsGoal || 0) }}</strong></div>
                    </div>
                  </div>

                  <div class="viz-card">
                    <h4>Principal vs Interest</h4>
                    <div ref="stackedChartRef" class="stacked-chart"></div>
                  </div>
                </div>
              </div>
            </div><!-- /calculator-container -->
          </div><!-- /calculator-card -->
        </div><!-- /savings-calculator-section -->
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted, computed, watch } from "vue";
import * as echarts from "echarts";

export default {
  name: "BudgetPlanner",
  setup() {
    /** ===== 左侧表单 ===== */
    const income = ref({ salary: "5800", investments: "0", other: "0" });
    const expenses = ref({
      housing: "1800",
      transportation: "650",
      food: "400",
      entertainment: "200",
      healthcare: "150",
    });

    /** ===== Flashcards 索引 ===== */
    const activeIndex = ref(0);
    const nextCard = () => (activeIndex.value = (activeIndex.value + 1) % 2);
    const prevCard = () => (activeIndex.value = (activeIndex.value + 1) % 2);

    /** ===== 饼图：Expense Distribution ===== */
    const chartRef = ref(null);
    let chart = null;

    const initChart = () => {
      if (!chartRef.value) return;
      if (!chart) {
        chart = echarts.init(chartRef.value);
        window.addEventListener("resize", () => chart && chart.resize());
      }
      updateChart();
    };

    const updateChart = () => {
      if (!chart) return;
      const data = [
        { value: parseFloat(expenses.value.housing) || 0,        name: "Housing" },
        { value: parseFloat(expenses.value.transportation) || 0, name: "Transportation" },
        { value: parseFloat(expenses.value.food) || 0,           name: "Food & Dining" },
        { value: parseFloat(expenses.value.entertainment) || 0,  name: "Entertainment" },
        { value: parseFloat(expenses.value.healthcare) || 0,     name: "Healthcare" },
      ];
      chart.setOption({
        tooltip: { trigger: "item", formatter: "{b}<br/>${c} ({d}%)" },
        legend: { bottom: 8 },
        series: [{
          name: "Expenses",
          type: "pie",
          radius: ["40%", "70%"],
          center: ["50%", "50%"],
          itemStyle: { borderRadius: 8, borderColor: "#fff", borderWidth: 2 },
          label: { formatter: "{b}\n${c}" },
          data: data.length ? data : [{ value: 1, name: "No Data" }],
        }],
      });
    };

    const calculateBudget = () => { if (chart) updateChart(); };

    /** ===== Alerts：Spent 来自左侧；Budget 可编辑 ===== */
    const categoryMeta = [
      { key: "housing",        name: "Housing" },
      { key: "transportation", name: "Transportation" },
      { key: "food",           name: "Food & Dining" },
      { key: "entertainment",  name: "Entertainment" },
      { key: "healthcare",     name: "Healthcare" },
    ];

    const budgets = ref({
      housing: 2000,
      transportation: 500,
      food: 600,
      entertainment: 300,
      healthcare: 200,
    });

    const alertCards = computed(() =>
      categoryMeta.map(m => {
        const spent  = parseFloat(expenses.value[m.key]) || 0;
        const budget = parseFloat(budgets.value[m.key]) || 0;
        return { ...m, spent, budget };
      })
    );

    const percentUsed = (item) => {
      const spent = item.spent || 0;
      const budget = item.budget || 0;
      if (budget <= 0) return spent > 0 ? 100 : 0;
      return Math.round((spent / budget) * 100);
    };
    const statusClass   = (item) => percentUsed(item) > 100 ? "exceeded" : (percentUsed(item) >= 90 ? "warning" : "good");
    const barClass      = (item) => statusClass(item);
    const progressWidth = (item) => Math.min(percentUsed(item), 100) + "%";
    const statusText    = (item) => percentUsed(item) > 100 ? "Exceeded" : (percentUsed(item) >= 90 ? "Warning" : "Good");
    const statusIcon    = (item) => percentUsed(item) > 100 ? "🚫" : (percentUsed(item) >= 90 ? "⚠️" : "✅");
    const formatNumber  = (v) => (parseFloat(v) || 0).toLocaleString();

    /** ===== Savings：进度环 + 堆叠面积图 ===== */
    const goalRingRef = ref(null);
    const stackedChartRef = ref(null);
    let goalRingChart = null;
    let stackedChart  = null;

    const savingsGoal     = ref("10000");
    const duration        = ref("12");
    const timeUnit        = ref("months");
    const initialDeposit  = ref("1000");
    const interestRate    = ref("5");
    const monthlyAmount   = ref("750");
    const weeklyAmount    = ref("173");
    const currentProjected = ref(0);

    const toMonths = (d, unit) => {
      const v = parseFloat(d) || 0;
      if (unit === "weeks") return v / 4.33;
      if (unit === "years") return v * 12;
      return v;
    };

    const updateGoalMeterChart = (goal, current) => {
      if (!goalRingRef.value) return;
      if (!goalRingChart) {
        goalRingChart = echarts.init(goalRingRef.value);
        window.addEventListener("resize", () => goalRingChart && goalRingChart.resize());
      }
      const g = Math.max(0, +goal || 0);
      const c = Math.max(0, +current || 0);
      const pct = g > 0 ? Math.min(1, c / g) : 0;

      goalRingChart.setOption({
        title: {
          text: Math.round(pct * 100) + '%',
          left: 'center', top: '40%',
          textStyle: { fontSize: 26, fontWeight: 800, color: '#16a34a' }
        },
        series: [{
          type: 'pie', radius: ['70%','90%'], silent: true, label: { show: false },
          data: [
            { value: pct,   itemStyle: { color: '#16a34a' } },
            { value: 1-pct, itemStyle: { color: '#e5e7eb' } }
          ]
        }]
      });
    };

    const updateStackedGrowthChart = (months, monthly, initial, apr) => {
      if (!stackedChartRef.value) return;
      if (!stackedChart) {
        stackedChart = echarts.init(stackedChartRef.value);
        window.addEventListener("resize", () => stackedChart && stackedChart.resize());
      }

      const m    = Math.max(0, +months || 0);
      const pm   = Math.max(0, +monthly || 0);
      const init = Math.max(0, +initial || 0);
      const r    = Math.max(0, (+apr || 0) / 100 / 12); // 月利率

      const x = [], principal = [], interest = [];
      let balance = init, cumP = init, cumI = 0;

      for (let i = 0; i <= Math.round(m); i++) {
        x.push(i.toString());
        principal.push(cumP);
        interest.push(cumI);

        const gain = balance * r;
        cumI += gain;
        balance += gain + pm;
        cumP += pm;
      }

      stackedChart.setOption({
        tooltip: { trigger: 'axis', valueFormatter: v => '$' + Math.round(v).toLocaleString() },
        legend: { data: ['Principal', 'Interest'] },
        grid: { left: '12%', right: '8%', top: '12%', bottom: '14%' },
        xAxis: { type: 'category', data: x },
        yAxis: {
          type: 'value',
          splitLine: { lineStyle: { color: '#f0f0f0' } },
          axisLabel: { formatter: v => '$' + (v/1000) + 'k' }
        },
        series: [
          { name: 'Principal', type: 'line', stack: 'total', areaStyle: {}, data: principal, itemStyle:{ color:'#93c5fd' } },
          { name: 'Interest',  type: 'line', stack: 'total', areaStyle: {}, data: interest,  itemStyle:{ color:'#16a34a' } }
        ]
      });
    };

    const updateSavingsVisuals = () => {
      const months   = toMonths(duration.value, timeUnit.value);
      const monthly  = +monthlyAmount.value || 0;
      const initial  = +initialDeposit.value || 0;
      const goal     = +savingsGoal.value || 0;
      const apr      = +interestRate.value || 0;

      const projected = initial + months * monthly; // 简化累计值（不含利息），直观对比目标
      currentProjected.value = projected;

      updateGoalMeterChart(goal, projected);
      updateStackedGrowthChart(months, monthly, initial, apr);
    };

    const calculateSavings = () => {
      const goal = parseFloat(savingsGoal.value) || 0;
      const initial = parseFloat(initialDeposit.value) || 0;
      const remaining = Math.max(goal - initial, 0);

      let months = parseFloat(duration.value) || 1;
      if (timeUnit.value === "weeks") months = months / 4.33;
      if (timeUnit.value === "years") months = months * 12;

      const perMonth = remaining / months;
      const perWeek  = remaining / (months * 4.33);

      monthlyAmount.value = Math.round(perMonth).toString();
      weeklyAmount.value  = Math.round(perWeek).toString();

      updateSavingsVisuals();
    };

    /** ===== 挂载 & 监听 ===== */
    onMounted(() => {
      initChart();
      calculateBudget();

      calculateSavings(); // 内部会绘制两个图
    });

    // Savings 任一关键值变化都刷新可视化
    watch(
      () => [savingsGoal.value, duration.value, timeUnit.value, initialDeposit.value, interestRate.value, monthlyAmount.value],
      () => updateSavingsVisuals()
    );

    // 费用输入变化时，自动更新饼图与 Alerts
    watch(() => ({...expenses.value}), () => updateChart(), { deep: true });

    return {
      // 表单
      income, expenses, calculateBudget,
      // flashcards
      activeIndex, nextCard, prevCard,
      // 饼图
      chartRef,
      // alerts
      budgets, alertCards, percentUsed, statusClass, barClass, progressWidth, statusText, statusIcon, formatNumber,
      // savings
      savingsGoal, duration, timeUnit, initialDeposit, interestRate, monthlyAmount, weeklyAmount,
      goalRingRef, stackedChartRef, currentProjected,
      calculateSavings,
    };
  },
};
</script>

<style scoped>
.budget-planner { min-height: 100vh; background: #f8fafc; }
.main-content { padding: 3rem 0; }
.container { max-width: 1400px; margin: 0 auto; padding: 0 2rem; }

/* 顶部布局：左表单 + 右 Flashcards */
.budget-section { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin-bottom: 32px; }

/* 左侧表单卡片 */
.form-section { background: #fff; padding: 20px; border-radius: 12px; box-shadow: 0 1px 3px rgba(0,0,0,.1); }
.income-section, .expenses-section { margin-bottom: 20px; }

.section-header { display: flex; align-items: center; gap: 8px; margin-bottom: 12px; }
.section-icon { width: 12px; height: 12px; border-radius: 50%; }
.section-icon.green { background: #10B981; }
.section-icon.red { background: #EF4444; }
.section-header h3 { font-size: 1.05rem; font-weight: 700; color: #111827; margin: 0; }

.form-group { margin-bottom: 12px; }
.form-group label { display: block; font-size: .875rem; font-weight: 500; color: #374151; margin-bottom: 6px; }
.form-group input { width: 100%; padding: .72rem; border: 1px solid #d1d5db; border-radius: 8px; background: #fff; font-size: .9rem; }
.form-group input:focus { outline: none; border-color: #4F46E5; box-shadow: 0 0 0 3px rgba(79,70,229,.12); }

.calculate-btn { width: 100%; background: #4F46E5; color: #fff; border: 0; padding: .9rem; border-radius: 10px; font-weight: 700; cursor: pointer; }
.calculate-btn:hover { background: #4338CA; }

/* 右：Flashcard 容器 */
.summary-section { display: flex; flex-direction: column; gap: 12px; }
.flashcard { background: #fff; border-radius: 12px; box-shadow: 0 8px 24px rgba(0,0,0,.06); padding: 12px; }
.flashcard-header { display: flex; justify-content: space-between; align-items: center; padding: 4px 6px 10px; border-bottom: 1px solid #f1f5f9; margin-bottom: 8px; }
.flashcard-header h3 { font-size: 1.05rem; font-weight: 800; color: #111827; margin: 0; }
.nav { display: inline-flex; gap: 8px; }
.nav-btn { width: 34px; height: 34px; border-radius: 8px; border: 1px solid #e5e7eb; background: #fff; font-size: 18px; line-height: 1; cursor: pointer; }
.nav-btn:hover { background: #f8fafc; }

.flashcard-body { position: relative; min-height: 380px; }
.flashcard-body .pane { position: absolute; inset: 0; transition: opacity .25s ease; }
.flashcard-body .pane[style*="display: none"] { opacity: 0; pointer-events: none; }

.chart-section { background: #fff; padding: 4px; border-radius: 12px; }
.summary-section .chart-container { height: 380px; min-height: 380px; }

/* Alerts 栅格 */
.alerts-intro .muted { color: #64748b; font-size: .9rem; margin: 4px 0 10px; }
.alerts-grid.compact { display: grid; grid-template-columns: repeat(2,1fr); gap: 10px; }
.alert-card { background: #fff; border-radius: 12px; padding: 12px; box-shadow: 0 1px 3px rgba(0,0,0,.06); border-left: 4px solid; }
.alert-card.warning  { border-left-color: #F59E0B; }
.alert-card.exceeded { border-left-color: #EF4444; }
.alert-card.good     { border-left-color: #10B981; }

.alert-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px; }
.alert-header h4 { font-size: 1rem; font-weight: 700; color: #111827; margin: 0; }
.alert-content { display: flex; flex-direction: column; gap: 8px; }
.alert-row { display: flex; justify-content: space-between; font-size: .875rem; color: #64748b; }

.progress-bar { width: 100%; height: 8px; background: #f1f5f9; border-radius: 4px; overflow: hidden; }
.progress-fill { height: 100%; border-radius: 4px; }
.progress-fill.warning  { background: #F59E0B; }
.progress-fill.exceeded { background: #EF4444; }
.progress-fill.good     { background: #10B981; }

.alert-status { font-size: .85rem; font-weight: 600; }
.alert-card.warning  .alert-status { color: #F59E0B; }
.alert-card.exceeded .alert-status { color: #EF4444; }
.alert-card.good     .alert-status { color: #10B981; }

.alert-row.editable { align-items: center; }
.budget-edit { display: inline-flex; align-items: center; gap: 6px; }
.budget-edit .currency { color: #6b7280; font-size: 0.9rem; }
.budget-input { width: 110px; padding: 6px 10px; border: 1px solid #e5e7eb; border-radius: 8px; font-size: 0.9rem; background: #fff; }
.budget-input:focus { outline: none; border-color: #4F46E5; box-shadow: 0 0 0 3px rgba(79,70,229,.12); }

/* ===== Savings —— 布局打磨：左定宽、右自适应、顶部齐平 ===== */
.savings-calculator-section { margin-top: 24px; }
.calc-header { text-align: center; margin-bottom: 10px; }
.calc-header h2 { font-size: 1.5rem; font-weight: 800; color: #111827; }
.calc-header p  { margin-top: 4px; color: #6b7280; font-size: .92rem; }

.calculator-card { background: #fff; border-radius: 14px; box-shadow: 0 12px 24px rgba(0,0,0,.08); padding: 12px 12px 18px; }

/* 关键：左固定 480px，右自适应；顶部对齐 */
.calculator-container {
  display: grid;
  grid-template-columns: 480px 1fr;
  column-gap: 24px;
  align-items: start;
}

/* 左表单去外 padding，统一由内层控制 */
.calculator-left { padding: 0; }
.savings-calculator-section .calculator-left .form-section {
  padding: 20px;
  border: 1px solid #e5e7eb;
  border-radius: 12px;
  background: #fff;
  box-shadow: none;
}

/* 右侧统一卡片间距 */
.calculator-right { display: flex; flex-direction: column; gap: 12px; padding: 0; }

.savings-plan-card {
  border-radius: 12px;
  border: 1px solid #e5e7eb;
  background: #f9fafb;
  padding: 16px;
  min-height: 160px;
}
.savings-plan-card h3 { font-size: 1rem; font-weight: 700; color: #1f2937; margin-bottom: 10px; }
.plan-box { background: #fff; border: 1px solid #e5e7eb; border-radius: 10px; padding: 12px; }
.plan-amount .currency { color: #16a34a; font-weight: 700; }
.plan-amount .amount { color: #16a34a; font-size: 1.75rem; font-weight: 800; }
.plan-description { margin-top: 4px; color: #6b7280; font-size: .85rem; }
.stat-pills { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 10px; }
.stat-pill { background: #fff; border: 1px solid #e5e7eb; border-radius: 10px; padding: 10px; text-align: center; }
.pill-amount { font-weight: 800; }
.pill-amount.blue { color: #2563eb; }
.pill-amount.purple { color: #7c3aed; }
.pill-label { font-size: .75rem; color: #6b7280; }

/* 可视化双列：左环、右图 */
.viz-grid {
  display: grid;
  grid-template-columns: 320px 1fr;
  gap: 12px;
  margin-top: 6px;
}
.viz-card {
  background: #ffffff;
  border: 1px solid #e5e7eb;
  border-radius: 12px;
  padding: 12px;
  display: flex;
  flex-direction: column;
}
.viz-card h4 { margin: 0 0 8px 0; font-size: .95rem; font-weight: 700; color: #111827; }
.goal-ring { flex: 1; height: 200px; }
.ring-card .ring-caption { margin-top: 6px; display: grid; grid-template-columns: 1fr 1fr; gap: 6px; }
.ring-card .ring-line { display: flex; justify-content: space-between; font-size: .85rem; color: #374151; }
.stacked-chart { flex: 1; min-height: 220px; }

/* 响应式 */
@media (max-width: 1200px) {
  .budget-section { grid-template-columns: 1fr; }
}
@media (max-width: 1024px) {
  .calculator-container { grid-template-columns: 1fr; }
  .viz-grid { grid-template-columns: 1fr; }
  .goal-ring { height: 180px; }
  .stacked-chart { min-height: 200px; }
}
</style>
