<script setup>
import { ref, provide, onMounted, computed } from 'vue'
import Header from './components/Header.vue'
import Hero from './components/Hero.vue'
import Features from './components/Features.vue'
import CTA from './components/CTA.vue'
import Footer from './components/Footer.vue'

import MortgageCalculator from './components/MortgageCalculator.vue'
import BudgetPlanner from './components/BudgetPlanner.vue'
import SavingsGoalCalculator from './components/SavingsGoalCalculator.vue'
import FinancialLiteracy from './components/FinancialLiteracy.vue'
import CostEstimator from './components/CostEstimator.vue'
import TaxLearn from './components/TaxLearn.vue'

// 统一页头组件（主标题+次标题）
import PageHeader from './components/PageHeader.vue'

// 简易路由
const currentRoute = ref('home')

// 路由导航
const navigateTo = (route) => {
  currentRoute.value = route
  window.location.hash = route === 'home' ? '' : `#${route}`
}

// 处理 URL hash
const handleHashChange = () => {
  const hash = window.location.hash.slice(1)
  currentRoute.value = hash || 'home'
}

// 初始化
onMounted(() => {
  handleHashChange()
  window.addEventListener('hashchange', handleHashChange)
})

// 对外提供
provide('navigateTo', navigateTo)
provide('currentRoute', currentRoute)

// 各页面的统一标题与副标题（可在此集中修改）
const headers = {
  'mortgage-calculator': {
    title: 'Home Mortgage Calculator',
    subtitle: 'Calculate repayments easily with accurate and clear mortgage estimates.',
    // 可选：页面图标（示例保留你原来的房子图标）
    icon: 'mortgage'
  },
  'budget-planner': {
    title: 'Personal Budget Planner',
    subtitle: 'Manage income, expenses, and savings with smart financial balance tracking.'
  },
  'savings-goal-calculator': {
    title: 'Savings Goal Calculator',
    subtitle: 'Set a target amount and date, then track the contributions you need to stay on course.'
  },
  'financial-literacy': {
    title: 'Financial Literacy Hub',
    subtitle: 'Learn practical money skills with interactive modules designed to boost your confidence and financial knowledge.'
  },
  'cost-estimator': {
    title: 'Education Cost Estimator',
    subtitle: 'Get clear insights into tuition, living, and study costs tailored to your goals.'
  },
  'tax-learn': {
    title: 'Learn Tax & Super',
    subtitle: 'Understand Australian taxation and superannuation with interactive flashcards and calculators.'
  }
}

// 当前页头信息
const activeHeader = computed(() => headers[currentRoute.value] || null)
</script>

<template>
  <!-- 全站导航 -->
  <Header />

  <!-- 非首页：用统一页头 -->
  <PageHeader
    v-if="currentRoute !== 'home' && activeHeader"
    :title="activeHeader.title"
    :subtitle="activeHeader.subtitle"
  >
    <!-- 可选：在页头左侧插入图标（目前为 Mortgage 的小房子） -->
    <template #default>
      <div v-if="activeHeader.icon === 'mortgage'" aria-hidden="true" style="display:inline-flex;align-items:center;margin-right:.5rem;">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none"
             xmlns="http://www.w3.org/2000/svg">
          <path d="M3 9L12 2L21 9V20C21 20.5304 20.7893 21.0391 20.4142 21.4142C20.0391 21.7893 19.5304 22 19 22H5C4.46957 22 3.96086 21.7893 3.58579 21.4142C3.21071 21.0391 3 20.5304 3 20V9Z"
                stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="M9 22V12H15V22" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </div>
    </template>
  </PageHeader>

  <!-- 首页 -->
  <main v-if="currentRoute === 'home'">
    <Hero />
    <Features />
    <CTA />
  </main>

  <!-- 各页面主体 -->
  <MortgageCalculator v-else-if="currentRoute === 'mortgage-calculator'" />
  <BudgetPlanner v-else-if="currentRoute === 'budget-planner'" />
  <SavingsGoalCalculator v-else-if="currentRoute === 'savings-goal-calculator'" />
  <FinancialLiteracy v-else-if="currentRoute === 'financial-literacy'" />
  <CostEstimator v-else-if="currentRoute === 'cost-estimator'" />
  <TaxLearn v-else-if="currentRoute === 'tax-learn'" />


  <!-- 首页 Footer -->
  <Footer v-if="currentRoute === 'home'" />
</template>

