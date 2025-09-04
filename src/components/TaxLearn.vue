<template>
  <div class="tax-learn">
    <!-- Main Content -->
    <div class="main-content">
      <!-- Left Column - Salary Calculator -->
      <div class="left-column">
        <div class="calculator-card">
          <div class="card-header">
            <h2 class="card-title">Salary Calculator</h2>
            <button class="refresh-btn"></button>
          </div>
          <p class="card-subtitle">Click the button to see your take-home pay</p>

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

          <button class="calculate-btn" @click="calculateTax">Calculate Take-Home Pay</button>

          <div class="breakdown-section">
            <h3 class="breakdown-title">Your Breakdown</h3>
            <div class="salary-display">
              <div class="salary-label">Gross Salary</div>
              <div class="salary-amount">${{ formatNumber(parseFloat(grossSalary.replace(/,/g, '')) || 0) }}</div>
              <div class="progress-bar">
                <div class="progress-fill"></div>
              </div>
            </div>

            <div class="tax-breakdown">
              <div class="tax-item income-tax">
                <div class="tax-color red"></div>
                <div class="tax-info">
                  <div class="tax-name">Income Tax</div>
                  <div class="tax-amount">${{ formatNumber(calculatedResults.incomeTax) }}</div>
                  <div class="tax-period">per year</div>
                </div>
              </div>
              <div class="tax-item medicare">
                <div class="tax-color orange"></div>
                <div class="tax-info">
                  <div class="tax-name">Medicare Levy</div>
                  <div class="tax-amount">${{ formatNumber(calculatedResults.medicareLevy) }}</div>
                  <div class="tax-period">per year</div>
                </div>
              </div>
              <div class="tax-item net-pay">
                <div class="tax-color green"></div>
                <div class="tax-info">
                  <div class="tax-name">Net Pay</div>
                  <div class="tax-amount">${{ formatNumber(calculatedResults.netPay) }}</div>
                  <div class="tax-period">per year</div>
                </div>
              </div>
              <div class="tax-item super">
                <div class="tax-color blue"></div>
                <div class="tax-info">
                  <div class="tax-name">Superannuation (11.5%)</div>
                  <div class="tax-amount">${{ formatNumber(calculatedResults.superannuation) }}</div>
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
            <h2 class="section-title">Financial Terms Cards</h2>
            <div class="nav-arrows">
              <button class="arrow-btn" @click="prevCard">◀</button>
              <button class="arrow-btn" @click="nextCard">▶</button>
            </div>
          </div>
          <p class="section-subtitle">Learn financial terms and definitions</p>

          <!-- Dynamic Term Card -->
          <div class="concept-card">
            <div class="concept-header">
              <h3 class="concept-title">{{ getCurrentTerm().term }}</h3>
              <span class="concept-count">{{ currentCardIndex + 1 }}/{{ taxTerms.length }}</span>
            </div>
            
            <div class="concept-content">
              <p class="concept-text">
                {{ getCurrentTerm().definition }}
              </p>
              <div class="category-badge" :class="getCategoryColor(getCurrentTerm().category)">
                {{ getCurrentTerm().category }}
              </div>
            </div>

            <!-- Navigation hints -->
            <div class="navigation-hints">
        <button
          type="button"
          class="hint-link"
          @click="prevCard"
          :disabled="atStart"
          aria-label="Previous term"
        >
          <span class="hint-icon">◀</span>
          <span class="hint-text">Previous term</span>
        </button>

        <button
          type="button"
          class="hint-link"
          @click="nextCard"
          :disabled="atEnd"
          aria-label="Next term"
        >
          <span class="hint-text">Next term</span>
          <span class="hint-icon">▶</span>
        </button>
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
          <!-- <div class="expandable-sections">
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
          </div> -->

          <!-- Get Advice Section
          <div class="advice-section">
            <div class="advice-content">
              <p class="advice-text">Ready to optimize your super?</p>
              <p class="advice-subtext">Get personalized advice from our experts</p>
            </div>
            <button class="advice-btn">Get Advice</button>
          </div> -->
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
      state: 'NSW',
      calculatedResults: {
        incomeTax: 0,
        medicareLevy: 0,
        netPay: 0,
        superannuation: 0
      },
      currentCardIndex: 0,
      taxTerms: [
        {
          term: "Non-concessional contribution",
          definition: "After-tax contribution to super.",
          category: "Superannuation"
        },
        {
          term: "Preservation age",
          definition: "Earliest age you can access super.",
          category: "Superannuation"
        },
        {
          term: "BSB",
          definition: "Bank routing number used with account number.",
          category: "Banking & payments"
        },
        {
          term: "Account number",
          definition: "Your unique banking account identifier.",
          category: "Banking & payments"
        },
        {
          term: "PayID/Osko",
          definition: "Fast payments using email/phone as an identifier.",
          category: "Banking & payments"
        },
        {
          term: "Debit card",
          definition: "Spends money from your bank account.",
          category: "Banking & payments"
        },
        {
          term: "Credit card",
          definition: "Borrows money up to a limit.",
          category: "Interest not repaid"
        },
        {
          term: "Direct debit",
          definition: "Merchant automatically debits money from your account.",
          category: "Banking & payments"
        },
        {
          term: "BPAY",
          definition: "Bill payment method via your online banking.",
          category: "Banking & payments"
        },
        {
          term: "Overdraft",
          definition: "Bank allows negative balance.",
          category: "fees/interest apply"
        },
        {
          term: "Chargeback",
          definition: "Ask bank to reverse a card charge for issues/scams.",
          category: "Banking & payments"
        },
        {
          term: "Budget",
          definition: "Plan of income vs spending and saving.",
          category: "Budgeting"
        },
        {
          term: "Needs vs Wants",
          definition: "Essentials (needs) vs optional (wants) spending.",
          category: "Budgeting"
        },
        {
          term: "50/30/20 rule",
          definition: "Guide: 50% needs, 30% wants, 20% saving/debt.",
          category: "Budgeting"
        },
        {
          term: "Fixed cost",
          definition: "Expenses that stays the same (e.g. rent).",
          category: "Budgeting"
        },
        {
          term: "Variable cost",
          definition: "Expense that changes (e.g. food, transport).",
          category: "Budgeting"
        },
        {
          term: "Emergency fund",
          definition: "Cash buffer for unexpected expenses.",
          category: "Budgeting"
        },
        {
          term: "Sinking fund",
          definition: "Savings set aside for known future expenses.",
          category: "Budgeting"
        },
        {
          term: "Interest",
          definition: "Cost of borrowing money, or savings, expressed as a rate.",
          category: "Saving & investing"
        },
        {
          term: "Compound interest",
          definition: "Interest earned on interest.",
          category: "snowball effect"
        },
        {
          term: "Term deposit",
          definition: "Locked savings at a set rate at a fixed return.",
          category: "Saving & investing"
        },
        {
          term: "ETF (Exchange-Traded Fund)",
          definition: "A basket of assets you can buy like a share.",
          category: "Saving & investing"
        },
        {
          term: "Index fund",
          definition: "Fund that tracks a market index (e.g. ASX 200).",
          category: "Saving & investing"
        },
        {
          term: "Diversification",
          definition: "Spread money across assets to reduce risk.",
          category: "Saving & investing"
        },
        {
          term: "Risk vs return",
          definition: "Higher potential returns usually mean higher risk.",
          category: "Saving & investing"
        },
        {
          term: "Credit score",
          definition: "Number summarising how risky you are to lend to.",
          category: "Credit & debt"
        },
        {
          term: "Credit report",
          definition: "Your credit history: loans, cards, repayments.",
          category: "Credit & debt"
        },
        {
          term: "Interest rate (APR)",
          definition: "Yearly cost of a loan/card (often promo rate).",
          category: "Credit & debt"
        },
        {
          term: "Minimum repayment",
          definition: "Smallest amount you must pay each period.",
          category: "Credit & debt"
        },
        {
          term: "Balance transfer",
          definition: "Move card debt to a new card (often promo rate).",
          category: "Credit & debt"
        },
        {
          term: "BNPL (Buy Now, Pay Later)",
          definition: "Pay in instalments.",
          category: "fees for late/missed payments"
        },
        {
          term: "Late fee",
          definition: "Charge for missing a payment deadline.",
          category: "Credit & debt"
        },
        {
          term: "Default",
          definition: "Serious missed payment recorded on your credit file.",
          category: "Credit & debt"
        },
        {
          term: "Debt-to-income ratio (DTI)",
          definition: "How much debt vs income - key for home loans.",
          category: "Credit & debt"
        }
      ]
    }
  },
  methods: {
    calculateTax() {
      const salary = parseFloat(this.grossSalary.replace(/,/g, '')) || 0
      
      // Australian tax brackets for 2023-24
      let incomeTax = 0
      if (salary > 18200) {
        if (salary <= 45000) {
          incomeTax = (salary - 18200) * 0.19
        } else if (salary <= 120000) {
          incomeTax = 5092 + (salary - 45000) * 0.325
        } else if (salary <= 180000) {
          incomeTax = 29467 + (salary - 120000) * 0.37
        } else {
          incomeTax = 51667 + (salary - 180000) * 0.45
        }
      }
      
      // Medicare levy (2%)
      const medicareLevy = salary * 0.02
      
      // Superannuation (11.5%)
      const superannuation = salary * 0.115
      
      // Net pay
      const netPay = salary - incomeTax - medicareLevy
      
      this.calculatedResults = {
        incomeTax: Math.round(incomeTax),
        medicareLevy: Math.round(medicareLevy),
        netPay: Math.round(netPay),
        superannuation: Math.round(superannuation)
      }
    },
    formatNumber(num) {
      return num.toLocaleString()
    },
    nextCard() {
      this.currentCardIndex = (this.currentCardIndex + 1) % this.taxTerms.length
    },
    prevCard() {
      this.currentCardIndex = this.currentCardIndex === 0 ? this.taxTerms.length - 1 : this.currentCardIndex - 1
    },
    getCurrentTerm() {
      return this.taxTerms[this.currentCardIndex]
    },
    getCategoryColor(category) {
      const colors = {
        'Superannuation': 'blue',
        'Banking & payments': 'green', 
        'Budgeting': 'purple',
        'Saving & investing': 'orange',
        'Credit & debt': 'red',
        'Interest not repaid': 'red',
        'fees/interest apply': 'red',
        'snowball effect': 'orange',
        'fees for late/missed payments': 'red'
      }
      return colors[category] || 'gray'
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
  align-items: stretch;
}

.left-column,
.right-column {
  display: flex;
  flex-direction: column;
}


/* Left Column - Calculator */
.calculator-card {
  background: white;
  border-radius: 16px;
  padding: 24px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
  border: 1px solid #e5e7eb;
  height: fit-content;
  flex: 1 1 auto;
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

.navigation-hints {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 12px;
  padding-top: 12px;
  border-top: 1px solid var(--border-color, #e5e7eb);
}

.hint-link {
  background: transparent;
  border: 0;
  padding: 6px 0;
  color: #6B7280;
  font-weight: 600;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  cursor: pointer;
}

.hint-link:hover:not(:disabled) { color: var(--primary-color, #4F46E5); }
.hint-link:disabled { opacity: .45; cursor: not-allowed; }

.arrow-btn:disabled { opacity: .45; cursor: not-allowed; }


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

.category-badge {
  display: inline-block;
  padding: 4px 12px;
  border-radius: 12px;
  font-size: 12px;
  font-weight: 600;
  margin-top: 12px;
}

.category-badge.blue {
  background: #eff6ff;
  color: #2563eb;
}

.category-badge.green {
  background: #f0fdf4;
  color: #16a34a;
}

.category-badge.purple {
  background: #faf5ff;
  color: #a855f7;
}

.category-badge.orange {
  background: #fff7ed;
  color: #ea580c;
}

.category-badge.red {
  background: #fef2f2;
  color: #dc2626;
}

.category-badge.gray {
  background: #f9fafb;
  color: #6b7280;
}

.navigation-hints {
  display: flex;
  justify-content: space-between;
  margin-top: 16px;
  padding-top: 16px;
  border-top: 1px solid #e5e7eb;
}

.hint-item {
  display: flex;
  align-items: center;
  gap: 6px;
  color: #6b7280;
  font-size: 12px;
}

.hint-icon {
  font-size: 14px;
  color: #9ca3af;
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
  grid-template-columns: 1fr;
  gap: 16px;
}

.fact-item {
  display: grid;
  align-items: flex-start;
  grid-template-columns: 28px 1fr;
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
  grid-column: 1;
  align-self: start;
}

.fact-content {
  grid-column: 2;
  display: grid;
  grid-template-columns: 1fr auto; /* text | value */
  column-gap: 24px;
  row-gap: 2px;
  align-items: center;
}

.fact-label {
  font-size: 12px;
  color: black;
  margin-bottom: 2px;
  grid-column: 1;
  grid-row: 1;

}

.fact-value {
  grid-column: 2; 
  grid-row: 1 / span 2;     /* span both rows */
  justify-self: end;         /* align to the right */
  font-size: 18px;           /* keep your current size or bump up */
  font-weight: 700;
  color: black
}

.fact-desc {
  font-size: 11px;
  color: #000;
  grid-column: 1;
  grid-row: 2;
}

.facts-grid .fact-card,
.facts-grid .fact-item {
  width: 100%;
  box-sizing: border-box;
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

@media (max-width: 480px) {
  .fact-content { grid-template-columns: 1fr; }
  .fact-value   { grid-column: 1; grid-row: 3; justify-self: start; }
}

</style>