<!-- src/components/PageHeader.vue -->
<template>
  <header class="ww-header" :class="align">
    <div class="header-inner">
      <!-- 可选图标插槽：你在 App.vue 里已经放了小房子图标 -->
      <div v-if="$slots.default" class="header-icon">
      </div>

      <div class="header-text">
        <Typography :variant="'main'" :tag="titleTag">
          {{ title }}
        </Typography>
        <Typography v-if="subtitle" variant="subtitle" tag="p">
          {{ subtitle }}
        </Typography>
      </div>
    </div>
  </header>
</template>

<script setup>
import Typography from './Typography.vue'

const props = defineProps({
  title: { type: String, required: true },
  subtitle: { type: String, default: '' },
  align: { type: String, default: 'center' }, // 'center' | 'left'
  titleTag: { type: String, default: 'h1' }   // 'h1' | 'h2' ...
})
</script>

<style scoped>
.ww-header {
  background: #ffffff;
  color: #111827;
  border-bottom: 1px solid #e5e7eb;
  padding: 20px 0;
}

.header-inner {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 24px;
  display: flex;
  align-items: center;
  gap: 12px;
}

/* 左右/居中对齐策略 */
.ww-header.center .header-text { text-align: center; margin: 0 auto; }
.ww-header.left .header-text { text-align: left; }

/* 图标外观（颜色和尺寸与你现有风格一致） */
.header-icon {
  width: 28px;
  height: 28px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #4f46e5;
}

@media (max-width: 640px) {
  .header-inner { gap: 10px; }
}
</style>
