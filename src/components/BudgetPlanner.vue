<template>
  <div class="budget-planner">
    <div class="main-content">
      <div class="container">
        <!-- Top: left form + right flashcards -->
        <div class="budget-section">
          <!-- Left: Budget form -->
          <div class="form-section">
            <!-- Income -->
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

            <!-- Expenses -->
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

          <!-- Right: Flashcards (Pie chart <-> Alerts) -->
          <div class="summary-section">
            <div class="flashcard">
              <div class="flashcard-header">
                <h3>{{ activeIndex === 0 ? 'Expense Distribution' : 'Overspending Alerts' }}</h3>
                <div class="nav">
                  <button class="nav-btn" @click="prevCard" aria-label="Previous">‹</button>
                  <button class="nav-btn" @click="nextCard" aria-label="Next">›</button>
                </div>
              </div>

              <div class="flashcard-body">
                <!-- Card 1: Expense distribution -->
                <div v-show="activeIndex === 0" class="pane">
                  <div class="chart-section">
                    <div ref="chartRef" class="chart-container"></div>
                  </div>
                </div>

                <!-- Card 2: Overspending Alerts -->
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
        <!-- (Savings section removed) -->
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
    // ===== Left form =====
    const income = ref({ salary: "5800", investments: "0", other: "0" });
    const expenses = ref({
      housing: "1800",
      transportation: "650",
      food: "400",
      entertainment: "200",
      healthcare: "150",
    });

    // ===== Flashcards index =====
    const activeIndex = ref(0);
    const nextCard = () => (activeIndex.value = (activeIndex.value + 1) % 2);
    const prevCard = () => (activeIndex.value = (activeIndex.value + 1) % 2);

    // ===== Pie chart =====
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

    // ===== Alerts =====
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

    // ===== Mount & watchers =====
    onMounted(() => {
      initChart();
      calculateBudget();
    });

    // Update pie chart/alerts when expenses change
    watch(() => ({...expenses.value}), () => updateChart(), { deep: true });

    return {
      income, expenses, calculateBudget,
      activeIndex, nextCard, prevCard,
      chartRef,
      budgets, alertCards, percentUsed, statusClass, barClass, progressWidth, statusText, statusIcon, formatNumber,
    };
  },
};
</script>

<style scoped>
.budget-planner { min-height: 100vh; background: #f8fafc; }
.main-content { padding: 3rem 0; }
.container { max-width: 1400px; margin: 0 auto; padding: 0 2rem; }

/* top layout: left form + right flashcards */
.budget-section { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin-bottom: 32px; }

/* left card */
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

/* right flashcard */
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

/* Alerts grid */
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

/* responsive */
@media (max-width: 1200px) {
  .budget-section { grid-template-columns: 1fr; }
}
</style>
