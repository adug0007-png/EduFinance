<script setup>
import { ref, provide, onMounted, computed } from 'vue'
import Header from './components/Header.vue'
import Hero from './components/Hero.vue'
import Footer from './components/Footer.vue'

import MortgageCalculator from './components/MortgageCalculator.vue'
import BudgetPlanner from './components/BudgetPlanner.vue'
import SavingsGoalCalculator from './components/SavingsGoalCalculator.vue'
import FinancialLiteracy from './components/FinancialLiteracy.vue'
import CostEstimator from './components/CostEstimator.vue'
import TaxLearn from './components/TaxLearn.vue'

import PageHeader from './components/PageHeader.vue'

// Simple hash routing
const currentRoute = ref('home')
const navigateTo = (route) => {
  currentRoute.value = route
  window.location.hash = route === 'home' ? '' : `#${route}`
}
const handleHashChange = () => {
  const hash = window.location.hash.slice(1)
  currentRoute.value = hash || 'home'
}
onMounted(() => {
  handleHashChange()
  window.addEventListener('hashchange', handleHashChange)
})
provide('navigateTo', navigateTo)
provide('currentRoute', currentRoute)

// Centralized titles/subtitles for non-home pages
const headers = {
  'mortgage-calculator': {
    title: 'Home Mortgage Calculator',
    subtitle: 'Calculate repayments easily with accurate and clear mortgage estimates.',
    icon: 'mortgage',
  },
  'budget-planner': {
    title: 'Personal Budget Planner',
    subtitle: 'Manage income, expenses, and savings with smart financial balance tracking.',
  },
  'savings-goal-calculator': {
    title: 'Savings Goal Calculator',
    subtitle: 'Set a target amount and date, then track the contributions you need to stay on course.',
  },
  'financial-literacy': {
    title: 'Financial Literacy Hub',
    subtitle: 'Learn practical money skills with curated videos on budgeting, saving, and tax.',
  },
  'cost-estimator': {
    title: 'Education Cost Estimator',
    subtitle: 'Get clear insights into tuition, living, and study costs tailored to your goals.',
  },
  'tax-learn': {
    title: 'Financial Concepts',
    subtitle: 'Understand Australian taxation and superannuation with with flashcards of key terms and a take-home pay calculator.',
  },
}
const activeHeader = computed(() => headers[currentRoute.value] || null)
</script>

<template>
  <!-- Global site header (sticky) -->
  <Header />

  <!-- Page header on every page except Home -->
  <PageHeader
    v-if="currentRoute !== 'home' && activeHeader"
    :title="activeHeader.title"
    :subtitle="activeHeader.subtitle"
    :dark="currentRoute !== 'home'"
  >
    <!-- Optional icon (only for mortgage example) -->
    <template #default>
      <div
        v-if="activeHeader.icon === 'mortgage'"
        aria-hidden="true"
        style="display:inline-flex;align-items:center;margin-right:.5rem;"
      >
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
          <path d="M3 9L12 2L21 9V20c0 .53-.21 1.04-.59 1.41S19.53 22 19 22H5c-.53 0-1.04-.21-1.41-.59S3 20.53 3 20V9Z"
                stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="M9 22V12h6v10" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </div>
    </template>
  </PageHeader>

  <!-- Home page (leave exactly as-is: only Hero) -->
  <main v-if="currentRoute === 'home'">
    <Hero />
  </main>

  <!-- Other pages -->
  <MortgageCalculator v-else-if="currentRoute === 'mortgage-calculator'" />
  <BudgetPlanner v-else-if="currentRoute === 'budget-planner'" />
  <SavingsGoalCalculator v-else-if="currentRoute === 'savings-goal-calculator'" />
  <FinancialLiteracy v-else-if="currentRoute === 'financial-literacy'" />
  <CostEstimator v-else-if="currentRoute === 'cost-estimator'" />
  <TaxLearn v-else-if="currentRoute === 'tax-learn'" />

  <!-- Footer only on Home (as before) -->
  <Footer v-if="currentRoute === 'home'" />
</template>
