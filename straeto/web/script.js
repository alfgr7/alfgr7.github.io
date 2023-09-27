fetch('map.html')
.then(response => response.text())
.then(data => {
    document.getElementById('map').innerHTML = data;
});