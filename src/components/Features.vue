        <!-- 3 Cards -->
<template>
  <section class="features">
    <div class="container">
      <div class="features-header">
        <h2 class="section-title">Everything You Need to Succeed</h2>
        <p class="section-subtitle">Comprehensive tools and resources designed to help students make informed financial decisions about their education.</p>
      </div>
      <div class="features-grid">
        <!-- Card 1 -->
        <article class="feature-card" @click="navigateTo('cost-estimator')" style="cursor:pointer;">
          <div class="card-icon-badge icon-blue">
            <img src="../assets/icon-calculator.svg" alt="Calculator icon" />
          </div>
          <div class="card-media" aria-hidden="true">
            <img src="../assets/caculator.png" alt="Cost Estimator illustration" />
          </div>
          <h3 class="card-title">Cost Estimator</h3>
          <p class="card-description">Get accurate estimates for tuition, living expenses, and total education costs. Plan your budget with confidence using our comprehensive calculation tools.</p>
        </article>

        <!-- Card 2 -->
        <article class="feature-card" @click="navigateTo('financial-literacy')" style="cursor:pointer;">
          <div class="card-icon-badge icon-green">
            <img src="../assets/icon-book.svg" alt="Learning icon" />
          </div>
          <div class="card-media" aria-hidden="true">
            <img src="../assets/Learning.png" alt="Learning Modules illustration" />
          </div>
          <h3 class="card-title">Learning Modules</h3>
          <p class="card-description">Interactive lessons covering budgeting, saving, investing, and debt management. Build essential financial skills through engaging, bite-sized modules.</p>
        </article>

        <!-- Card 3 -->
        <article class="feature-card">
          <div class="card-icon-badge icon-purple">
            <img src="../assets/icon-users.svg" alt="Sharing icon" />
          </div>
          <div class="card-media" aria-hidden="true">
            <img src="../assets/sharing.png" alt="Sharing Hub illustration" />
          </div>
          <h3 class="card-title">Sharing Hub</h3>
          <p class="card-description">Connect with peers, share experiences, and learn from others' financial journeys. Join a supportive community of students building financial literacy together.</p>
        </article>
      </div>
    </div>
  </section>
</template>

<script setup>
import { inject } from 'vue'

// 从 App.vue 拿到 navigateTo
const navigateTo = inject('navigateTo')
</script>

<style scoped>
.features { padding: 88px 0; background: var(--surface-color); margin-top: 72px; }



.features-header { text-align: center; max-width: 720px; margin: 0 auto 48px; }
.section-title { font-size: 34px; font-weight: 800; margin: 0 0 10px; letter-spacing: -0.01em; }
.section-subtitle { font-size: 18px; color: var(--muted-text-color); }

.features-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 28px; }

.feature-card {
  background: #fff;
  border: 1px solid var(--border-color);
  border-radius: 16px;
  box-shadow: var(--shadow-sm, 0 4px 12px rgba(0,0,0,.04));
  padding: 24px;
  display: flex;
  flex-direction: column;
  align-items: stretch;
  gap: 14px;
  transition: transform .2s ease, box-shadow .2s ease;
}
.feature-card:hover { transform: translateY(-4px); box-shadow: var(--shadow-md, 0 12px 24px rgba(0,0,0,.08)); }

.feature-card {
  cursor: pointer;
}

.card-icon-badge { width: 52px; height: 52px; border-radius: 14px; display: inline-flex; align-items: center; justify-content: center; }
.card-icon-badge img { width: 32px; height: 32px; display: block; }
.icon-blue { background: #EEF2FF; box-shadow: inset 0 0 0 1px #C7D2FE; }
.icon-green { background: #ECFDF5; box-shadow: inset 0 0 0 1px #BBF7D0; }
.icon-purple { background: #F5F3FF; box-shadow: inset 0 0 0 1px #E9D5FF; }

.card-title { font-size: 20px; font-weight: 700; margin: 2px 0 0; }
.card-description { color: var(--muted-text-color); line-height: 1.6; }

.card-media { overflow: hidden; border-radius: 12px; }
.card-media img { width: 100%; height: 180px; object-fit: cover; display: block; }

@media (max-width: 1200px) { .features-grid { grid-template-columns: 1fr; } }
@media (max-width: 992px) { .features { margin-top: 40px; } }


@media (max-width: 768px) {
  .card-media img { height: 200px; }
}
</style>