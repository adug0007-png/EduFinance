<template>
  <section class="hero">
    <div class="container">
      <div class="hero-grid">
        <!-- 左侧卡片：标题、文案与按钮 -->
        <div class="hero-card">
          <h1 class="hero-title">Plan Your Education Journey & Learn...</h1>
          <p class="hero-subtitle">Master financial literacy while planning your educational future. Get personalized cost estimates and learn essential money management skills for life.</p>
          <div class="hero-buttons">
            <button class="btn btn-primary">Get Started</button>
            <button class="btn btn-secondary">Learn Basics</button>
          </div>
        </div>
        <!-- 右侧图片：不在卡片内 -->
        <div class="hero-image-wrapper" aria-hidden="true">
          <img src="../assets/hero-illustration.svg" alt="Education planning illustration" class="hero-image" />
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
</script>

<style scoped>
.hero { padding: 88px 0; }

/* 新版：两列布局，仅左侧为卡片 */
.hero-grid {
  display: grid;
  grid-template-columns: 1.15fr 1fr;
  align-items: stretch;
  gap: 40px;
}

.hero-card {
  background: #fff;
  border: 1px solid var(--border-color);
  /* 顶部边线更淡，底部阴影更重 */
  border-top-color: rgba(229, 231, 235, 0.45);
  border-left-color: rgba(229, 231, 235, 0.85);
  border-right-color: rgba(229, 231, 235, 0.85);
  border-bottom-color: rgba(229, 231, 235, 1);
  border-radius: var(--radius-xl, 20px);
  /* 底部偏重的阴影效果 */
  box-shadow: 0 22px 36px -12px rgba(0,0,0,0.14), 0 4px 10px rgba(0,0,0,0.04);
  padding: 40px;
  height: 100%;
}

.hero-title {
  font-size: 52px;
  font-weight: 800;
  line-height: 1.1;
  letter-spacing: -0.025em;
  margin: 0 0 20px;
}

.hero-subtitle {
  font-size: 18px;
  color: var(--muted-text-color);
  margin: 0 0 28px;
}

.hero-buttons { display: flex; gap: 16px; }

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
}

/* 主按钮：实心紫底白字（Get Started 白字） */
.btn-primary { background: var(--primary-color); color: #fff; border: none; }
.btn-primary:hover { transform: translateY(-1px); box-shadow: 0 8px 20px rgba(79,70,229,.25); }

/* 次按钮：蓝色描边 + 蓝色文字 */
.btn-secondary { background: #fff; color: var(--primary-color); border: 1px solid var(--primary-color); }
.btn-secondary:hover { transform: translateY(-1px); background: rgba(79,70,229,0.06); box-shadow: 0 6px 16px rgba(0,0,0,.06); }

/* 右侧图片独立展示，不包裹在卡片中：纯 CSS 等高 */
.hero-image-wrapper { display: flex; justify-content: center; align-items: center; align-self: stretch; }
.hero-image {
  width: 100%;
  height: 100%;
  min-height: 300px;
  object-fit: cover;
  border-radius: 16px;
  box-shadow: 0 20px 40px rgba(0,0,0,.10);
}

@media (max-width: 992px) {
  .hero { padding: 72px 0; }
  .hero-grid { grid-template-columns: 1fr; gap: 28px; }
  .hero-title { font-size: 42px; }
  .hero-buttons { justify-content: center; }
  .hero-card { height: auto; }
  .hero-image-wrapper { height: auto; }
  .hero-image { height: 300px; min-height: 0; }
}

@media (max-width: 576px) {
  .btn { width: 100%; }
  .hero-buttons { flex-direction: column; }
}
</style>