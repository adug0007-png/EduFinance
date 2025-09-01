<template>
  <div class="financial-literacy">
    <!-- Header Section -->
    <div class="header-section">
      <div class="header-content">
        <div class="header-left">
          <h1 class="page-title">Financial Literacy Modules</h1>
          <div class="breadcrumb">
            <span class="breadcrumb-item">Learning Hub</span>
            <span class="breadcrumb-separator">›</span>
            <span class="breadcrumb-item active">Financial Literacy</span>
          </div>
        </div>
        
        <div class="header-controls">
          <div class="search-box">
            <input type="text" placeholder="Search modules..." class="search-input">
            <svg class="search-icon" width="16" height="16" viewBox="0 0 24 24" fill="none">
              <path d="M21 21L16.514 16.506M19 10.5A8.5 8.5 0 1 1 10.5 2a8.5 8.5 0 0 1 8.5 8.5Z" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
            </svg>
          </div>
          <button class="filter-btn">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none">
              <path d="M3 6h18M7 12h10M11 18h2" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
            </svg>
            Filter
          </button>
        </div>
      </div>
    </div>

    <!-- Description Section -->
    <div class="description-section">
      <div class="description-content">
        <p class="page-description">
          Master essential financial skills through our comprehensive learning modules. Each lesson is designed to build your confidence and knowledge in managing personal finances.
        </p>
      </div>
    </div>

    <!-- Main Content -->
    <div class="main-content">
      <!-- Learning Modules Grid -->
      <div class="modules-grid">
        <!-- Understanding Inflation Module -->
        <div class="module-card">
          <div class="module-image">
            <img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='200' viewBox='0 0 300 200'%3E%3Crect width='300' height='200' fill='%23f0f4ff'/%3E%3Cpath d='M50 150 L80 130 L110 140 L140 110 L170 120 L200 90 L230 100 L250 70' stroke='%234f46e5' stroke-width='3' fill='none'/%3E%3Cpath d='M250 70 L245 80 L255 80 Z' fill='%234f46e5'/%3E%3Crect x='60' y='140' width='15' height='10' fill='%23e5e7eb'/%3E%3Crect x='90' y='130' width='15' height='20' fill='%23e5e7eb'/%3E%3Crect x='120' y='120' width='15' height='30' fill='%23e5e7eb'/%3E%3Crect x='150' y='110' width='15' height='40' fill='%23e5e7eb'/%3E%3Crect x='180' y='100' width='15' height='50' fill='%23e5e7eb'/%3E%3C/svg%3E" alt="Understanding Inflation">
          </div>
          <div class="module-content">
            <h3 class="module-title">Understanding Inflation</h3>
            <div class="module-rating">
              <div class="stars">
                <span class="star filled">★</span>
                <span class="star filled">★</span>
                <span class="star filled">★</span>
                <span class="star filled">★</span>
                <span class="star filled">★</span>
              </div>
              <span class="rating-value">5.0</span>
            </div>
            <p class="module-description">
              Learn how inflation affects your purchasing power and investment decisions.
            </p>
            <div class="module-meta">
              <span class="duration">⏱ 45 mins</span>
              <span class="difficulty easy">Easy</span>
            </div>
            <button class="start-learning-btn">Start Learning</button>
          </div>
        </div>

        <!-- Smart Budgeting Module -->
        <div class="module-card">
          <div class="module-image">
            <img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='200' viewBox='0 0 300 200'%3E%3Crect width='300' height='200' fill='%23f0f9ff'/%3E%3Crect x='60' y='60' width='180' height='120' rx='8' fill='white' stroke='%23e5e7eb'/%3E%3Crect x='80' y='80' width='60' height='40' rx='4' fill='%2306b6d4'/%3E%3Crect x='80' y='130' width='140' height='8' rx='4' fill='%23e5e7eb'/%3E%3Crect x='80' y='145' width='100' height='8' rx='4' fill='%23e5e7eb'/%3E%3Crect x='80' y='160' width='120' height='8' rx='4' fill='%23e5e7eb'/%3E%3Ctext x='190' y='95' font-family='Arial' font-size='12' fill='%234f46e5'%3E$2,500%3C/text%3E%3C/svg%3E" alt="Smart Budgeting">
          </div>
          <div class="module-content">
            <h3 class="module-title">Smart Budgeting</h3>
            <div class="module-rating">
              <div class="stars">
                <span class="star filled">★</span>
                <span class="star filled">★</span>
                <span class="star filled">★</span>
                <span class="star filled">★</span>
                <span class="star filled">★</span>
              </div>
              <span class="rating-value">5.0</span>
            </div>
            <p class="module-description">
              Master the art of creating and maintaining effective personal budgets.
            </p>
            <div class="module-meta">
              <span class="duration">⏱ 60 mins</span>
              <span class="difficulty easy">Easy</span>
            </div>
            <button class="start-learning-btn">Start Learning</button>
          </div>
        </div>

        <!-- Saving Strategies Module -->
        <div class="module-card">
          <div class="module-image">
            <img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='200' viewBox='0 0 300 200'%3E%3Crect width='300' height='200' fill='%23fef3e2'/%3E%3Ccircle cx='150' cy='100' r='40' fill='%23f59e0b' opacity='0.2'/%3E%3Cpath d='M130 90 Q150 70 170 90 Q150 110 130 90' fill='%23f59e0b'/%3E%3Crect x='80' y='130' width='15' height='30' rx='2' fill='%23d97706'/%3E%3Crect x='100' y='120' width='15' height='40' rx='2' fill='%23d97706'/%3E%3Crect x='120' y='110' width='15' height='50' rx='2' fill='%23d97706'/%3E%3Crect x='140' y='100' width='15' height='60' rx='2' fill='%23d97706'/%3E%3Crect x='160' y='90' width='15' height='70' rx='2' fill='%23d97706'/%3E%3Crect x='180' y='80' width='15' height='80' rx='2' fill='%23d97706'/%3E%3Crect x='200' y='70' width='15' height='90' rx='2' fill='%23d97706'/%3E%3C/svg%3E" alt="Saving Strategies">
          </div>
          <div class="module-content">
            <h3 class="module-title">Saving Strategies</h3>
            <div class="module-rating">
              <div class="stars">
                <span class="star filled">★</span>
                <span class="star filled">★</span>
                <span class="star filled">★</span>
                <span class="star filled">★</span>
                <span class="star">★</span>
              </div>
              <span class="rating-value">4.0</span>
            </div>
            <p class="module-description">
              Discover proven methods to build your emergency fund and savings goals.
            </p>
            <div class="module-meta">
              <span class="duration">⏱ 50 mins</span>
              <span class="difficulty medium">Medium</span>
            </div>
            <button class="start-learning-btn">Start Learning</button>
          </div>
        </div>

        <!-- Credit Management Module -->
        <div class="module-card">
          <div class="module-image">
            <img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='200' viewBox='0 0 300 200'%3E%3Crect width='300' height='200' fill='%23f0fdf4'/%3E%3Crect x='70' y='80' width='160' height='100' rx='8' fill='%2316a34a'/%3E%3Crect x='80' y='90' width='140' height='60' rx='4' fill='%23dcfce7'/%3E%3Ctext x='90' y='110' font-family='Arial' font-size='10' fill='%2316a34a'%3ECREDIT CARD%3C/text%3E%3Ctext x='90' y='130' font-family='Arial' font-size='8' fill='%2316a34a'%3E•••• •••• •••• 1234%3C/text%3E%3Crect x='190' y='95' width='30' height='20' rx='2' fill='%2316a34a'/%3E%3Crect x='80' y='160' width='40' height='8' rx='2' fill='%23dcfce7'/%3E%3C/svg%3E" alt="Credit Management">
          </div>
          <div class="module-content">
            <h3 class="module-title">Credit Management</h3>
            <div class="module-rating">
              <div class="stars">
                <span class="star filled">★</span>
                <span class="star filled">★</span>
                <span class="star filled">★</span>
                <span class="star filled">★</span>
                <span class="star">★</span>
              </div>
              <span class="rating-value">4.0</span>
            </div>
            <p class="module-description">
              Build and maintain excellent credit while avoiding common pitfalls.
            </p>
            <div class="module-meta">
              <span class="duration">⏱ 75 mins</span>
              <span class="difficulty medium">Medium</span>
            </div>
            <button class="start-learning-btn">Start Learning</button>
          </div>
        </div>

        <!-- Investment Fundamentals Module -->
        <div class="module-card">
          <div class="module-image">
            <img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='200' viewBox='0 0 300 200'%3E%3Crect width='300' height='200' fill='%23faf5ff'/%3E%3Cpath d='M50 150 Q80 120 110 130 Q140 100 170 110 Q200 80 230 90 Q250 70 270 80' stroke='%237c3aed' stroke-width='3' fill='none'/%3E%3Cpath d='M270 80 L265 85 L270 90 L275 85 Z' fill='%237c3aed'/%3E%3Crect x='60' y='140' width='12' height='20' fill='%23c4b5fd'/%3E%3Crect x='80' y='130' width='12' height='30' fill='%23c4b5fd'/%3E%3Crect x='100' y='120' width='12' height='40' fill='%23c4b5fd'/%3E%3Crect x='120' y='110' width='12' height='50' fill='%23c4b5fd'/%3E%3Crect x='140' y='100' width='12' height='60' fill='%23c4b5fd'/%3E%3Crect x='160' y='90' width='12' height='70' fill='%23c4b5fd'/%3E%3Crect x='180' y='80' width='12' height='80' fill='%23c4b5fd'/%3E%3C/svg%3E" alt="Investment Fundamentals">
          </div>
          <div class="module-content">
            <h3 class="module-title">Investment Fundamentals</h3>
            <div class="module-rating">
              <div class="stars">
                <span class="star filled">★</span>
                <span class="star filled">★</span>
                <span class="star filled">★</span>
                <span class="star filled">★</span>
                <span class="star filled">★</span>
              </div>
              <span class="rating-value">5.0</span>
            </div>
            <p class="module-description">
              Start your investment journey with solid foundations and risk management.
            </p>
            <div class="module-meta">
              <span class="duration">⏱ 90 mins</span>
              <span class="difficulty advanced">Advanced</span>
            </div>
            <button class="start-learning-btn">Start Learning</button>
          </div>
        </div>
      </div>

      <!-- Learning Progress Section -->
      <div class="progress-section">
        <div class="progress-header">
          <h2 class="progress-title">Your Learning Progress</h2>
          <button class="view-all-btn">📚 View All Courses</button>
        </div>
        
        <div class="progress-stats">
          <div class="stat-item">
            <div class="stat-number blue">2</div>
            <div class="stat-label">Modules Completed</div>
          </div>
          <div class="stat-item">
            <div class="stat-number purple">3</div>
            <div class="stat-label">In Progress</div>
          </div>
          <div class="stat-item">
            <div class="stat-number pink">15</div>
            <div class="stat-label">Total Hours</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'FinancialLiteracy',
  data() {
    return {
      searchQuery: ''
    }
  },
  methods: {
    startLearning(moduleTitle) {
      console.log(`Starting learning: ${moduleTitle}`)
      // 这里可以添加具体的学习逻辑
    }
  }
}
</script>

<style scoped>
.financial-literacy {
  min-height: 100vh;
  background: #f8fafc;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}

/* Header Section */
.header-section {
  background: white;
  border-bottom: 1px solid #e5e7eb;
  padding: 24px 0;
}

.header-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 24px;
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 32px;
}

.header-left {
  flex: 1;
}

.page-title {
  font-size: 32px;
  font-weight: 700;
  color: #111827;
  margin: 0 0 8px 0;
}

.breadcrumb {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 14px;
  color: #6b7280;
}

.breadcrumb-item.active {
  color: #4f46e5;
  font-weight: 500;
}

.breadcrumb-separator {
  color: #d1d5db;
}

/* Description Section */
.description-section {
  background: #f8fafc;
  padding: 20px 0;
}

.description-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 24px;
}

.page-description {
  font-size: 16px;
  color: #6b7280;
  line-height: 1.6;
  margin: 0;
  max-width: 800px;
}

.header-controls {
  display: flex;
  align-items: center;
  gap: 12px;
}

.search-box {
  position: relative;
}

.search-input {
  width: 280px;
  height: 40px;
  padding: 0 16px 0 40px;
  border: 1px solid #d1d5db;
  border-radius: 8px;
  font-size: 14px;
  background: white;
}

.search-input:focus {
  outline: none;
  border-color: #4f46e5;
  box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.1);
}

.search-icon {
  position: absolute;
  left: 12px;
  top: 50%;
  transform: translateY(-50%);
  color: #9ca3af;
}

.filter-btn {
  height: 40px;
  padding: 0 16px;
  background: white;
  border: 1px solid #d1d5db;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 500;
  color: #374151;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 8px;
}

.filter-btn:hover {
  background: #f9fafb;
}

/* Main Content */
.main-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 40px 24px;
}

.modules-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 24px;
  margin-bottom: 48px;
}

.module-card {
  background: white;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s, box-shadow 0.2s;
}

.module-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.module-image {
  width: 100%;
  height: 200px;
  overflow: hidden;
}

.module-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.module-content {
  padding: 20px;
}

.module-title {
  font-size: 18px;
  font-weight: 600;
  color: #111827;
  margin: 0 0 8px 0;
}

.module-rating {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 12px;
}

.stars {
  display: flex;
  gap: 2px;
}

.star {
  color: #d1d5db;
  font-size: 14px;
}

.star.filled {
  color: #fbbf24;
}

.rating-value {
  font-size: 14px;
  font-weight: 500;
  color: #6b7280;
}

.module-description {
  font-size: 14px;
  color: #6b7280;
  line-height: 1.5;
  margin: 0 0 16px 0;
}

.module-meta {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 16px;
  font-size: 14px;
}

.duration {
  color: #6b7280;
}

.difficulty {
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 500;
}

.difficulty.easy {
  background: #dcfce7;
  color: #16a34a;
}

.difficulty.medium {
  background: #fef3c7;
  color: #d97706;
}

.difficulty.advanced {
  background: #fde4e4;
  color: #dc2626;
}

.start-learning-btn {
  width: 100%;
  height: 40px;
  background: #4f46e5;
  color: white;
  border: none;
  border-radius: 6px;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  transition: background-color 0.2s;
}

.start-learning-btn:hover {
  background: #4338ca;
}

/* Progress Section */
.progress-section {
  background: white;
  border-radius: 12px;
  padding: 32px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.progress-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24px;
}

.progress-title {
  font-size: 24px;
  font-weight: 700;
  color: #1e40af;
  margin: 0;
}

.view-all-btn {
  background: #3b82f6;
  color: white;
  border: none;
  padding: 8px 16px;
  border-radius: 6px;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
}

.view-all-btn:hover {
  background: #2563eb;
}

.progress-stats {
  display: flex;
  justify-content: space-around;
  text-align: center;
}

.stat-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
}

.stat-number {
  font-size: 48px;
  font-weight: 700;
}

.stat-number.blue {
  color: #3b82f6;
}

.stat-number.purple {
  color: #8b5cf6;
}

.stat-number.pink {
  color: #ec4899;
}

.stat-label {
  font-size: 14px;
  color: #6b7280;
  font-weight: 500;
}

@media (max-width: 768px) {
  .header-content {
    flex-direction: column;
    gap: 20px;
  }
  
  .header-controls {
    width: 100%;
    justify-content: space-between;
  }
  
  .search-input {
    width: 200px;
  }
  
  .modules-grid {
    grid-template-columns: 1fr;
  }
  
  .progress-stats {
    flex-direction: column;
    gap: 24px;
  }
}
</style>