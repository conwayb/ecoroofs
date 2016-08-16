import ol from 'ol';

export default class Map extends ol.Map {
    constructor (options) {
        const center = ol.proj.fromLonLat(options.view.center);

        const baseLayers = [
            new ol.layer.Tile({
                source: new ol.source.OSM()
            })
        ];



        const view = new ol.View({
            center: center,
            minZoom: options.view.minZoom,
            maxZoom: options.view.maxZoom,
            zoom: options.view.zoom
        });

        super({
            layers: baseLayers,
            target: options.target,
            view: view
        });
    }
}
