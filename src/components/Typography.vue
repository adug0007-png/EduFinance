<template>
  <component :is="tag" :class="classes">
    <slot />
  </component>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  variant: {
    type: String,
    default: 'subtitle' // 'main' | 'subtitle'
  },
  tag: {
    type: String,
    default: 'p' // h1 for main, p for subtitle (as you use)
  }
})

const classes = computed(() => (props.variant === 'main' ? 'main-title' : 'subtitle'))
</script>

<style scoped>
.main-title {
  font-size: 2rem;        /* ~32px */
  font-weight: 700;
  color: var(--text-primary);      /* THEME TOKEN */
  line-height: 1.3;
  margin-bottom: 0.75rem;
  text-align: inherit;             /* inherit alignment from parent (center/left) */
}

.subtitle {
  font-size: 1.125rem;    /* ~18px */
  color: var(--text-secondary);    /* THEME TOKEN */
  line-height: 1.6;
  font-weight: 400;
  margin-top: 0.5rem;
  margin-bottom: 1.5rem;
  text-align: inherit;             /* inherit alignment from parent */
}
</style>
