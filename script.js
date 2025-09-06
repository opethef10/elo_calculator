document.addEventListener('DOMContentLoaded', function() {
    const rating1Input = document.getElementById('rating1');
    const rating2Input = document.getElementById('rating2');
    const kFactorInput = document.getElementById('k-factor');
    const scoreButtons = document.querySelectorAll('.score-btn');

    const ratingChangeEl = document.getElementById('rating-change');
    const newRatingsEl = document.getElementById('new-ratings');

    let selectedScore = 1;


    // Calculate function
    function calculateElo() {
        const rating1 = parseInt(rating1Input.value);
        const rating2 = parseInt(rating2Input.value);
        const K = parseInt(kFactorInput.value);
        const score = selectedScore;


        if (score < 0 || score > 1) {
            return;
        }

        if (rating1Input.validity.valid && rating2Input.validity.valid && kFactorInput.validity.valid) {
            const M = 400;
            const delta = rating2 - rating1;
            const expected = 1 / (1 + Math.pow(10, delta / M));
            const gain = Math.round(K * (score - expected));

            // Update results
            const newRating1 = rating1 + gain;
            const newRating2 = rating2 - gain;

            // Style the gain based on positive/negative
            if (gain > 0) {
                ratingChangeEl.innerHTML = `<span class="gain-positive">+${gain}</span>`;
            } else if (gain < 0) {
                ratingChangeEl.innerHTML = `<span class="gain-negative">${gain}</span>`;
            } else {
                ratingChangeEl.textContent = `${gain}`;
            }

            newRatingsEl.textContent = `${newRating1}, ${newRating2}`;
        }
        else {
            ratingChangeEl.textContent = '-';
            newRatingsEl.textContent = 'Please fill the inputs correctly';
        }
    }

    // Score selection
    scoreButtons.forEach(btn => {
        btn.addEventListener('click', function() {
            scoreButtons.forEach(b => b.classList.remove('active'));
            this.classList.add('active');
            selectedScore = parseFloat(this.getAttribute('data-score'));
        });
        btn.addEventListener('click', calculateElo);
    });

    // Calculate when inputs change
    rating1Input.addEventListener('input', calculateElo);
    rating2Input.addEventListener('input', calculateElo);
    kFactorInput.addEventListener('input', calculateElo);

    // Calculate initially
    calculateElo();
});
