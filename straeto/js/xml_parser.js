fetch('https://opendata.straeto.is/bus/x0473244192926714/status.xml')
    .then(response => response.text())
    .then(xmlData => {
        // Parse the XML data when the fetch is successful
        const parser = new DOMParser();
        const xmlDoc = parser.parseFromString(xmlData, 'text/xml');
        
        // Use xmlDoc to access and manipulate the XML data
        const items = xmlDoc.querySelectorAll('item');
        items.forEach(item => {
            const name = item.querySelector('name').textContent;
            const price = item.querySelector('price').textContent;
            console.log(`Item: ${name}, Price: ${price}`);
        });
    })
    .catch(error => {
        console.error('Error fetching XML data:', error);
    });
