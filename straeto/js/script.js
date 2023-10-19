var userPosition; // Global variable to store user's geolocation

        function initMap() {
            if (userPosition) {
                const latitude = userPosition.coords.latitude;
                const longitude = userPosition.coords.longitude;
                var map = L.map('map').setView([latitude, longitude], 10);
        L.marker([latitude, longitude]).addTo(map).bindPopup('Marker Popup Text');


                L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                }).addTo(map);
            }
        }

        function getLocation() {
            if ("geolocation" in navigator) {
                navigator.geolocation.getCurrentPosition(function(position) {
                    userPosition = position; // Store user's geolocation in the global variable
                    initMap(); // Call initMap to initialize the map
                }, function(error) {
                    // Handle errors here
                    switch (error.code) {
                        case error.PERMISSION_DENIED:
                            console.error("User denied geolocation request.");
                            break;
                        case error.POSITION_UNAVAILABLE:
                            console.error("Location information is unavailable.");
                            break;
                        case error.TIMEOUT:
                            console.error("The request to get user location timed out.");
                            break;
                        default:
                            console.error("An unknown error occurred.");
                            break;
                    }
                });
            } else {
                console.error("Geolocation is not available in this browser.");
            }
        }

        // Call getLocation() to start the geolocation process
        getLocation();