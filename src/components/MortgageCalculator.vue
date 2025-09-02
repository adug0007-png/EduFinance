
<template>
  <section class="mortgage-calculator">
    <div class="main-content">
      <div class="calculator-card">
        <h2 class="form-title">Enter Loan Details</h2>
        
        <div class="form-field">
          <label class="field-label">Loan Amount</label>
          <div class="input-container">
            <span class="input-prefix">$</span>
            <input 
              v-model="loanAmount" 
              type="text" 
              class="form-input" 
              placeholder="500,000"
            />
          </div>
        </div>

        <div class="form-row">
          <div class="form-field">
            <label class="field-label">Annual Interest Rate</label>
            <div class="input-container">
              <input 
                v-model="interestRate" 
                type="text" 
                class="form-input" 
                placeholder="3.75"
              />
              <span class="input-suffix">%</span>
            </div>
          </div>
          
          <div class="form-field">
            <label class="field-label">Loan Term</label>
            <div class="input-container">
              <input 
                v-model="loanTerm" 
                type="text" 
                class="form-input" 
                placeholder="30"
              />
              <span class="input-suffix">years</span>
            </div>
          </div>
        </div>

        <button class="calculate-button" @click="calculatePayment">
          Calculate
        </button>
      </div>
    </div>

    <!-- Result Modal -->
    <div v-if="showModal" class="modal-overlay" @click="closeModal">
      <div class="modal-content" @click.stop>
        <div class="modal-header">
          <h3 class="modal-title">Calculation Results</h3>
          <button class="close-button" @click="closeModal">×</button>
        </div>
        <div class="modal-body">
          <div class="result-item">
            <span class="result-label">Monthly Payment:</span>
            <span class="result-value">${{ formatNumber(monthlyPayment) }}</span>
          </div>
          <div class="result-item">
            <span class="result-label">Total Payment:</span>
            <span class="result-value">${{ formatNumber(totalPayment) }}</span>
          </div>
          <div class="result-item">
            <span class="result-label">Total Interest:</span>
            <span class="result-value">${{ formatNumber(totalInterest) }}</span>
          </div>
        </div>
        <div class="modal-footer">
          <button class="modal-button" @click="closeModal">OK</button>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'MortgageCalculator',
  data() {
    return {
      loanAmount: '500,000',
      interestRate: '3.75',
      loanTerm: '30',
      monthlyPayment: null,
      totalPayment: null,
      totalInterest: null,
      showModal: false
    }
  },
  methods: {
    calculatePayment() {
      const principal = parseFloat(this.loanAmount.replace(/,/g, ''))
      const rate = parseFloat(this.interestRate) / 100 / 12
      const payments = parseFloat(this.loanTerm) * 12
      
      if (principal && rate && payments) {
        const monthlyPayment = principal * (rate * Math.pow(1 + rate, payments)) / (Math.pow(1 + rate, payments) - 1)
        this.monthlyPayment = monthlyPayment.toFixed(2)
        this.totalPayment = (monthlyPayment * payments).toFixed(2)
        this.totalInterest = (this.totalPayment - principal).toFixed(2)
        this.showModal = true
      }
    },
    closeModal() {
      this.showModal = false
    },
    formatNumber(value) {
      if (!value) return '0'
      return parseFloat(value).toLocaleString('en-US', {
        minimumFractionDigits: 2,
        maximumFractionDigits: 2
      })
    }
  }
}
</script>

<style scoped>
.mortgage-calculator {
  background-color: #f8fafc;
  min-height: calc(100vh - 64px);
  display: flex;
  flex-direction: column;
}

.main-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 40px 24px;
  display: flex;
  justify-content: flex-start;
  flex: 1;
}

.calculator-card {
  background: white;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  padding: 24px;
  width: 380px;
  min-width: 380px;
  max-width: 380px;
  height: 400px;
  min-height: 400px;
  max-height: 400px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.form-title {
  font-size: 18px;
  font-weight: 600;
  color: #111827;
  margin: 0 0 20px 0;
}

.form-field {
  margin-bottom: 16px;
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
  margin-bottom: 20px;
}

.field-label {
  display: block;
  font-size: 14px;
  font-weight: 500;
  color: #6b7280;
  margin-bottom: 8px;
}

.input-container {
  position: relative;
  display: flex;
  align-items: center;
}

.form-input {
  width: 100%;
  height: 44px;
  padding: 0 12px;
  border: 1px solid #d1d5db;
  border-radius: 6px;
  font-size: 16px;
  color: #111827;
  background: white;
  outline: none;
  transition: border-color 0.2s, box-shadow 0.2s;
}

.form-input::placeholder {
  color: #9ca3af;
}

.form-input:focus {
  border-color: #3b82f6;
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}

.input-prefix {
  position: absolute;
  left: 12px;
  color: #6b7280;
  font-size: 16px;
  pointer-events: none;
}

.input-suffix {
  position: absolute;
  right: 12px;
  color: #6b7280;
  font-size: 16px;
  pointer-events: none;
}

.input-container .input-prefix + .form-input {
  padding-left: 32px;
}

.input-container .form-input:has(+ .input-suffix) {
  padding-right: 50px;
}

.calculate-button {
  width: 100%;
  height: 48px;
  background: #4f46e5;
  color: white;
  border: none;
  border-radius: 6px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: background-color 0.2s;
  margin-top: 8px;
}

.calculate-button:hover {
  background: #4338ca;
}

.calculate-button:active {
  background: #3730a3;
}

.page-footer {
  background: #374151;
  margin-top: auto;
}

.footer-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px 24px;
  text-align: center;
  color: #9ca3af;
  font-size: 14px;
}

/* Modal Styles */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.modal-content {
  background: white;
  border-radius: 12px;
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
  max-width: 500px;
  width: 90%;
  max-height: 90vh;
  overflow: hidden;
}

.modal-header {
  padding: 24px 24px 0 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.modal-title {
  font-size: 20px;
  font-weight: 600;
  color: #111827;
  margin: 0;
}

.close-button {
  background: none;
  border: none;
  font-size: 24px;
  color: #6b7280;
  cursor: pointer;
  padding: 4px;
  line-height: 1;
  transition: color 0.2s;
}

.close-button:hover {
  color: #374151;
}

.modal-body {
  padding: 24px;
}

.result-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px 0;
  border-bottom: 1px solid #f3f4f6;
}

.result-item:last-child {
  border-bottom: none;
}

.result-label {
  font-size: 16px;
  color: #374151;
  font-weight: 500;
}

.result-value {
  font-size: 18px;
  font-weight: 600;
  color: #059669;
}

.modal-footer {
  padding: 0 24px 24px 24px;
}

.modal-button {
  width: 100%;
  height: 44px;
  background: #4f46e5;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: background-color 0.2s;
}

.modal-button:hover {
  background: #4338ca;
}
</style>