<template>
  <div class="tax-learn">
    <!-- Header Section -->
    <div class="header-section">
      <div class="header-content">
        <div class="logo">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
            <circle cx="12" cy="12" r="10" fill="#4f46e5"/>
            <path d="M8 14s1.5 2 4 2 4-2 4-2" stroke="white" stroke-width="2"/>
          </svg>
          <span class="logo-text">TaxLearn</span>
        </div>
        <nav class="top-nav">
          <a href="#" class="nav-link">Home</a>
          <a href="#" class="nav-link">Tools</a>
          <a href="#" class="nav-link">Resources</a>
          <a href="#" class="nav-link">Contact</a>
        </nav>
      </div>
    </div>

    <!-- Main Title -->
    <div class="title-section">
      <h1 class="main-title">Learn Tax & Super</h1>
      <p class="main-subtitle">
        Interactive flashcards and calculators to master Australian taxation and<br>
        superannuation. Study, calculate, and understand your finances better.
      </p>
    </div>

    <!-- Main Content -->
    <div class="main-content">
      <!-- Left Column - Salary Calculator -->
      <div class="left-column">
        <div class="calculator-card">
          <div class="card-header">
            <h2 class="card-title">Salary Calculator</h2>
            <button class="refresh-btn">🔄</button>
          </div>
          <p class="card-subtitle">Flip the card to see your take-home pay</p>

          <div class="form-group">
            <label class="form-label">Annual Gross Salary</label>
            <div class="input-container">
              <span class="currency-symbol">$</span>
              <input type="text" class="form-input" v-model="grossSalary">
            </div>
          </div>

          <div class="form-row">
            <div class="form-group">
              <label class="form-label">Pay Frequency</label>
              <select class="form-select" v-model="payFrequency">
                <option value="Annual">Annual</option>
                <option value="Monthly">Monthly</option>
              </select>
            </div>
            <div class="form-group">
              <label class="form-label">State</label>
              <select class="form-select" v-model="state">
                <option value="NSW">NSW</option>
                <option value="VIC">VIC</option>
              </select>
            </div>
          </div>

          <button class="calculate-btn">📊 Calculate Take-Home Pay</button>

          <div class="breakdown-section">
            <h3 class="breakdown-title">Your Breakdown</h3>
            <div class="salary-display">
              <div class="salary-label">Gross Salary</div>
              <div class="salary-amount">$75,000</div>
              <div class="progress-bar">
                <div class="progress-fill"></div>
              </div>
            </div>

            <div class="tax-breakdown">
              <div class="tax-item income-tax">
                <div class="tax-color red"></div>
                <div class="tax-info">
                  <div class="tax-name">Income Tax</div>
                  <div class="tax-amount">$14,842</div>
                  <div class="tax-period">per year</div>
                </div>
              </div>
              <div class="tax-item medicare">
                <div class="tax-color orange"></div>
                <div class="tax-info">
                  <div class="tax-name">Medicare Levy</div>
                  <div class="tax-amount">$1,500</div>
                  <div class="tax-period">per year</div>
                </div>
              </div>
              <div class="tax-item net-pay">
                <div class="tax-color green"></div>
                <div class="tax-info">
                  <div class="tax-name">Net Pay</div>
                  <div class="tax-amount">$58,658</div>
                  <div class="tax-period">per year</div>
                </div>
              </div>
              <div class="tax-item super">
                <div class="tax-color blue"></div>
                <div class="tax-info">
                  <div class="tax-name">Superannuation (11%)</div>
                  <div class="tax-amount">$8,250</div>
                  <div class="tax-period">per year</div>
                  <div class="tax-note">Employer contribution</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Right Column - Super Flashcards -->
      <div class="right-column">
        <div class="flashcard-section">
          <div class="section-header">
            <h2 class="section-title">Super Flashcards</h2>
            <div class="nav-arrows">
              <button class="arrow-btn">◀</button>
              <button class="arrow-btn">▶</button>
            </div>
          </div>
          <p class="section-subtitle">Click cards to reveal explanations</p>

          <!-- Study Super Concepts -->
          <div class="concept-card">
            <div class="concept-header">
              <h3 class="concept-title">Study Super Concepts</h3>
              <span class="concept-count">1/4 Done</span>
            </div>
            
            <div class="concept-content">
              <p class="concept-text">
                The Superannuation Guarantee (SG) is the mandatory contribution 
                your employer must make to your super fund. Currently set at 11% 
                of your ordinary time earnings.
              </p>
              <a href="#" class="concept-link">Tap to flip back</a>
            </div>

            <div class="concept-items">
              <div class="concept-item">
                <div class="item-icon green">●</div>
                <div class="item-content">
                  <div class="item-title">Salary Sacrifice</div>
                  <div class="item-subtitle">Additional voluntary contributions</div>
                </div>
                <div class="item-status">Optional</div>
              </div>
              <div class="concept-item">
                <div class="item-icon purple">●</div>
                <div class="item-content">
                  <div class="item-title">Government Co-contribution</div>
                  <div class="item-subtitle">Up to $500 for eligible earners</div>
                </div>
                <div class="item-amount">$500</div>
              </div>
            </div>
          </div>

          <!-- Key Super Facts -->
          <div class="facts-section">
            <h3 class="facts-title">Key Super Facts</h3>
            <div class="facts-grid">
              <div class="fact-item">
                <div class="fact-icon">⚡</div>
                <div class="fact-content">
                  <div class="fact-label">Current Rate</div>
                  <div class="fact-value">11%</div>
                  <div class="fact-desc">Minimum employer contribution</div>
                </div>
              </div>
              <div class="fact-item">
                <div class="fact-icon">🎯</div>
                <div class="fact-content">
                  <div class="fact-label">Preservation Age</div>
                  <div class="fact-value">60</div>
                  <div class="fact-desc">When you can access super</div>
                </div>
              </div>
              <div class="fact-item">
                <div class="fact-icon">💰</div>
                <div class="fact-content">
                  <div class="fact-label">Concessional Cap</div>
                  <div class="fact-value">$27,500</div>
                  <div class="fact-desc">Annual contribution limit</div>
                </div>
              </div>
              <div class="fact-item">
                <div class="fact-icon">📊</div>
                <div class="fact-content">
                  <div class="fact-label">Tax Rate</div>
                  <div class="fact-value">15%</div>
                  <div class="fact-desc">Tax on super contributions</div>
                </div>
              </div>
            </div>
          </div>

          <!-- Expandable Sections -->
          <div class="expandable-sections">
            <div class="expandable-item">
              <div class="expandable-header">
                <span>Benefits of Super</span>
                <span>▼</span>
              </div>
            </div>
            <div class="expandable-item">
              <div class="expandable-header">
                <span>Super Strategies</span>
                <span>▼</span>
              </div>
            </div>
          </div>

          <!-- Get Advice Section -->
          <div class="advice-section">
            <div class="advice-content">
              <p class="advice-text">Ready to optimize your super?</p>
              <p class="advice-subtext">Get personalized advice from our experts</p>
            </div>
            <button class="advice-btn">Get Advice</button>
          </div>
        </div>
      </div>
    </div>

    <!-- Additional Resources -->
    <div class="resources-section">
      <h2 class="resources-title">Additional Resources</h2>
      <div class="resources-grid">
        <div class="resource-item">
          <div class="resource-icon blue">📅</div>
          <h3 class="resource-title">Tax Guide</h3>
          <p class="resource-desc">Comprehensive guide to Australian taxation</p>
        </div>
        <div class="resource-item">
          <div class="resource-icon green">⚙️</div>
          <h3 class="resource-title">More Calculators</h3>
          <p class="resource-desc">Explore our full suite of financial tools</p>
        </div>
        <div class="resource-item">
          <div class="resource-icon purple">📞</div>
          <h3 class="resource-title">Expert Advice</h3>
          <p class="resource-desc">Speak with our qualified financial advisers</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TaxLearn',
  data() {
    return {
      grossSalary: '75,000',
      payFrequency: 'Annual',
      state: 'NSW'
    }
  }
}
</script>

<style scoped>
.tax-learn {
  min-height: 100vh;
  background: #f8fafc;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}

/* Header Section */
.header-section {
  background: white;
  border-bottom: 1px solid #e5e7eb;
  padding: 12px 0;
}

.header-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 24px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo {
  display: flex;
  align-items: center;
  gap: 8px;
}

.logo-text {
  font-size: 18px;
  font-weight: 700;
  color: #1f2937;
}

.top-nav {
  display: flex;
  gap: 32px;
}

.nav-link {
  color: #6b7280;
  text-decoration: none;
  font-size: 14px;
  font-weight: 500;
}

.nav-link:hover {
  color: #4f46e5;
}

/* Title Section */
.title-section {
  text-align: center;
  padding: 60px 24px 40px;
  background: white;
}

.main-title {
  font-size: 48px;
  font-weight: 700;
  color: #4f46e5;
  margin: 0 0 16px 0;
}

.main-subtitle {
  font-size: 16px;
  color: #6b7280;
  line-height: 1.6;
  margin: 0;
}

/* Main Content */
.main-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 40px 24px;
  display: grid;
  grid-template-columns: 400px 1fr;
  gap: 40px;
}

/* Left Column - Calculator */
.calculator-card {
  background: white;
  border-radius: 16px;
  padding: 24px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
  border: 1px solid #e5e7eb;
  height: fit-content;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 8px;
}

.card-title {
  font-size: 20px;
  font-weight: 700;
  color: #1f2937;
  margin: 0;
}

.refresh-btn {
  background: none;
  border: none;
  color: #6b7280;
  cursor: pointer;
  padding: 4px;
  font-size: 16px;
}

.refresh-btn:hover {
  color: #4f46e5;
}

.card-subtitle {
  color: #6b7280;
  font-size: 14px;
  margin: 0 0 24px 0;
}

.form-group {
  margin-bottom: 20px;
}

.form-label {
  display: block;
  font-size: 14px;
  font-weight: 600;
  color: #374151;
  margin-bottom: 8px;
}

.input-container {
  position: relative;
}

.currency-symbol {
  position: absolute;
  left: 12px;
  top: 50%;
  transform: translateY(-50%);
  color: #6b7280;
  font-size: 16px;
}

.form-input {
  width: 100%;
  height: 44px;
  padding: 0 16px 0 32px;
  border: 1px solid #d1d5db;
  border-radius: 6px;
  font-size: 16px;
  background: white;
  box-sizing: border-box;
}

.form-input:focus {
  outline: none;
  border-color: #4f46e5;
  box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.1);
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
}

.form-select {
  width: 100%;
  height: 44px;
  padding: 0 12px;
  border: 1px solid #d1d5db;
  border-radius: 6px;
  font-size: 16px;
  background: white;
  box-sizing: border-box;
}

.form-select:focus {
  outline: none;
  border-color: #4f46e5;
  box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.1);
}

.calculate-btn {
  width: 100%;
  height: 48px;
  background: #4f46e5;
  color: white;
  border: none;
  border-radius: 6px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  margin-bottom: 24px;
}

.calculate-btn:hover {
  background: #4338ca;
}

/* Breakdown Section */
.breakdown-section {
  border-top: 1px solid #e5e7eb;
  padding-top: 20px;
}

.breakdown-title {
  font-size: 16px;
  font-weight: 700;
  color: #1f2937;
  margin: 0 0 16px 0;
}

.salary-display {
  margin-bottom: 16px;
}

.salary-label {
  font-size: 14px;
  color: #374151;
  margin-bottom: 4px;
}

.salary-amount {
  font-size: 18px;
  font-weight: 700;
  color: #1f2937;
  margin-bottom: 8px;
}

.progress-bar {
  height: 8px;
  background: #f3f4f6;
  border-radius: 4px;
  overflow: hidden;
  position: relative;
}

.progress-fill {
  height: 100%;
  background: #10b981;
  width: 100%;
  border-radius: 4px;
}

/* Tax Breakdown */
.tax-breakdown {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
}

.tax-item {
  display: flex;
  align-items: flex-start;
  gap: 8px;
  padding: 12px;
  border-radius: 8px;
  background: #f9fafb;
}

.tax-color {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  flex-shrink: 0;
  margin-top: 2px;
}

.tax-color.red { background: #ef4444; }
.tax-color.orange { background: #f97316; }
.tax-color.green { background: #10b981; }
.tax-color.blue { background: #3b82f6; }

.tax-info {
  flex: 1;
  min-width: 0;
}

.tax-name {
  font-size: 12px;
  color: #6b7280;
  margin-bottom: 2px;
}

.tax-amount {
  font-size: 14px;
  font-weight: 700;
  color: #1f2937;
}

.tax-period {
  font-size: 11px;
  color: #9ca3af;
}

.tax-note {
  font-size: 11px;
  color: #6b7280;
  margin-top: 2px;
}

.tax-item.super {
  grid-column: 1 / -1;
}

/* Right Column */
.right-column {
  background: white;
  border-radius: 16px;
  padding: 24px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
  border: 1px solid #e5e7eb;
  height: fit-content;
}

.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 8px;
}

.section-title {
  font-size: 20px;
  font-weight: 700;
  color: #1f2937;
  margin: 0;
}

.nav-arrows {
  display: flex;
  gap: 4px;
}

.arrow-btn {
  background: #f3f4f6;
  border: none;
  border-radius: 4px;
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  color: #6b7280;
  font-size: 14px;
}

.arrow-btn:hover {
  background: #e5e7eb;
  color: #374151;
}

.section-subtitle {
  color: #6b7280;
  font-size: 14px;
  margin: 0 0 24px 0;
}

/* Concept Card */
.concept-card {
  background: #f8fafc;
  border-radius: 12px;
  padding: 20px;
  margin-bottom: 24px;
}

.concept-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
}

.concept-title {
  font-size: 16px;
  font-weight: 700;
  color: #1f2937;
  margin: 0;
}

.concept-count {
  background: #4f46e5;
  color: white;
  padding: 4px 12px;
  border-radius: 12px;
  font-size: 12px;
  font-weight: 600;
}

.concept-content {
  margin-bottom: 16px;
}

.concept-text {
  color: #374151;
  font-size: 14px;
  line-height: 1.5;
  margin: 0 0 8px 0;
}

.concept-link {
  color: #4f46e5;
  font-size: 12px;
  text-decoration: none;
  font-weight: 500;
}

.concept-link:hover {
  text-decoration: underline;
}

.concept-items {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.concept-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px;
  background: white;
  border-radius: 8px;
  border: 1px solid #e5e7eb;
}

.item-icon {
  font-size: 12px;
  width: 12px;
  height: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.item-icon.green { color: #10b981; }
.item-icon.purple { color: #8b5cf6; }

.item-content {
  flex: 1;
}

.item-title {
  font-size: 14px;
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 2px;
}

.item-subtitle {
  font-size: 12px;
  color: #6b7280;
}

.item-status {
  background: #ecfdf5;
  color: #10b981;
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 600;
}

.item-amount {
  color: #8b5cf6;
  font-size: 14px;
  font-weight: 700;
}

/* Facts Section */
.facts-section {
  margin-bottom: 24px;
}

.facts-title {
  font-size: 16px;
  font-weight: 700;
  color: #1f2937;
  margin: 0 0 16px 0;
}

.facts-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
}

.fact-item {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  padding: 12px;
  background: #f9fafb;
  border-radius: 8px;
  border: 1px solid #e5e7eb;
}

.fact-icon {
  font-size: 16px;
  width: 20px;
  height: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.fact-content {
  flex: 1;
}

.fact-label {
  font-size: 12px;
  color: #6b7280;
  margin-bottom: 2px;
}

.fact-value {
  font-size: 18px;
  font-weight: 700;
  color: #1f2937;
  margin-bottom: 2px;
}

.fact-desc {
  font-size: 11px;
  color: #9ca3af;
}

/* Expandable Sections */
.expandable-sections {
  margin-bottom: 24px;
}

.expandable-item {
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  margin-bottom: 8px;
}

.expandable-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px 16px;
  cursor: pointer;
  font-size: 14px;
  font-weight: 500;
  color: #374151;
}

.expandable-header:hover {
  background: #f9fafb;
}

/* Advice Section */
.advice-section {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px;
  background: #f0f9ff;
  border-radius: 8px;
  border: 1px solid #e0f2fe;
}

.advice-content {
  flex: 1;
}

.advice-text {
  font-size: 14px;
  font-weight: 600;
  color: #1f2937;
  margin: 0 0 4px 0;
}

.advice-subtext {
  font-size: 12px;
  color: #6b7280;
  margin: 0;
}

.advice-btn {
  background: #4f46e5;
  color: white;
  border: none;
  padding: 8px 16px;
  border-radius: 6px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
}

.advice-btn:hover {
  background: #4338ca;
}

/* Resources Section */
.resources-section {
  max-width: 1200px;
  margin: 0 auto;
  padding: 60px 24px 40px;
}

.resources-title {
  font-size: 24px;
  font-weight: 700;
  color: #1f2937;
  text-align: center;
  margin: 0 0 40px 0;
}

.resources-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 32px;
}

.resource-item {
  text-align: center;
  padding: 32px 24px;
  background: white;
  border-radius: 16px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
  border: 1px solid #e5e7eb;
}

.resource-icon {
  width: 48px;
  height: 48px;
  margin: 0 auto 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 24px;
  border-radius: 12px;
}

.resource-icon.blue { background: #eff6ff; color: #2563eb; }
.resource-icon.green { background: #f0fdf4; color: #16a34a; }
.resource-icon.purple { background: #faf5ff; color: #a855f7; }

.resource-title {
  font-size: 18px;
  font-weight: 700;
  color: #1f2937;
  margin: 0 0 8px 0;
}

.resource-desc {
  font-size: 14px;
  color: #6b7280;
  margin: 0;
}

/* Responsive */
@media (max-width: 768px) {
  .main-content {
    grid-template-columns: 1fr;
    gap: 24px;
  }
  
  .resources-grid {
    grid-template-columns: 1fr;
    gap: 24px;
  }
  
  .facts-grid {
    grid-template-columns: 1fr;
  }
  
  .tax-breakdown {
    grid-template-columns: 1fr;
  }
}
</style>