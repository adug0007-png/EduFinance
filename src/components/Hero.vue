<template>
  <section class="hero" aria-labelledby="hero-title">
    <div class="container">
      <div class="hero-content-box">
        <div class="hero-content">
          <h1 id="hero-title" class="hero-title">Know your costs <br>Budget, save, understand tax</h1>
          <p class="hero-subtitle">
            Master the basics and crunch your costs—budget, save, and understand tax—so your budget is real, trackable, and doable
          </p>
          <div class="hero-buttons">
            <button class="btn btn-primary" @click="navigateTo('tax-learn')">
              Explore Financial Concepts
            </button>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { inject } from 'vue'
const navigateTo = inject('navigateTo')
</script>

<style scoped>
.hero {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: flex-start;
  min-height: 100vh;
}

/* Background image stays untouched */
.hero::before {
  content: '';
  position: absolute;
  inset: 0;
  background-image: url("/hero-bg-light.png");
  background-repeat: no-repeat;
  background-position: right center;
  background-size: cover;
  opacity: 1;
  z-index: -1;
}

/* Swap to dark image based on OS preference (keeps your original behavior) */
@media (prefers-color-scheme: dark) {
  .hero::before {
    background-image: url('/hero-bg-dark.png');
  }
}

.hero .container {
  position: relative;
  z-index: 1;
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 40px;
}

/* The content box: semi-transparent, blur, shadow */
.hero-content-box {
  background: rgba(0,0,0, 0.001); /* was empty — now a subtle dark glass */
  backdrop-filter: blur(8px);
  border-radius: 12px;
  padding: 30px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
  max-width: 600px;
}

/* Force white text INSIDE the box (without touching the page background/image) */
.hero-content,
.hero-content h1,
.hero-content p {
  color: var(--text-primary) !important;
}

.hero-title {
  font-size: clamp(38px, 6vw, 52px);
  font-weight: 800;
  line-height: 1.1;
  letter-spacing: -0.025em;
  margin: 0 0 16px;
}

.hero-subtitle {
  font-size: clamp(1.05rem, 2vw, 1.35rem);
  line-height: 1.6;
  margin: 0 0 20px;
  max-width: 60ch;
}

.hero-buttons {
  display: flex;
  flex-wrap: wrap;
  gap: 14px 16px;
}

.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  height: 48px;
  padding: 0 28px;
  border-radius: 10px;
  font-weight: 600;
  font-size: 16px;
  transition: all .2s ease;
  cursor: pointer;
  text-decoration: none;
}

.btn-primary {
  background: #4F46E5;
  color: #fff;
  border: none;
}

.btn-primary:hover {
  transform: translateY(-1px);
  box-shadow: 0 8px 20px rgba(79,70,229,.25);
}

/* ------------------ Responsive ------------------ */

@media (min-width: 1200px) {
  .hero-content-box { margin-left: -100px; }
}

@media (max-width: 1100px) {
  .hero::before { background-position: right 20%; }
}

@media (max-width: 768px) {
  .hero {
    min-height: 80vh;
    padding: 100px 20px 40px;
    align-items: flex-end;
  }
  .hero::before {
    background-position: center top;
    background-size: 100% 100%;
  }
  .hero-content-box {
    max-width: 100%;
    text-align: center;
  }
  .hero-title, .hero-subtitle { text-align: center; }
  .hero-buttons { justify-content: center; }
}
</style>
