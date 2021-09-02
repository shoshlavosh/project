"use strict";

function initMap() {
  const sfCityCoords = {
    lat: 37.7452134,
    lng: -122.4870761
  };
  
  const basicMap = new google.maps.Map(
    document.querySelector("#map"),
    {
      center: sfCityCoords,
      zoom: 12
    }
  );

  const sfMarker = new google.maps.Marker({
    position: sfCityCoords,
    title: "San Francisco",
    map: basicMap
  });
}