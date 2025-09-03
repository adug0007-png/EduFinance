<template>
  <!-- Sticky site header -->
  <header
    ref="el"
    class="header"
    :class="[
      isDark ? 'theme-slate' : 'theme-pearl',
      (currentRoute !== 'home' || scrolled) && 'solid'
    ]"
    :data-ribbon="currentRoute === 'home' ? 'on' : 'off'"
  >
    <div class="container">
      <nav class="navbar">
        <!-- Logo -->
        <div
          class="logo"
          role="link"
          tabindex="0"
          @click="go('home')"
          @keydown.enter.prevent="go('home')"
          @keydown.space.prevent="go('home')"
          style="cursor:pointer"
        >
          <svg class="logo-mark" viewBox="0 0 24 24" aria-hidden="true">
            <path fill="var(--primary-color)" d="M12 3l9 4-9 4-9-4 9-4Z" />
            <path fill="#A5B4FC" d="M6 10v4c0 1.1.9 2 2 2h8c1.1 0 2-.9 2-2v-4l-6 3-6-3Z" />
          </svg>
          <span class="logo-text">WealthWave</span>
        </div>

        <!-- Mobile toggle -->
        <button class="menu-toggle" @click="menuOpen = !menuOpen" aria-label="Toggle menu">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
            <path d="M4 7h16M4 12h16M4 17h16" stroke="currentColor" stroke-width="2" stroke-linecap="round" />
          </svg>
        </button>

        <!-- Links -->
        <ul class="nav-links" :class="{ open: menuOpen }">
          <li><a href="#" :class="{active: currentRoute==='financial-literacy'}" @click.prevent="go('financial-literacy')">Financial Basics</a></li>
          <li><a href="#" :class="{active: currentRoute==='budget-planner'}" @click.prevent="go('budget-planner')">Budget Planner</a></li>
          <li><a href="#" :class="{active: currentRoute==='savings-goal-calculator'}" @click.prevent="go('savings-goal-calculator')">Savings Goals</a></li>
          <li><a href="#" :class="{active: currentRoute==='cost-estimator'}" @click.prevent="go('cost-estimator')">Study & Living Costs</a></li>
          <li><a href="#" :class="{active: currentRoute==='tax-learn'}" @click.prevent="go('tax-learn')">Taxes</a></li>
          <li><a href="#" :class="{active: currentRoute==='mortgage-calculator'}" @click.prevent="go('mortgage-calculator')">Home & Mortgage Planning</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <!-- Spacer: 0 on home, real height elsewhere -->
  <div
    class="header-spacer"
    :style="{ height: (currentRoute === 'home' ? '0px' : headerH + 'px') }"
    aria-hidden="true"
  />
</template>

<script setup>
import { inject, ref, onMounted, onBeforeUnmount, watch, nextTick } from 'vue'

const navigateTo = inject('navigateTo')
const currentRoute = inject('currentRoute')

const menuOpen = ref(false)
const go = (r) => { menuOpen.value = false; navigateTo(r) }

const isDark = ref(window.matchMedia?.('(prefers-color-scheme: dark)').matches ?? false)
let mql, themeHandler

// measure header height and publish to :root as --header-height
const el = ref(null)
const headerH = ref(72)

const scrolled = ref(false)
function onScroll() {
  scrolled.value = window.scrollY > 8
}

function publishHeight(h) {
  document.documentElement.style.setProperty('--header-height', `${h}px`)
}

function measure() {
  const h = el.value?.offsetHeight || 72
  headerH.value = h
  publishHeight(h)
}

let ro
function setupResizeObserver() {
  if (window.ResizeObserver && el.value) {
    ro = new ResizeObserver(measure)
    ro.observe(el.value)
  } else {
    window.addEventListener('resize', measure)
  }
}

onMounted(() => {
  // Dark mode listener
  mql = window.matchMedia('(prefers-color-scheme: dark)')
  themeHandler = (e) => { isDark.value = e.matches }
  mql.addEventListener('change', themeHandler)

  window.addEventListener('scroll', onScroll, { passive: true })
  onScroll()

  // Initial measure and observers
  nextTick(measure)
  setupResizeObserver()
})

// Re-measure when menu opens/closes (height can change on mobile)
watch(menuOpen, async () => { await nextTick(); measure() })

// Apply dark page backdrop ONLY when OS is dark AND we're off home
const DARK_CLASS = 'non-home-dark'
function applyPageTheme() {
  const html = document.documentElement
  const shouldDark = (currentRoute.value !== 'home') && isDark.value
  html.classList.toggle(DARK_CLASS, shouldDark)
}
watch([currentRoute, isDark], applyPageTheme, { immediate: true })

onBeforeUnmount(() => {
  mql?.removeEventListener('change', themeHandler)
  if (ro) ro.disconnect()
  else window.removeEventListener('resize', measure)
  window.removeEventListener('scroll', onScroll)
})
</script>

<!-- Global (unscoped) styles used when .non-home-dark is present -->
<style>
:root {
  --page-bg-dark: #0b1220;
  --page-text-dark: #e6eaf2;
}
.non-home-dark, .non-home-dark body {
  background-color: var(--page-bg-dark);
  color: var(--page-text-dark);
}
.non-home-dark main,
.non-home-dark .container,
.non-home-dark .page-section {
  background: transparent;
}
.non-home-dark .page-header { color: var(--page-text-dark); }
</style>

<style scoped>
/* ===== Header container ===== */
.header {
  position: sticky; top: 0; z-index: 40; width: 100%;
  isolation: isolate;
  background: transparent;
  box-shadow: 0 6px 20px rgba(0,0,0,.04);
}

/* spacer element lives outside the sticky header to push content down */
.header-spacer { width: 100%; }

/* ===== Glass layer (shared) — no color here ===== */
.header.theme-pearl::before,
.header.theme-slate::before {
  content: "";
  position: absolute; inset: 0;
  z-index: -1;
  backdrop-filter: blur(16px) saturate(160%);
  -webkit-backdrop-filter: blur(16px) saturate(160%);
  border-bottom: 1px solid transparent; /* set per theme */
}

/* Light ribbon */
.header.theme-pearl::before {
  background: #f0f8f9;
  border-bottom-color: rgba(255,255,255,.10);
}
.header.theme-pearl .logo-text { color: #111827; }              /* ensure dark logo in light theme */
.header.theme-pearl .nav-links a { color: #111827; }
.header.theme-pearl .nav-links a:hover { color: var(--primary-color); }
.header.theme-pearl .nav-links a::after { background: var(--primary-color); }

/* Dark ribbon */
.header.theme-slate::before {
  background: #030911;
  border-bottom-color: rgba(255,255,255,0.06);
}
.header.theme-slate .logo-text { color: #E5E7EB; }
.header.theme-slate .nav-links a { color: #e6eaf2; text-shadow: 0 1px 2px rgba(0,0,0, 0.35); }
.header.theme-slate .nav-links a:hover,
.header.theme-slate .nav-links a.active { color: #fff; }
.header.theme-slate .nav-links a::after { background: rgba(255,255,255,0.9); }

/* ===== Layout & sizing ===== */
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
  cursor: pointer;
}

.logo-mark { width: 32px !important; height: 32px !important; }
.logo-text { font-size: 22px !important; line-height: 1; font-weight: 700; letter-spacing: -0.02em; }

/* Desktop links */
.nav-links {
  display: flex;
  align-items: center;
  gap: 20px;
  list-style: none;
  margin: 0;
  padding: 0;
}
.nav-links a {
  position: relative;
  white-space: nowrap;
  padding: 10px 6px 12px;
  text-decoration: none;
  font-weight: 700;
  font-size: 16px;
  transition: color .15s ease;
}
.nav-links a::after {
  content: "";
  position: absolute;
  left: 0; right: 100%; bottom: 4px; height: 2px;
  border-radius: 1px;
  transition: right .22s ease;
}
.nav-links a:hover::after,
.nav-links a.active::after { right: 0; }

/* ===== Responsive nav ===== */
.menu-toggle {
  display: none;
  width: 40px; height: 40px;
  border: 1px solid currentColor; border-radius: 10px;
  background: transparent; color: currentColor; opacity: .85;
}

@media (max-width: 1200px) {
  .menu-toggle { display: inline-flex; align-items: center; justify-content: center; }

  /* Use dynamic header height for the dropdown top edge */
  .nav-links {
    position: fixed; left: 0; right: 0; top: var(--header-height, 72px);
    display: none;
    flex-direction: column; align-items: flex-start;
    gap: 12px; padding: 12px 16px;
    background: rgba(255,255,255,0.95);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    box-shadow: 0 12px 30px rgba(0,0,0,.14);
    z-index: 50;
  }
  .nav-links.open { display: flex; }

  .header.theme-slate .nav-links {
    background: rgba(3, 9, 17,0.92);
  }
}

/* Wider screens: scale brand and bar a bit */
@media (min-width: 1200px) {
  .logo-mark { width: 32px; height: 32px; }
  .header.theme-pearl .nav-links { background: rgba(251, 247, 247, 0.95); }
  .logo-text { font-size: clamp(22px, 1.8vw, 26px); }
}
@media (min-width: 1280px) {
  .logo-mark { width: 40px !important; height: 40px !important; }
  .logo-text { font-size: 24px !important; }
}
@media (min-width: 1536px) {
  .logo-mark { width: 46px !important; height: 46px !important; }
  .logo-text { font-size: 26px !important; }
}
@media (min-width: 1920px) {
  .logo-mark { width: 50px !important; height: 50px !important; }
  .logo-text { font-size: 28px !important; }
}

/* Keep the bar comfy as the logo grows */
.navbar { height: 72px; }
@media (min-width: 1536px) { .navbar { height: 76px; } }
@media (min-width: 1920px) { .navbar { height: 80px; } }

/* Ribbon visibility: hidden by default, only ON at home */
.header::before {
  opacity: 0;
  border-bottom-color: transparent;
  transition: opacity .18s ease, background-color .18s ease, border-color .18s ease;
}
.header { box-shadow: none; }
.header[data-ribbon="on"]::before { opacity: 1; }
.header[data-ribbon="on"] { box-shadow: 0 6px 20px rgba(0,0,0,.04); }

/* SOLID STATE: background depends on theme (no generic .header.solid::before) */
.header.theme-pearl.solid::before {
  opacity: 1;
  background: #ffffff;
  border-bottom-color: rgba(0,0,0,0.06);
}
.header.theme-slate.solid::before {
  opacity: 1;
  background: #0b1220;
  border-bottom-color: rgba(255,255,255,0.06);
}

/* Optional: subtle shadow when solid */
.header.solid { box-shadow: 0 4px 16px rgba(0,0,0,0.08); }
</style>
