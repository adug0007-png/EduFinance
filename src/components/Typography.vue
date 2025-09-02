<template>
  <component :is="tag" :class="classes">
    <slot />
  </component>
</template>

<script setup>
import { computed } from 'vue'

// 接收 props 来区分主标题/副标题
const props = defineProps({
  variant: {
    type: String,
    default: 'subtitle' // 可选: 'main' | 'subtitle'
  },
  tag: {
    type: String,
    default: 'p' // 主标题用 h1, 副标题用 p
  }
})

const classes = computed(() => {
  if (props.variant === 'main') {
    return 'main-title'
  }
  return 'subtitle'
})
</script>

<style scoped>
.main-title {
  font-size: 2rem;        /* ~32px */
  font-weight: 700;
  color: #111827;         /* 深灰 */
  line-height: 1.3;
  margin-bottom: 0.75rem;
  text-align: center;
}

.subtitle {
  font-size: 1.125rem;    /* ~18px */
  color: #6B7280;         /* 灰色 */
  line-height: 1.6;
  font-weight: 400;
  margin-top: 0.5rem;
  margin-bottom: 1.5rem;
  text-align: center;
}
</style>
