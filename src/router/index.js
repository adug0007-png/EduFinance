import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import MortgageCalculator from '../components/MortgageCalculator.vue'
import BudgetPlanner from '../components/BudgetPlanner.vue'
import SavingsGoalCalculator from '../components/SavingsGoalCalculator.vue'
import FinancialLiteracy from '../views/FinancialLiteracy.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/mortgage-calculator',
    name: 'MortgageCalculator',
    component: MortgageCalculator
  },
  {
    path: '/budget-planner',
    name: 'BudgetPlanner',
    component: BudgetPlanner
  },
  {
    path: '/savings-goal-calculator',
    name: 'SavingsGoalCalculator',
    component: SavingsGoalCalculator
  },
  { 
    path: '/financial-literacy', 
    name: 'FinancialLiteracy', 
    component: FinancialLiteracy 
  }

]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router