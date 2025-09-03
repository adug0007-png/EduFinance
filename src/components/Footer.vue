<template>
  <footer class="footer" role="contentinfo">
    <div class="container footer-container">
      <div class="footer-brand" @click="goHome" style="cursor:pointer">
        <svg class="logo-mark" viewBox="0 0 24 24" aria-hidden="true">
          <path fill="var(--primary-color)" d="M12 3l9 4-9 4-9-4 9-4Z"/>
          <path fill="#A5B4FC" d="M6 10v4c0 1.1.9 2 2 2h8c1.1 0 2-.9 2-2v-4l-6 3-6-3Z"/>
        </svg>
        <span class="logo-text">WealthWave</span>
      </div>

      <nav class="footer-links" aria-label="Footer">
        <!-- All links route to home -->
        <a href="#" @click.prevent="goHome">About</a>
        <a href="#" @click.prevent="goHome">Contact</a>
        <a href="#" @click.prevent="goHome">Privacy</a>
      </nav>
    </div>
  </footer>
</template>

<script setup>
import { inject } from 'vue'
const navigateTo = inject('navigateTo')
const goHome = () => navigateTo('home')
</script>

<style scoped>
.footer {
  position: relative;
  z-index: 0;
  margin-top: auto;                 /* sits at bottom when parent is flex column */
  padding: 24px 0;
  background: transparent;          /* glass is drawn by ::before */
}

/* Glass/blur layer */
.footer::before {
  content: "";
  position: absolute; inset: 0;
  z-index: -1;
  background: #BEDBF9;         /* more opaque for readability */
  backdrop-filter: blur(14px) saturate(160%);
  -webkit-backdrop-filter: blur(14px) saturate(160%);
  border-top: 1px solid rgba(255,255,255,.06);
}

/* Center everything */
.footer-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 12px;
}

/* Brand */
.footer-brand {
  display: flex;
  align-items: center;
  gap: 8px;
}
.logo-mark { width: 24px; height: 24px; }
.logo-text { font-weight: 700; font-size: 18px; color: #111827; }   /* stronger contrast */

/* Links */
.footer-links {
  display: flex;
  gap: 24px;
  flex-wrap: wrap;
  justify-content: center;
}
.footer-links a {
  color: #374151;                     /* darker than muted for legibility */
  text-decoration: none;
  font-size: 14px;
  font-weight: 500;
  transition: color .2s ease;
}
.footer-links a:hover { color: var(--primary-color); }
.footer-links a:focus-visible {
  outline: none;
  box-shadow: 0 0 0 2px var(--primary-color);
  border-radius: 6px;
  padding: 2px 4px;
}

/* Small screens */
@media (max-width: 480px) {
  .footer-links { gap: 16px; }
}

/* Dark mode */
@media (prefers-color-scheme: dark) {
  .footer::before {
    background: #030911;
    border-top: 1px solid rgba(255,255,255,.10);
  }
  .logo-text { color: #e5e7eb; }
  .footer-links a { color: #e5e7eb; }
  .footer-links a:hover { color: #c7d2fe; }
}
</style>
