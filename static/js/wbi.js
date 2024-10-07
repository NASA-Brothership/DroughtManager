let latitude = 0;
let longitude = 0;
let map;

if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
    latitude = position.coords.latitude;
    longitude = position.coords.longitude;

    // Initialize the map
    map = L.map('map').setView([latitude, longitude], 15);

    // Add a base layer
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: 'Map data © <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    // Use fetch to send the data as query parameters in a GET request
    fetch(`/water-balance-map-tile?latitude=${encodeURIComponent(latitude)}&longitude=${encodeURIComponent(longitude)}`)
        .then(response => response.json())
        .then(data => {
        L.tileLayer(data.url, {
            opacity: 0.5,
            attribution: 'NASA SMAP Soil Moisture Data',
            maxZoom: 20
        }).addTo(map);
        })
        .catch(error => console.error('Error loading data:', error));
    }, function(error) {
        console.error('Error getting location:', error);
    });
    } else {
    console.log('Geolocation is not supported by this browser.');
    }