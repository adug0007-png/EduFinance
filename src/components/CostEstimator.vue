<template>
  <div class="education-cost-estimator">
    <!-- Main Content -->
    <div class="main-content">
      <div class="estimator-container">
        <!-- Left Side - Education Details Card -->
        <div class="card education-details-card">
          <h2 class="section-title">Education Details</h2>
          
          <div class="form-group">
            <label class="form-label">Education Level</label>
            <div class="select-container">
              <select v-model="educationLevel" class="form-select">
                <option value="">Select Education Level</option>
                <option value="undergraduate">Undergraduate Degree</option>
                <option value="graduate">Graduate Degree</option>
                <option value="doctorate">Doctorate Degree</option>
                <option value="certificate">Certificate Program</option>
                <option value="diploma">Diploma</option>
              </select>
              <svg class="select-icon" width="16" height="16" viewBox="0 0 24 24" fill="none">
                <path d="M6 9L12 15L18 9" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </div>
          </div>

          <div class="form-group">
            <label class="form-label">Duration (Years)</label>
            <div class="select-container">
              <select v-model="duration" class="form-select">
                <option value="">Select Duration</option>
                <option value="1">1 Year</option>
                <option value="2">2 Years</option>
                <option value="3">3 Years</option>
                <option value="4">4 Years</option>
                <option value="5">5 Years</option>
                <option value="6">6 Years</option>
              </select>
              <svg class="select-icon" width="16" height="16" viewBox="0 0 24 24" fill="none">
                <path d="M6 9L12 15L18 9" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </div>
          </div>

          <div class="form-group">
            <label class="form-label">Location</label>
            <div class="input-container">
              <svg class="input-icon" width="16" height="16" viewBox="0 0 24 24" fill="none">
                <circle cx="11" cy="11" r="8" stroke="currentColor" stroke-width="2"/>
                <path d="M21 21L16.65 16.65" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              <input 
                type="text" 
                v-model="location" 
                placeholder="Enter country or city" 
                class="form-input"
              />
            </div>
          </div>

          <div class="form-group">
            <label class="form-label">Living Style</label>
            <div class="radio-group">
              <label class="radio-option">
                <input type="radio" v-model="livingStyle" value="on-campus" name="living-style">
                <span class="radio-custom"></span>
                <span class="radio-label">On-campus Housing</span>
              </label>
              <label class="radio-option">
                <input type="radio" v-model="livingStyle" value="off-campus" name="living-style">
                <span class="radio-custom"></span>
                <span class="radio-label">Off-campus Rental</span>
              </label>
              <label class="radio-option">
                <input type="radio" v-model="livingStyle" value="family" name="living-style">
                <span class="radio-custom"></span>
                <span class="radio-label">Living with Family</span>
              </label>
            </div>
          </div>

          <button class="calculate-btn" @click="calculateCosts">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none">
              <path d="M9 11H15M9 15H15M17 21H7C5.89543 21 5 20.1046 5 19V5C5 3.89543 5.89543 3 7 3H12.5858C12.851 3 13.1054 3.10536 13.2929 3.29289L19.7071 9.70711C19.8946 9.89464 20 10.149 20 10.4142V19C20 20.1046 19.1046 21 18 21H17Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            Calculate Costs
          </button>
        </div>

        <!-- Right Side - Cost Breakdown Card -->
        <div class="card cost-breakdown-card">
          <h2 class="section-title">Cost Breakdown</h2>
          
          <div class="results-content">
            <div v-if="!hasCalculated" class="empty-state">
              <div class="pie-chart-placeholder">
                <svg width="120" height="120" viewBox="0 0 120 120">
                  <circle cx="60" cy="60" r="50" fill="none" stroke="#e5e7eb" stroke-width="8"/>
                  <circle cx="60" cy="60" r="50" fill="none" stroke="#6366f1" stroke-width="8" 
                          stroke-dasharray="94 314" stroke-dashoffset="0" transform="rotate(-90 60 60)"/>
                </svg>
              </div>
              <p class="empty-message">Fill out the form to see your cost estimate</p>
            </div>
            
            <div v-else class="cost-results">
              <div class="pie-chart">
                <canvas ref="chartCanvas" width="200" height="200"></canvas>
              </div>
              
              <div class="cost-breakdown">
                <div class="cost-item" v-for="item in costBreakdown" :key="item.category">
                  <div class="cost-indicator" :style="{ backgroundColor: item.color }"></div>
                  <div class="cost-details">
                    <span class="cost-category">{{ item.category }}</span>
                    <span class="cost-amount">${{ formatNumber(item.amount) }}</span>
                  </div>
                </div>
              </div>
              
              <div class="total-cost">
                <div class="total-label">Total Estimated Cost</div>
                <div class="total-amount">${{ formatNumber(totalCost) }}</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CostEstimator',
  data() {
    return {
      educationLevel: '',
      duration: '',
      location: '',
      livingStyle: '',
      hasCalculated: false,
      totalCost: 0,
      costBreakdown: []
    }
  },
  methods: {
    calculateCosts() {
      if (!this.educationLevel || !this.duration || !this.location || !this.livingStyle) {
        alert('Please fill in all required fields');
        return;
      }
      
      // Calculate costs based on inputs
      const baseTuition = this.getBaseTuition();
      const livingCosts = this.getLivingCosts();
      const booksCosts = baseTuition * 0.1; // 10% of tuition
      const miscCosts = baseTuition * 0.05; // 5% of tuition
      
      this.costBreakdown = [
        { category: 'Tuition & Fees', amount: baseTuition, color: '#6366f1' },
        { category: 'Living Expenses', amount: livingCosts, color: '#8b5cf6' },
        { category: 'Books & Supplies', amount: booksCosts, color: '#06b6d4' },
        { category: 'Personal & Misc', amount: miscCosts, color: '#10b981' }
      ];
      
      this.totalCost = baseTuition + livingCosts + booksCosts + miscCosts;
      this.hasCalculated = true;
      
      this.$nextTick(() => {
        this.drawPieChart();
      });
    },
    
    getBaseTuition() {
      const levelMultipliers = {
        'undergraduate': 1.0,
        'graduate': 1.5,
        'doctorate': 2.0,
        'certificate': 0.5,
        'diploma': 0.7
      };
      
      const baseCost = 25000; // Base annual tuition
      const years = parseInt(this.duration);
      const multiplier = levelMultipliers[this.educationLevel] || 1.0;
      
      return baseCost * years * multiplier;
    },
    
    getLivingCosts() {
      const styleMultipliers = {
        'on-campus': 15000,
        'off-campus': 18000,
        'family': 5000
      };
      
      const years = parseInt(this.duration);
      const annualCost = styleMultipliers[this.livingStyle] || 15000;
      
      return annualCost * years;
    },
    
    drawPieChart() {
      const canvas = this.$refs.chartCanvas;
      if (!canvas) return;
      
      const ctx = canvas.getContext('2d');
      const centerX = 100;
      const centerY = 100;
      const radius = 80;
      
      ctx.clearRect(0, 0, 200, 200);
      
      let currentAngle = -Math.PI / 2;
      
      this.costBreakdown.forEach(item => {
        const sliceAngle = (item.amount / this.totalCost) * 2 * Math.PI;
        
        ctx.beginPath();
        ctx.moveTo(centerX, centerY);
        ctx.arc(centerX, centerY, radius, currentAngle, currentAngle + sliceAngle);
        ctx.closePath();
        ctx.fillStyle = item.color;
        ctx.fill();
        
        currentAngle += sliceAngle;
      });
    },
    
    formatNumber(num) {
      return Math.round(num || 0).toLocaleString();
    }
  }
}
</script>

<style scoped>
.education-cost-estimator {
  min-height: 100vh;
  background: #f8fafc;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}

/* Header Section */
.header-section {
  background: white;
  padding: 40px 0;
  text-align: center;
}

.header-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 24px;
}

.page-title {
  font-size: 48px;
  font-weight: 700;
  color: #4f46e5;
  margin: 0 0 12px 0;
}

.page-subtitle {
  font-size: 18px;
  color: #6b7280;
  margin: 0;
}

/* Main Content */
.main-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 40px 24px;
}

.estimator-container {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 40px;
}

/* Card Styles */
.card {
  background: white;
  border-radius: 16px;
  padding: 32px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
  border: 1px solid #e5e7eb;
}

.education-details-card {
  display: flex;
  flex-direction: column;
}

.cost-breakdown-card {
  display: flex;
  flex-direction: column;
}

/* Form Section */
.form-section {
  display: flex;
  flex-direction: column;
}

.section-title {
  font-size: 24px;
  font-weight: 700;
  color: #1f2937;
  margin: 0 0 32px 0;
}

.form-group {
  margin-bottom: 24px;
}

.form-label {
  display: block;
  font-size: 16px;
  font-weight: 600;
  color: #374151;
  margin-bottom: 8px;
}

.select-container {
  position: relative;
}

.form-select {
  width: 100%;
  height: 48px;
  padding: 0 40px 0 16px;
  border: 2px solid #e5e7eb;
  border-radius: 8px;
  font-size: 16px;
  background: white;
  appearance: none;
  cursor: pointer;
  box-sizing: border-box;
}

.form-select:focus {
  outline: none;
  border-color: #4f46e5;
  box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.1);
}

.select-icon {
  position: absolute;
  right: 12px;
  top: 50%;
  transform: translateY(-50%);
  color: #9ca3af;
  pointer-events: none;
}

.input-container {
  position: relative;
}

.form-input {
  width: 100%;
  height: 48px;
  padding: 0 16px 0 40px;
  border: 2px solid #e5e7eb;
  border-radius: 8px;
  font-size: 16px;
  background: white;
  box-sizing: border-box;
}

.form-input:focus {
  outline: none;
  border-color: #4f46e5;
  box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.1);
}

.input-icon {
  position: absolute;
  left: 12px;
  top: 50%;
  transform: translateY(-50%);
  color: #9ca3af;
}

.radio-group {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.radio-option {
  display: flex;
  align-items: center;
  gap: 12px;
  cursor: pointer;
}

.radio-option input[type="radio"] {
  display: none;
}

.radio-custom {
  width: 20px;
  height: 20px;
  border: 2px solid #d1d5db;
  border-radius: 50%;
  position: relative;
  transition: all 0.2s;
}

.radio-option input[type="radio"]:checked + .radio-custom {
  border-color: #4f46e5;
  background: #4f46e5;
}

.radio-option input[type="radio"]:checked + .radio-custom::after {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 8px;
  height: 8px;
  background: white;
  border-radius: 50%;
}

.radio-label {
  font-size: 16px;
  color: #374151;
}

.calculate-btn {
  width: 100%;
  height: 52px;
  background: #4f46e5;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  margin-top: auto;
  transition: background-color 0.2s;
}

.calculate-btn:hover {
  background: #4338ca;
}

/* Results Section */
.results-section {
  display: flex;
  flex-direction: column;
}

.results-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.empty-state {
  text-align: center;
}

.pie-chart-placeholder {
  margin-bottom: 24px;
}

.empty-message {
  font-size: 16px;
  color: #9ca3af;
  margin: 0;
}

.cost-results {
  width: 100%;
  text-align: center;
}

.pie-chart {
  margin-bottom: 32px;
  display: flex;
  justify-content: center;
}

.cost-breakdown {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-bottom: 24px;
}

.cost-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 8px 0;
}

.cost-indicator {
  width: 16px;
  height: 16px;
  border-radius: 50%;
}

.cost-details {
  display: flex;
  justify-content: space-between;
  width: 100%;
}

.cost-category {
  font-size: 14px;
  color: #6b7280;
}

.cost-amount {
  font-size: 14px;
  font-weight: 600;
  color: #1f2937;
}

.total-cost {
  padding: 20px;
  background: #f3f4f6;
  border-radius: 8px;
  text-align: center;
}

.total-label {
  font-size: 14px;
  color: #6b7280;
  margin-bottom: 8px;
}

.total-amount {
  font-size: 32px;
  font-weight: 700;
  color: #1f2937;
}

@media (max-width: 768px) {
  .page-title {
    font-size: 36px;
  }
  
  .estimator-container {
    grid-template-columns: 1fr;
    gap: 32px;
  }
  
  .card {
    padding: 24px;
  }
}
</style>