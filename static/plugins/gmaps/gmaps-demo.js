$(document).ready(function() {

		//Basic
		new GMaps({
		  div: '#basic-map',
		  lat: -12.043333,
		  lng: -77.028333
		});

       //Events
		mapEvents = new GMaps({
		  div: '#map-events',
		  zoom: 16,
		  lat: -12.043333,
		  lng: -77.028333,
		  click: function(e) {
		    alert('click');
		  },
		  dragend: function(e) {
		    alert('dragend');
		  }
		});

		//Markers
		mapMarkers = new GMaps({
        div: '#map-markers',
        lat: -12.043333,
        lng: -77.028333
      });
      mapMarkers.addMarker({
        lat: -12.043333,
        lng: -77.03,
        title: 'Lima',
        details: {
          database_id: 42,
          author: 'HPNeo'
        },
        click: function(e){
          if(console.log)
            console.log(e);
          alert('You clicked in this marker');
        }
      });
      mapMarkers.addMarker({
        lat: -12.042,
        lng: -77.028333,
        title: 'Marker with InfoWindow',
        infoWindow: {
          content: '<p>HTML Content</p>'
        }
      });

      //Geolocation
      mapGeolocation = new GMaps({
        div: '#map-geolocation',
        lat: -12.043333,
        lng: -77.028333
      });

      GMaps.geolocate({
        success: function(position){
          mapGeolocation.setCenter(position.coords.latitude, position.coords.longitude);
        },
        error: function(error){
          alert('Geolocation failed: '+error.message);
        },
        not_supported: function(){
          alert("Your browser does not support geolocation");
        },
        always: function(){
          //alert("Done!");
        }
      });

      //Geocoding
      mapGeocoding = new GMaps({
        div: '#map-geocoding',
        lat: -12.043333,
        lng: -77.028333
      });
      $('#geocoding_form').submit(function(e){
        e.preventDefault();
        GMaps.geocode({
          address: $('#address').val().trim(),
          callback: function(results, status){
            if(status=='OK'){
              var latlng = results[0].geometry.location;
              mapGeocoding.setCenter(latlng.lat(), latlng.lng());
              mapGeocoding.addMarker({
                lat: latlng.lat(),
                lng: latlng.lng()
              });
            }
          }
        });
      });

      //polylines
       polylinesMap = new GMaps({
        div: '#map-polylines',
        lat: -12.043333,
        lng: -77.028333,
        click: function(e){
          console.log(e);
        }
      });

      path = [[-12.044012922866312, -77.02470665341184], [-12.05449279282314, -77.03024273281858], [-12.055122327623378, -77.03039293652341], [-12.075917129727586, -77.02764635449216], [-12.07635776902266, -77.02792530422971], [-12.076819390363665, -77.02893381481931], [-12.088527520066453, -77.0241058385925], [-12.090814532191756, -77.02271108990476]];

      polylinesMap.drawPolyline({
        path: path,
        strokeColor: '#1abc9c',
        strokeOpacity: 0.6,
        strokeWeight: 6
      });

      //Overlays
      mapOverlays = new GMaps({
        div: '#map-overlays',
        lat: -12.043333,
        lng: -77.028333
      });
      mapOverlays.drawOverlay({
        lat: mapOverlays.getCenter().lat(),
        lng: mapOverlays.getCenter().lng(),
        content: '<div class="overlay">Lima<div class="overlay_arrow above"></div></div>',
        verticalAlign: 'top',
        horizontalAlign: 'center'
      });

      //Polygon
      mapPolygon = new GMaps({
        div: '#map-polygon',
        lat: -12.043333,
        lng: -77.028333
      });

      var path = [[-12.040397656836609,-77.03373871559225],
									[-12.040248585302038,-77.03993927003302],
									[-12.050047116528843,-77.02448169303511],
									[-12.044804866577001,-77.02154422636042]];

      polygon = mapPolygon.drawPolygon({
			  paths: path,
			  strokeColor: '#1ABC9C',
			  strokeOpacity: 1,
			  strokeWeight: 3,
			  fillColor: '#1ABC9C',
			  fillOpacity: 0.6
			});



     
});