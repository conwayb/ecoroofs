import ol from 'ol';

export default class Map extends ol.Map {
    constructor (options) {
        let baseLayers = [
            new ol.layer.Tile({
                source: new ol.source.OSM()
            })
        ];

        let view = new ol.View({
            center: ol.proj.fromLonLat([-122.667473, 45.523023]),
            minZoom: 0,
            maxZoom: 19,
            zoom: 10
        });

        options.layers = baseLayers;
        options.view = view;

        super(options);
    }
}
