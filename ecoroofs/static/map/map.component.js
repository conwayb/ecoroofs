import Map from './map';

const MapComponent = {
    controller: function ($http, appConfig) {
        const target = document.querySelector('ecoroofs-map');
        const options = Object.assign({}, appConfig.map, {
            target: target,
            $http: $http
        });
        this.target = target;
        this.map = new Map(options);
    }
};

export default MapComponent;
