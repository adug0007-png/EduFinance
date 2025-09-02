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
        <div v-for="module in modules" :key="module.id" class="module-card">
          <div class="module-image">
            <div class="video-thumbnail" :style="{ backgroundImage: `url(https://img.youtube.com/vi/${module.videoId}/maxresdefault.jpg)` }">
              <div class="play-overlay">
                <div class="play-button">▶</div>
              </div>
            </div>
          </div>
          <div class="module-content">
            <h3 class="module-title">{{ module.title }}</h3>
            <div class="module-rating">
              <div class="stars">
                <span 
                  v-for="i in 5" 
                  :key="i" 
                  class="star" 
                  :class="{ 'filled': i <= getStarRating(module.rating).fullStars }"
                >★</span>
              </div>
              <span class="rating-value">{{ module.rating.toFixed(1) }}</span>
            </div>
            <p class="module-description">
              {{ module.description }}
            </p>
            <div class="module-meta">
              <span class="duration">⏱ {{ module.duration }}</span>
              <span class="difficulty" :class="module.difficulty.toLowerCase()">{{ module.difficulty }}</span>
            </div>
            <button class="start-learning-btn" @click="startLearning(module)">Start Learning</button>
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

    <!-- Video Player Modal -->
    <div v-if="showVideoPlayer" class="video-modal" @click="closeVideoPlayer">
      <div class="video-modal-content" @click.stop>
        <div class="video-header">
          <h3 class="video-title">{{ selectedModule?.title }}</h3>
          <button class="close-btn" @click="closeVideoPlayer">✕</button>
        </div>
        <div class="video-container">
          <iframe
            v-if="selectedModule"
            :src="`https://www.youtube.com/embed/${selectedModule.videoId}?autoplay=1&rel=0`"
            frameborder="0"
            allow="autoplay; encrypted-media"
            allowfullscreen
            class="video-player"
          ></iframe>
        </div>
        <div class="video-info">
          <p class="video-description">{{ selectedModule?.description }}</p>
          <div class="video-meta">
            <span class="video-duration">⏱ {{ selectedModule?.duration }}</span>
            <span class="video-difficulty" :class="selectedModule?.difficulty.toLowerCase()">
              {{ selectedModule?.difficulty }}
            </span>
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
      searchQuery: '',
      selectedModule: null,
      showVideoPlayer: false,
      modules: [
        {
          id: 1,
          title: 'Understanding Inflation',
          description: 'Learn how inflation affects your purchasing power and investment decisions.',
          duration: '45 mins',
          difficulty: 'Easy',
          rating: 5.0,
          videoId: 'HQ-Kg_xgdhE',
          videoUrl: 'https://youtu.be/HQ-Kg_xgdhE?si=1AcfezQ0o7bLIPPr'
        },
        {
          id: 2,
          title: 'Smart Budgeting',
          description: 'Master the art of creating and maintaining effective personal budgets.',
          duration: '60 mins',
          difficulty: 'Easy',
          rating: 5.0,
          videoId: 'V59GNErtt48',
          videoUrl: 'https://youtu.be/V59GNErtt48?si=HndLVw50O31VOa1s'
        },
        {
          id: 3,
          title: 'Saving Strategies',
          description: 'Discover proven methods to build your emergency fund and savings goals.',
          duration: '50 mins',
          difficulty: 'Medium',
          rating: 4.0,
          videoId: 'JP__utZQLb8',
          videoUrl: 'https://youtu.be/JP__utZQLb8?si=KdNE0zdxbif-ghmu'
        },
        {
          id: 4,
          title: 'Credit Management',
          description: 'Build and maintain excellent credit while avoiding common pitfalls.',
          duration: '75 mins',
          difficulty: 'Medium',
          rating: 4.0,
          videoId: '1yPgUHsjUTc',
          videoUrl: 'https://youtu.be/1yPgUHsjUTc?si=4vV_pALwKLGKOPBg'
        },
        {
          id: 5,
          title: 'Investment Fundamentals',
          description: 'Start your investment journey with solid foundations and risk management.',
          duration: '90 mins',
          difficulty: 'Advanced',
          rating: 5.0,
          videoId: '3BOE1A8HXeE',
          videoUrl: 'https://youtu.be/3BOE1A8HXeE?si=z2N3aLLyfmHyUvw9'
        }
      ]
    }
  },
  methods: {
    startLearning(module) {
      this.selectedModule = module
      this.showVideoPlayer = true
    },
    closeVideoPlayer() {
      this.showVideoPlayer = false
      this.selectedModule = null
    },
    getStarRating(rating) {
      const fullStars = Math.floor(rating)
      const hasHalfStar = rating % 1 !== 0
      return { fullStars, hasHalfStar }
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
  position: relative;
}

.module-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.video-thumbnail {
  width: 100%;
  height: 100%;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  position: relative;
  cursor: pointer;
  transition: transform 0.2s;
}

.video-thumbnail:hover {
  transform: scale(1.02);
}

.play-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.3);
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.2s;
}

.video-thumbnail:hover .play-overlay {
  opacity: 1;
}

.play-button {
  width: 60px;
  height: 60px;
  background: rgba(255, 255, 255, 0.9);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 24px;
  color: #4f46e5;
  transition: transform 0.2s;
}

.play-button:hover {
  transform: scale(1.1);
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

/* Video Modal Styles */
.video-modal {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.8);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  padding: 20px;
}

.video-modal-content {
  background: white;
  border-radius: 12px;
  max-width: 900px;
  width: 100%;
  max-height: 90vh;
  overflow-y: auto;
  position: relative;
}

.video-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px 24px;
  border-bottom: 1px solid #e5e7eb;
}

.video-title {
  font-size: 20px;
  font-weight: 600;
  color: #111827;
  margin: 0;
}

.close-btn {
  background: none;
  border: none;
  font-size: 20px;
  color: #6b7280;
  cursor: pointer;
  padding: 4px;
  border-radius: 4px;
}

.close-btn:hover {
  background: #f3f4f6;
  color: #374151;
}

.video-container {
  position: relative;
  width: 100%;
  height: 0;
  padding-bottom: 56.25%; /* 16:9 aspect ratio */
  background: #000;
}

.video-player {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.video-info {
  padding: 24px;
}

.video-description {
  font-size: 16px;
  color: #374151;
  line-height: 1.6;
  margin: 0 0 16px 0;
}

.video-meta {
  display: flex;
  align-items: center;
  gap: 16px;
  font-size: 14px;
}

.video-duration {
  color: #6b7280;
}

.video-difficulty {
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 12px;
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
  
  .video-modal {
    padding: 10px;
  }
  
  .video-modal-content {
    max-height: 95vh;
  }
  
  .video-header {
    padding: 16px;
  }
  
  .video-info {
    padding: 16px;
  }
}
</style>