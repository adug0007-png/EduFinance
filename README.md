# WealthWave  
**Know your costs. Budget, save, understand tax.**  
A lightweight Vue 3 (Vite) app that helps students & newcomers understand everyday money concepts with calculators, flashcards, and curated video guides.

<p align="left">
  <a href="https://vuejs.org/">
    <img src="https://img.shields.io/badge/Vue-3.x-42b883?logo=vue.js&logoColor=white" alt="Vue 3">
  </a>
  <a href="https://vitejs.dev/">
    <img src="https://img.shields.io/badge/Vite-5.x-646CFF?logo=vite&logoColor=white" alt="Vite">
  </a>
  <a href="https://eslint.org/">
    <img src="https://img.shields.io/badge/ESLint-configured-4B32C3?logo=eslint&logoColor=white" alt="ESLint">
  </a>
  <a href="https://prettier.io/">
    <img src="https://img.shields.io/badge/Prettier-on-1A2C34?logo=prettier&logoColor=F7B93E" alt="Prettier">
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/Deploy-AWS%20Amplify-FF9900?logo=amazon-aws&logoColor=white" alt="AWS Amplify">
  </a>
</p>

---

## 🚀 Live Demo
- **URL:** https://main.d17hcgnbwdrpcf.amplifyapp.com/  
- **Login (demo):** `admin / admin28` *(showcase only—rotate/remove for production)*

---

## ✨ Features
- **Modular Vue SPA** — Simple hash-based navigation with a sticky `Header` and per-page `PageHeader`.
- **Polished Home** — Hero section with preserved background images (light & dark), CTA to Tax & Super.
- **Smart Theming** — Auto flips with OS setting.  
  - Home keeps a translucent ribbon.  
  - Non-home pages use a solid, legible header; inputs/text stay readable in both modes.
- **Tax & Super** — Take-home pay calculator (AU 2023–24 brackets + Medicare + 11.5% super) and **flashcards** with arrow + “previous/next term” buttons.
- **Video Guides** — Financial basics page showcasing embedded YouTube cards (grid layout).
- **Scoped release** — “Home & Mortgage Planning” and “Study & Living Costs” are **hidden** from the header (kept out of user flow).

> Educational tool only—**not financial advice**.

---


## 🧱 Project Structure
```
src/
  components/
    Header.vue              # sticky nav (theme-aware, hash routing links)
    Hero.vue                # home hero + CTA → tax-learn
    PageHeader.vue          # title/subtitle block (light/dark-aware)
    Typography.vue          # h1/subtitle primitives
    BudgetPlanner.vue
    SavingsGoalCalculator.vue
    FinancialLiteracy.vue   # "Video Guides"
    TaxLearn.vue            # calculator + flashcards + facts
    Footer.vue
  App.vue                   # simple hash router + page headers
  main.js
  style.css                 # tokens, globals, light/dark text rules
public/
  hero-bg-light.png
  hero-bg-dark.png
```
---

## 🎛 Theming & UX (current)
- **Header ribbon**  
  - Home: glassy ribbon over hero image.  
  - Non-home: solid header (light or dark), improves readability on scroll.
- **Dark mode (non-home)**  
  Applied when **OS is dark** and **route ≠ home**; backgrounds, inputs, and labels keep contrast.
- **Home CTA**  
  Routes to **Tax & Super** page.

---

## 🧮 AU Tax Logic (in `TaxLearn.vue`)
- **2023–24 resident brackets** for Income Tax.  
- **Medicare Levy**: 2%.  
- **Superannuation (employer)**: 11.5%.  
- **Net Pay** = `salary – incomeTax – medicareLevy`.  
- Numbers are formatted with thousands separators; math is commented inline.

---

## 🛠 Getting Started
**Requirements:** Node 18+ (or 20+), npm or pnpm.

```bash
# install deps
npm install

# run dev server
npm run dev

# build for production
npm run build

# preview production build locally
npm run preview
```

---



## ✅ Code Quality for Final Release
**Modular Codebase Design:** Features live in small, reusable pieces (calculators, flashcards, video cards, header/page-header) to keep changes isolated.  
**Version Control with Git:** Branch-per-feature with short PRs ; clear commits for quick rollback.  
**Consistent Styling & Linting:** ESLint + Prettier; shared CSS variables for spacing/colors/light-dark; avoid `!important` unless scoped.  
**Manual Peer Review:** Self-review + quick walkthrough with the team for logic, copy, and flows before merge.  
**Testing Before Merge:** Smoke test key flows (nav → inputs → results), light/dark, and mobile; spot-check edge cases (empty/large values).  
**Well-Commented Code & Documentation:** Non-obvious logic (tax math, formatting) commented; README documents setup, structure, and release notes.

---

## ☁️ Deployment (AWS Amplify)
- Connect the Git repository; build: `npm ci && npm run build`.
- SPA behavior: default Amplify rewrite to `/index.html` (hash routing friendly).
- Keep previous deployment for one-click rollback.

---


## ⚠️ Disclaimer
This project is for educational purposes only and does not provide financial advice.
