<template>
  <footer class="footer">
    <div class="container footer-container">
      <div class="footer-brand">
        <svg class="logo-mark" viewBox="0 0 24 24" aria-hidden="true">
          <path fill="var(--primary-color)" d="M12 3l9 4-9 4-9-4 9-4Z"/>
          <path fill="#A5B4FC" d="M6 10v4c0 1.1.9 2 2 2h8c1.1 0 2-.9 2-2v-4l-6 3-6-3Z"/>
        </svg>
        <span class="logo-text">EduFinance</span>
      </div>
      <div class="footer-copyright">
        <p>&copy; 2025 EduFinance. All rights reserved.</p>
      </div>
      <nav class="footer-links">
        <a href="#about">About</a>
        <a href="#contact">Contact</a>
        <a href="#privacy">Privacy</a>
      </nav>
    </div>
  </footer>
</template>

<script setup>
</script>

<style scoped>
.footer {
  border-top: 1px solid var(--border-color);
  padding: 32px 0;
  background-color: var(--background-color);
}

.footer-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.footer-brand {
  display: flex;
  align-items: center;
  gap: 8px;
}

.logo-mark {
  width: 24px;
  height: 24px;
}

.logo-text {
  font-weight: 700;
  font-size: 18px;
  color: var(--text-color);
}

.footer-copyright {
  color: var(--muted-text-color);
  font-size: 14px;
}

.footer-links {
  display: flex;
  gap: 24px;
}

.footer-links a {
  color: var(--muted-text-color);
  text-decoration: none;
  font-size: 14px;
  font-weight: 500;
  transition: color 0.2s ease;
}

.footer-links a:hover {
  color: var(--primary-color);
}

@media (max-width: 768px) {
  .footer-container {
    flex-direction: column;
    gap: 24px;
  }

  .footer-copyright {
    order: 1;
  }
}
</style>