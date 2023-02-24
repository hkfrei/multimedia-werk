// marker image
const pin = "/static/kartenwerk/img/logomarker.png";
// Create the script tag, set the appropriate attributes
const script = document.createElement("script");
script.src =
  "https://maps.googleapis.com/maps/api/js?key=AIzaSyA4RuSmaLvSGKQdlTWFmQxetwHlh7XECk0&callback=initMap&v=weekly";
script.async = true;

const mapOptions = {
  center: { lat: 47.29522349252075, lng: 8.790515938971136 },
  zoom: 11,
  mapTypeControl: false,
  styles: [
    {
      featureType: "all",
      stylers: [
        {
          saturation: -100,
        },
        {
          gamma: 0.5,
        },
      ],
    },
  ],
};

const initMap = () => {
  // JS API is loaded and available
  const map = new google.maps.Map(
    document.getElementById("contact__map"),
    mapOptions
  );
  const marker = new google.maps.Marker({
    position: new google.maps.LatLng(47.310761, 8.79749),
    animation: google.maps.Animation.DROP,
    title: "Office Karten-Werk GmbH",
    icon: pin,
  });
  marker.setMap(map);
};
// Attach callback function to the `window` object
window.initMap = initMap;

// Append the 'script' element to 'head'
document.head.appendChild(script);
