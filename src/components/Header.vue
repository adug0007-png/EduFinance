<template>
  <header class="header">
    <div class="container">
      <nav class="navbar">
        <div class="logo" @click="navigateTo('home')" style="cursor: pointer;">
          <svg class="logo-mark" viewBox="0 0 24 24" aria-hidden="true">
            <path fill="var(--primary-color)" d="M12 3l9 4-9 4-9-4 9-4Z"/>
            <path fill="#A5B4FC" d="M6 10v4c0 1.1.9 2 2 2h8c1.1 0 2-.9 2-2v-4l-6 3-6-3Z"/>
          </svg>
          <span class="logo-text">EduFinance</span>
        </div>
        <ul class="nav-links">
          <li><a href="#" @click.prevent="navigateTo('mortgage-calculator')">Calculator</a></li>
          <li><a href="#" @click.prevent="navigateTo('budget-planner')">Budget</a></li>
          <li><a href="#" @click.prevent="navigateTo('financial-literacy')">Financial</a></li>
          <li><a href="#" @click.prevent="navigateTo('cost-estimator')">Cost Estimator</a></li>
          <li><a href="#" @click.prevent="navigateTo('tax-learn')">TaxLearn</a></li>
          <li><a href="#" @click.prevent="navigateTo('mortgage-calculator')" class="btn btn-primary">Get Started</a></li>
        </ul>
      </nav>
    </div>
  </header>
</template>

<script setup>
import { inject } from 'vue'

const navigateTo = inject('navigateTo')
const currentRoute = inject('currentRoute')
</script>

<style scoped>
.header {
  position: sticky;
  top: 0;
  z-index: 40;
  background: rgba(255, 255, 255, 0.85);
  backdrop-filter: saturate(180%) blur(10px);
  border-bottom: 1px solid var(--border-color);
}

.navbar {
  height: 72px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.logo {
  display: flex;
  align-items: center;
  gap: 8px;
}

.logo-mark {
  width: 24px;
  height: 24px;
}

.logo-text {
  font-weight: 700;
  font-size: 18px;
  letter-spacing: -0.02em;
  color: var(--text-color);
}

.nav-links {
  display: flex;
  align-items: center;
  gap: 32px;
  list-style: none;
  margin: 0;
  padding: 0;
}

/* 仅对非按钮链接应用默认文字色，避免覆盖按钮白字 */
.nav-links a:not(.btn) {
  color: var(--text-color);
  text-decoration: none;
  font-weight: 600;
  font-size: 15px;
  transition: color 0.2s ease;
}

.nav-links a:not(.btn):hover {
  color: var(--primary-color);
}

.nav-links a.active {
  color: var(--primary-color);
  position: relative;
}

.nav-links a.active:after {
  content: '';
  position: absolute;
  bottom: -8px;
  left: 0;
  right: 0;
  height: 2px;
  background: var(--primary-color);
  border-radius: 1px;
}

.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  height: 40px;
  padding: 0 20px;
  border-radius: 8px;
  font-weight: 600;
  font-size: 15px;
  transition: all 0.2s ease;
  border: none;
  cursor: pointer;
  text-decoration: none; /* remove underline for <a class=btn> */
}

.btn-primary {
  background-color: var(--primary-color);
  color: white;
}

.btn-primary:hover {
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(79, 70, 229, 0.2);
}

@media (max-width: 768px) {
  .nav-links li:not(:last-child) {
    display: none;
  }
}
</style>