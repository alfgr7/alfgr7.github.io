fetch('bottom-bar.html')
.then(response => response.text())
.then(data => {
    document.getElementById('bottom-bar').innerHTML = data;
});