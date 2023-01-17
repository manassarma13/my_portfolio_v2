// //transitions

// window.onload = () => {
//     const anchors = document.querySelectorAll('a'),
//         transitions_el = document.querySelector('.transition');

//     setTimeout(() => {
//         transitions_el.classList.remove('is-active');
//     },500);


//     for(let i=0; i<anchors.length; i++) {
//         const anchor = anchors[i];

//         anchor.addEventListener('click', (e) => {
//             e.preventDefault();
//             let target = e.target.href;
//             transitions_el.classList.add('is-active');

//             setInterval(() => {
//                 window.location.href = target;
//             }, 500);
//         })
//     }
// }

// // Initialize and add the map
// function initMap() {
//     // The location of Uluru
//     const uluru = { lat: 51.486060, lng: -3.173050 };
//     // The map, centered at Uluru
//     const map = new google.maps.Map(document.getElementById("map"), {
//         zoom: 16,
//         center: uluru,
//     });
//     // The marker, positioned at Uluru
//     const marker = new google.maps.Marker({
//         position: uluru,
//         map: map,
//     });
// }

// window.initMap = initMap;