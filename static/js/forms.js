const form = document.getElementById('farm-data-form');
const formsButton = document.getElementById('submit-form');
const loader = document.getElementById('loader');


document.addEventListener('DOMContentLoaded', function() {
    const cropTypeSelect = document.getElementById('crop-type');

    // Fetch the list of plants from the backend
    fetch('/plants')
        .then(response => response.json())
        .then(plants => {
            // Clear existing options
            cropTypeSelect.innerHTML = '';
            
            // Add default option
            const defaultOption = document.createElement('option');
            defaultOption.value = '';
            defaultOption.textContent = 'Select Crop';
            cropTypeSelect.appendChild(defaultOption);

            // Populate the select input with the list of plants
            plants.forEach(plant => {
                const option = document.createElement('option');
                option.value = plant;  // Use lowercase value
                option.textContent = plant;
                cropTypeSelect.appendChild(option);
            });
        })
        .catch(error => {
            console.error('Error fetching plant list:', error);
            cropTypeSelect.innerHTML = '<option value="">Error loading crops</option>';
        });
});

// Function to get GPS coordinates
function getCoordinates(callback) {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position) {
            const latitude = position.coords.latitude;
            const longitude = position.coords.longitude;
            callback(latitude, longitude);
        }, function(error) {
            alert('Error fetching GPS coordinates: ' + error.message);
        });
    } else {
        alert('Geolocation is not supported by your browser.');
    }
}

formsButton.addEventListener('click', function(event) {
    event.preventDefault();

    // Show the loader
    loader.style.display = 'block';

    // Retrieve GPS coordinates
    getCoordinates(function(latitude, longitude) {
        const cropType = document.getElementById('crop-type').value;
        const radiusKm = document.getElementById('radius-km').value;
        const isIrrigated = document.querySelector('input[name="irrigation"]:checked').value;
        const plantingPeriod = document.querySelector('input[name="plantingPeriod"]:checked').value;
        const existingCrops = document.querySelector('input[name="existingCrops"]:checked').value;

        const requestData = {
            crop_type: cropType,
            latitude: latitude,
            longitude: longitude,
            radius_km: radiusKm,
            is_irrigated: isIrrigated,
            planting_period: plantingPeriod,
            existing_crops: existingCrops
        };

        // Perform REST API call
        fetch('/drought-analysis', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(requestData)
        })
        .then(response => response.json())
        .then(data => {
            // Hide the loader
            loader.style.display = 'none';

            const recommendation = data.recommendation || 'No recommendation available for this risk level.';

            // Display results
            const resultsSection = document.getElementById('results');
            const analysisResults = document.getElementById('analysis-results');
            analysisResults.innerHTML = `
                <p><span class='bold'>Drought risk:</span>${data.drought_risk}</p>
                <a href="/water-balance?latitude=${latitude}&longitude=${longitude}" target="_blank">See water balance in your area here</a>
                <p><span class='bold'>Recommendation:</span>${recommendation}</p>
            `;
            resultsSection.style.display = 'block';

            // Scroll to the results section smoothly
            resultsSection.scrollIntoView({ behavior: 'smooth' });
        })
        .catch(error => {
            // Hide the loader on error
            loader.style.display = 'none';
            console.error('Error:', error);
        });
    });
});

function resetForm() {
    form.reset();
    document.getElementById('results').style.display = 'none';
}
