function loc() {
  navigator.geolocation.getCurrentPosition(success, error);
}

function success(position) {
  var latitude = position.coords.latitude;
  var longitude = position.coords.longitude;
    console.log(latitude, longitude);
  document.getElementById("longitude").value = longitude;
  document.getElementById("latitude").value = latitude;
}

function error() {
  console.log("Unable to retrieve your location");
}
