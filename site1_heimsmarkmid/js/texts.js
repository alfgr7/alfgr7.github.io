
function readFile(file, tag) {
    document.addEventListener('DOMContentLoaded', function () {
        const outputH1 = document.getElementById(tag);
        
        fetch(file)
            .then(response => response.text())
            .then(data => {
                outputH1.textContent = data;
            })
    });
}



readFile('./assets/text/par_main01.txt','par_main01')
readFile('./assets/text/par_train01.txt','par_train01')
