function initMap() {
    // The location of Uluru
    const uluru = { lat: 51.486060, lng: -3.173050 };
    // The map, centered at Uluru
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 16,
        center: uluru,
    });

    const marker = new google.maps.Marker({
        position: uluru,
        map: map,
    });
}

window.initMap = initMap;


const values = [
    { value: 'Projects', color: '#f9d77f' },
    { value: 'Experience', color: '#597bff' },
    { value: 'Certificates', color: '#f8f8f8' }
];
let currentIndex = 0;

function changeText() {
    const currentElement = values[currentIndex];
    document.getElementById('changing-text').innerHTML = currentElement.value;
    document.getElementById('changing-text').style.color = currentElement.color;
    currentIndex++;
    if (currentIndex === values.length) {
        currentIndex = 0;
    }
    setTimeout(changeText, 2000);
}

changeText();