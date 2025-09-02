<template>
  <section class="hero-ww">
    <!-- 背景图 -->
    <div class="hero-bg">
      <img src="../assets/home.jpg" alt="" />
      <div class="overlay"></div>
    </div>

    <!-- 内容叠加 -->
    <div class="hero-content">
      <h1 class="hero-title a-fade-up a-delay-0">Grow your wealth</h1>
      <p class="hero-subtitle a-fade-up a-delay-1">
        Plan smarter, save faster, and build lasting financial confidence with WealthWave.
      </p>
      <button class="btn-primary a-fade-up a-delay-2"
              @click="navigateTo('savings-goal-calculator')">
        Get Started
      </button>
    </div>
  </section>
</template>

<script setup>
import { inject } from 'vue'
const navigateTo = inject('navigateTo')
</script>

<style scoped>
/* ===== Base layout ===== */
.hero-ww {
  position: relative;
  width: 100%;
  height: clamp(420px, 80vh, 680px);
  overflow: hidden;
}

.hero-bg { position: absolute; inset: 0; }
.hero-bg img { width: 100%; height: 100%; object-fit: cover; }

.hero-bg .overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(
    to bottom,
    rgba(0,0,0,.25) 0%,
    rgba(0,0,0,.35) 40%,
    rgba(0,0,0,.55) 100%
  );
}

/* 底部渐变过渡到白色 */
.hero-bg .overlay::after {
  content: "";
  position: absolute;
  bottom: 0; left: 0; right: 0;
  height: 90px; /* 可调 60-120px */
  background: linear-gradient(to bottom, transparent, #fff);
}

/* 内容居中叠加 */
.hero-content {
  position: relative; z-index: 2;
  height: 100%;
  display: flex; flex-direction: column;
  align-items: center; justify-content: center;
  text-align: center; color: #fff; padding: 0 16px;
}

.hero-title {
  font-weight: 800;
  font-size: clamp(42px, 8vw, 92px);
  line-height: 1.05;
  margin-bottom: 16px;
  text-shadow: 0 4px 12px rgba(0,0,0,.45);
}

.hero-subtitle {
  font-size: clamp(16px, 2vw, 20px);
  max-width: 720px;
  margin: 0 auto 32px;
  line-height: 1.6;
  color: #e5e7eb;
  text-shadow: 0 2px 8px rgba(0,0,0,.4);
}

/* 按钮 */
.btn-primary {
  padding: 14px 28px;
  border-radius: 12px;
  background: linear-gradient(90deg, #4f46e5, #6366f1);
  color: #fff;
  font-weight: 700;
  font-size: 16px;
  border: none;
  cursor: pointer;
  box-shadow: 0 8px 24px rgba(0,0,0,.35);
  transition: transform .2s ease, box-shadow .2s ease;
}
.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 12px 30px rgba(0,0,0,.45);
}

/* ===== Animations ===== */
@keyframes fadeUp {
  from { opacity: 0; transform: translateY(16px) scale(.98); filter: blur(2px); }
  to   { opacity: 1; transform: translateY(0) scale(1);      filter: blur(0); }
}

.a-fade-up {
  opacity: 0; animation: fadeUp .6s cubic-bezier(.22,.9,.26,1) forwards;
}
.a-delay-0 { animation-delay: .05s; }
.a-delay-1 { animation-delay: .18s; }
.a-delay-2 { animation-delay: .32s; }

@media (prefers-reduced-motion: reduce) {
  .a-fade-up { animation: none; opacity: 1; transform: none; filter: none; }
}
</style>
