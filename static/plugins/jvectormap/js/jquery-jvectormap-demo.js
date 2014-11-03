$(document).ready(function() {

$('#world-map').vectorMap({map: 'world_mill_en',
          backgroundColor: 'transparent',
          regionStyle: {
            initial: {
              fill: '#1ABC9C',
            },
            hover: {
              "fill-opacity": 0.8
            }
          },
          markerStyle:{
              initial:{
                r: 10
              },
               hover: {
                r: 12,
                stroke: 'rgba(255,255,255,0.8)',
                "stroke-width": 3
              }
            }});
$('#europe-map').vectorMap({map: 'europe_mill_en',
          backgroundColor: 'transparent',
          regionStyle: {
            initial: {
              fill: '#1ABC9C',
            },
            hover: {
              "fill-opacity": 0.8
            }
          },
          markerStyle:{
              initial:{
                r: 10
              },
               hover: {
                r: 12,
                stroke: 'rgba(255,255,255,0.8)',
                "stroke-width": 3
              }
            }});
$('#canada-map').vectorMap({map: 'ca_lcc_en',
          backgroundColor: 'transparent',
          regionStyle: {
            initial: {
              fill: '#1ABC9C',
            },
            hover: {
              "fill-opacity": 0.8
            }
          },
          markerStyle:{
              initial:{
                r: 10
              },
               hover: {
                r: 12,
                stroke: 'rgba(255,255,255,0.8)',
                "stroke-width": 3
              }
            }});
$('#italy-map').vectorMap({map: 'it_mill_en',
          backgroundColor: 'transparent',
          regionStyle: {
            initial: {
              fill: '#1ABC9C',
            },
            hover: {
              "fill-opacity": 0.8
            }
          },
          markerStyle:{
              initial:{
                r: 10
              },
               hover: {
                r: 12,
                stroke: 'rgba(255,255,255,0.8)',
                "stroke-width": 3
              }
            }});
$('#usa-map').vectorMap({map: 'us_aea_en',
          backgroundColor: 'transparent',
          regionStyle: {
            initial: {
              fill: '#1ABC9C',
            },
            hover: {
              "fill-opacity": 0.8
            }
          },
          markerStyle:{
              initial:{
                r: 10
              },
               hover: {
                r: 12,
                stroke: 'rgba(255,255,255,0.8)',
                "stroke-width": 3
              }
            }});
$('#chicago-map').vectorMap({map: 'us-il-chicago_mill_en',
          backgroundColor: 'transparent',
          regionStyle: {
            initial: {
              fill: '#1ABC9C',
            },
            hover: {
              "fill-opacity": 0.8
            }
          },
          markerStyle:{
              initial:{
                r: 10
              },
               hover: {
                r: 12,
                stroke: 'rgba(255,255,255,0.8)',
                "stroke-width": 3
              }
            }});
$('#ny-map').vectorMap({map: 'us-ny-newyork_mill_en',
          backgroundColor: 'transparent',
          regionStyle: {
            initial: {
              fill: '#1ABC9C',
            },
            hover: {
              "fill-opacity": 0.8
            }
          },
          markerStyle:{
              initial:{
                r: 10
              },
               hover: {
                r: 12,
                stroke: 'rgba(255,255,255,0.8)',
                "stroke-width": 3
              }
            }});
$('#united-kingdom-map').vectorMap({map: 'uk_mill_en',
          backgroundColor: 'transparent',
          regionStyle: {
            initial: {
              fill: '#1ABC9C',
            },
            hover: {
              "fill-opacity": 0.8
            }
          },
          markerStyle:{
              initial:{
                r: 10
              },
               hover: {
                r: 12,
                stroke: 'rgba(255,255,255,0.8)',
                "stroke-width": 3
              }
            }});

  });