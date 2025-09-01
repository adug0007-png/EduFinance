<template>
  <section class="cta">
    <div class="container cta-container">
      <h2 class="section-title">Start Your Financial Education Journey Today</h2>
      <p class="section-subtitle">Join thousands of students who are taking control of their financial future. Begin with our free tools and resources.</p>
      <div class="cta-buttons">
        <button class="btn btn-primary" @click="navigateTo('mortgage-calculator')">Get Started Free</button>
        <button class="btn btn-secondary" @click="navigateTo('mortgage-calculator')">View Demo</button>
      </div>
    </div>
  </section>
</template>

<script setup>
import { inject } from 'vue'

const navigateTo = inject('navigateTo')
</script>

<style scoped>
.cta {
  padding: 80px 0;
}

.cta-container {
  text-align: center;
  max-width: 800px;
  margin: 0 auto;
}

.section-title {
  font-size: 36px;
  font-weight: 700;
  margin: 0 0 16px;
  white-space: nowrap;
}

.section-subtitle {
  font-size: 18px;
  color: var(--muted-text-color);
  margin: 0 0 32px;
}

.cta-buttons {
  display: flex;
  justify-content: center;
  gap: 16px;
}

.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  height: 48px;
  padding: 0 28px;
  border-radius: 8px;
  font-weight: 600;
  font-size: 16px;
  transition: all 0.2s ease;
  cursor: pointer;
}

.btn-primary {
  background-color: var(--primary-color);
  color: white;
  border: none;
}

.btn-primary:hover {
  transform: translateY(-1px);
  box-shadow: 0 6px 16px rgba(79, 70, 229, 0.25);
}

.btn-secondary {
  background-color: white;
  color: var(--text-color);
  border: 1px solid var(--border-color);
}

.btn-secondary:hover {
  transform: translateY(-1px);
  border-color: #D1D5DB;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
}

@media (max-width: 576px) {
  .cta-buttons {
    flex-direction: column;
    align-items: stretch;
  }
}
</style>