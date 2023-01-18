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