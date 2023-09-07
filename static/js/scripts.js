mapboxgl.accessToken = "{{ mapbox_key }}";

const geojson = {
    'type': 'FeatureCollection',
    'features': [
    {
        'type': 'Feature',
        'properties': {
        'message': 'Foo',
        'iconSize': [60, 60]
        },
        'geometry': {
        'type': 'Point',
        'coordinates': [-66.324462, -16.024695]
        }
    },
    {
        'type': 'Feature',
        'properties': {
        'message': 'Bar',
        'iconSize': [50, 50]
        },
        'geometry': {
        'type': 'Point',
        'coordinates': [-61.21582, -15.971891]
        }
    },
    {
        'type': 'Feature',
        'properties': {
        'message': 'Baz',
        'iconSize': [40, 40]
        },
        'geometry': {
        'type': 'Point',
        'coordinates': [-63.292236, -18.281518]
        }
    }
    ]
};

const map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/satellite-streets-v11',
    zoom: 1.5,
    center: [30, 50],
    projection: 'globe'
});

map.on("style.load", () => {
    map.setFog({});
});

// Add markers to the map.
for (const marker of geojson.features) {
    // Create a DOM element for each marker.
    const el = document.createElement('div');
    const width = marker.properties.iconSize[0];
    const height = marker.properties.iconSize[1];
    el.className = 'marker';
    el.style.backgroundImage = `url(https://placekitten.com/g/${width}/${height}/)`;
    el.style.width = `${width}px`;
    el.style.height = `${height}px`;
    el.style.backgroundSize = '100%';
    
    el.addEventListener('click', () => {
    $('#exampleModal').modal('toggle')
    });
    
    // Add markers to the map.
    new mapboxgl.Marker(el)
    .setLngLat(marker.geometry.coordinates)
    .addTo(map);
}