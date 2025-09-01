<script setup>
import { ref, provide, onMounted } from 'vue'
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

// Simple routing state
const currentRoute = ref('home')

// Navigation function
const navigateTo = (route) => {
  currentRoute.value = route
  window.location.hash = route === 'home' ? '' : `#${route}`
}

// Handle URL hash changes
const handleHashChange = () => {
  const hash = window.location.hash.slice(1) // Remove the '#'
  currentRoute.value = hash || 'home'
}

// Initialize route from URL on mount
onMounted(() => {
  handleHashChange()
  window.addEventListener('hashchange', handleHashChange)
})

// Provide navigation function to child components
provide('navigateTo', navigateTo)
provide('currentRoute', currentRoute)
</script>

<template>
  <!-- Global Header across all pages -->
  <Header />
  
  <!-- Calculator Header for mortgage calculator page -->
  <div v-if="currentRoute === 'mortgage-calculator'" class="calculator-page-header">
    <div class="header-content">
      <div class="header-icon" aria-hidden="true">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M3 9L12 2L21 9V20C21 20.5304 20.7893 21.0391 20.4142 21.4142C20.0391 21.7893 19.5304 22 19 22H5C4.46957 22 3.96086 21.7893 3.58579 21.4142C3.21071 21.0391 3 20.5304 3 20V9Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="M9 22V12H15V22" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </div>
      <div class="header-text">
        <h1 class="page-title">Home Mortgage Calculator</h1>
        <p class="page-subtitle">Simple and accurate mortgage calculations</p>
      </div>
    </div>
  </div>

  
  <!-- Home Page -->
  <main v-if="currentRoute === 'home'">
    <Hero />
    <Features />
    <CTA />
  </main>
  
  <!-- Mortgage Calculator Page -->
  <MortgageCalculator v-else-if="currentRoute === 'mortgage-calculator'" />
  
  <!-- Budget Planner Page -->
  <BudgetPlanner v-else-if="currentRoute === 'budget-planner'" />
  
  <!-- Savings Goal Calculator Page -->
  <SavingsGoalCalculator v-else-if="currentRoute === 'savings-goal-calculator'" />
  
  <!-- Financial Literacy Page -->
  <FinancialLiteracy v-else-if="currentRoute === 'financial-literacy'" />
  
  <!-- Cost Estimator Page -->
  <CostEstimator v-else-if="currentRoute === 'cost-estimator'" />
  
  <!-- TaxLearn Page -->
  <TaxLearn v-else-if="currentRoute === 'tax-learn'" />
  
  <Footer v-if="currentRoute === 'home'" />
</template>

<style scoped>
.calculator-page-header {
  background: #ffffff;
  color: #111827;
  padding: 20px 0;
  border-bottom: 1px solid #e5e7eb;
}

.header-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 24px;
  display: flex;
  align-items: center;
  gap: 12px;
}

.header-icon {
  width: 28px;
  height: 28px;
  color: #4f46e5;
  display: flex;
  align-items: center;
  justify-content: center;
}

.header-text { text-align: left; }

.page-title {
  font-size: 24px;
  font-weight: 700;
  margin: 0;
  line-height: 1.2;
}

.page-subtitle {
  font-size: 16px;
  margin: 4px 0 0 0;
  color: #6b7280;
  line-height: 1.4;
}

@media (max-width: 640px) {
  .page-title { font-size: 22px; }
  .page-subtitle { font-size: 14px; }
}
</style>
