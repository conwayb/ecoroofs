import ol from 'ol';

const pointRadius = 6;
const projectionCode = 'EPSG:3857';

export default class Map extends ol.Map {
    constructor (options) {
        const center = ol.proj.fromLonLat(options.view.center);
        const serverOptions = options.server;
        const mapServerBaseURL = serverOptions.baseURL;
        const workspace = `ecoroofs-${options.env}`;

        const baseLayers = [
            new ol.layer.Tile({
                source: new ol.source.OSM()
            })
        ];

        const featureLayers = [
            makeFeatureLayer(mapServerBaseURL, workspace, 'locations', 'Locations')
        ];

        const allLayers = [].concat(baseLayers, featureLayers);

        const view = new ol.View({
            center: center,
            minZoom: options.view.minZoom,
            maxZoom: options.view.maxZoom,
            zoom: options.view.zoom
        });

        super({
            layers: allLayers,
            target: options.target,
            view: view
        });
    }
}

function makeFeatureLayer (baseURL, workspace, layerName, label, style=null) {
    const url = `${baseURL}/wfs/${workspace}`;
    const typeName = `${workspace}:${layerName}`;
    const baseParams = [
        'service=WFS',
        'version=1.1.0',
        'request=GetFeature',
        `typeName=${typeName}`,
        `srsName=${projectionCode}`,
        'outputFormat=application/json'
    ].join('&');
    return new ol.layer.Vector({
        label: label,
        source: new ol.source.Vector({
            format: new ol.format.GeoJSON(),
            strategy: ol.loadingstrategy.bbox,
            url: function (extent) {
                const bboxParam = `${extent.join(',')},${projectionCode}`;
                const requestParams = `${baseParams}&bbox=${bboxParam}`;
                return `${url}?${requestParams}`;
            }
        }),
        style: style || new ol.style.Style({
            image: new ol.style.Circle({
                radius: pointRadius,
                stroke: new ol.style.Stroke({
                    color: '#ffffff',
                    width: 2
                }),
                fill: new ol.style.Fill({
                    color: '#6a7f10',
                })
            })
        })
    })
}
