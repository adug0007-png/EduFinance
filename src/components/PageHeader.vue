<!-- src/components/PageHeader.vue -->
<template>
  <header class="ww-header" :class="[align, dark ? 'dark' : 'light']">
    <div class="header-inner">
      <div v-if="$slots.default" class="header-icon"></div>

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
  titleTag: { type: String, default: 'h1' },
  dark: { type: Boolean, default: false }     // kept for compatibility
})
</script>

<style scoped>
/* Keep nav ribbon visually unchanged; this header adds minimal spacing only */
.ww-header {
  background: transparent;
  border: none;
  margin-top: 0;
  padding: 12px 0 16px;  /* small breathing room below sticky nav */
}

.header-inner {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 24px;
  display: flex;
  align-items: center;
  gap: 12px;
}

/* alignment */
.ww-header.center .header-text { text-align: center; margin: 0 auto; }
.ww-header.left   .header-text { text-align: left; }

/* Use THEME TOKENS so colors flip with .non-home-dark and system dark mode */
.header-text :deep(h1),
.header-text :deep(h2),
.header-text :deep(h3) {
  color: var(--text-primary);
}
.header-text :deep(p) {
  color: var(--text-secondary);
}

/* optional icon slot */
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
