"use strict";

function initMap() {
  const sfCityCoords = {
    lat: 37.7554818,
    lng: -122.4451369
  };
  
  const basicMap = new google.maps.Map(
    document.querySelector("#map"),
    {
      center: sfCityCoords,
      zoom: 12
    }
  );
 
  // const sfMarker = new google.maps.Marker({
  //   position: sfCityCoords,
  //   title: "San Francisco",
  //   map: basicMap
  // });

  const geocoder = new google.maps.Geocoder();
  geocoder.geocode({address: $("#address")[0].innerText}, (results, status) => {
    console.log($("#address")[0].innerText);
    if (status === 'OK') {
      const buildingLocation = results[0].geometry.location;

      console.log(buildingLocation)

      const buildingLocationMarker = new google.maps.Marker({
        position: buildingLocation,
        map: basicMap
      });

      basicMap.setCenter(buildingLocation);
      basicMap.setZoom(15);
    } else {
      alert(`Geocode was unsuccessful for the following reason:${status}`);
    }
  });

}
