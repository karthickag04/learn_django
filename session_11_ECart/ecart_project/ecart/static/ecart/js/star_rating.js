/**
 * Interactive Star Rating System
 * Author: ECart Development Team
 * Purpose: Provide interactive star rating for product reviews
 */

document.addEventListener('DOMContentLoaded', function() {
    
    // ============================================
    // 1. SELECT DOM ELEMENTS
    // ============================================
    
    const starRatingContainer = document.querySelector('.star-rating');
    console.log('Star Rating Container:', starRatingContainer);
    
    // Exit if star rating container doesn't exist (not on review page)
    if (!starRatingContainer) {
        return;
    }
    
    const stars = document.querySelectorAll('.star');
    console.log('Stars found:', stars);
    const ratingInput = document.getElementById('rating-input');
    let currentRating = parseInt(starRatingContainer.dataset.rating) || 0;
    
    console.log('Star Rating System Initialized');
    console.log('Total stars:', stars.length);
    console.log('Initial rating:', currentRating);
    
    
    // ============================================
    // 2. INITIALIZE DEFAULT RATING
    // ============================================
    
    // Set initial rating if exists
    if (currentRating > 0) {
        updateStarsDisplay(currentRating, true);
    }
    
    
    // ============================================
    // 3. ADD EVENT LISTENERS TO EACH STAR
    // ============================================
    
    stars.forEach((star, index) => {
        
        // Hover effect - show preview
        star.addEventListener('mouseover', function() {
            const hoverRating = parseInt(this.dataset.value);
            updateStarsDisplay(hoverRating, false);
        });
        
        // Click to select rating
        star.addEventListener('click', function() {
            const selectedRating = parseInt(this.dataset.value);
            currentRating = selectedRating;
            
            // Update hidden input value for form submission
            ratingInput.value = selectedRating;
            
            // Update container data attribute
            starRatingContainer.dataset.rating = selectedRating;
            
            // Update visual display
            updateStarsDisplay(selectedRating, true);
            
            console.log('Rating selected:', selectedRating);
            
            // Optional: Add a small animation effect
            this.style.transform = 'scale(1.2)';
            setTimeout(() => {
                this.style.transform = 'scale(1)';
            }, 200);
        });
    });
    
    
    // ============================================
    // 4. RESET TO CURRENT RATING ON MOUSE LEAVE
    // ============================================
    
    starRatingContainer.addEventListener('mouseleave', function() {
        updateStarsDisplay(currentRating, true);
    });
    
    
    // ============================================
    // 5. HELPER FUNCTION: UPDATE STARS DISPLAY
    // ============================================
    
    /**
     * Updates the visual appearance of stars
     * @param {number} rating - The rating value (1-5)
     * @param {boolean} isActive - Whether this is the locked-in rating
     */
    function updateStarsDisplay(rating, isActive) {
        stars.forEach((star, index) => {
            const starValue = parseInt(star.dataset.value);
            
            // Remove all state classes first
            star.classList.remove('active', 'hovered');
            
            // Fill stars up to the rating value
            if (starValue <= rating) {
                star.textContent = '★'; // Filled star
                
                if (isActive) {
                    star.classList.add('active');
                } else {
                    star.classList.add('hovered');
                }
            } else {
                star.textContent = '☆'; // Empty star
            }
        });
    }
    
    
    // ============================================
    // 6. KEYBOARD ACCESSIBILITY (BONUS)
    // ============================================
    
    // Allow keyboard navigation (1-5 keys)
    document.addEventListener('keypress', function(e) {
        const key = e.key;
        
        // Check if a number key 1-5 was pressed
        if (key >= '1' && key <= '5') {
            const rating = parseInt(key);
            currentRating = rating;
            ratingInput.value = rating;
            starRatingContainer.dataset.rating = rating;
            updateStarsDisplay(rating, true);
            
            console.log('Rating set via keyboard:', rating);
        }
    });
    
    
    // ============================================
    // 7. FORM VALIDATION (OPTIONAL)
    // ============================================
    
    const reviewForm = document.querySelector('form');
    
    if (reviewForm) {
        reviewForm.addEventListener('submit', function(e) {
            if (currentRating === 0) {
                e.preventDefault();
                alert('Please select a rating before submitting your review!');
                
                // Add shake animation to stars
                starRatingContainer.style.animation = 'shake 0.5s';
                setTimeout(() => {
                    starRatingContainer.style.animation = '';
                }, 500);
                
                return false;
            }
            
            console.log('Form submitted with rating:', currentRating);
        });
    }
});


// ============================================
// 8. READ-ONLY STAR DISPLAY (For existing reviews)
// ============================================

/**
 * Initialize read-only star displays for existing reviews
 * This runs separately from the interactive rating
 */
function initializeReadOnlyStars() {
    const readOnlyStars = document.querySelectorAll('.review-stars');
    
    readOnlyStars.forEach(container => {
        const rating = parseInt(container.dataset.rating);
        let starsHTML = '';
        
        // Create filled and empty stars based on rating
        for (let i = 1; i <= 5; i++) {
            if (i <= rating) {
                starsHTML += '<span class="star-readonly filled">★</span>';
            } else {
                starsHTML += '<span class="star-readonly">☆</span>';
            }
        }
        
        container.innerHTML = starsHTML;
    });
}

// Initialize read-only stars when DOM is ready
document.addEventListener('DOMContentLoaded', initializeReadOnlyStars);
