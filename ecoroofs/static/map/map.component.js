import Map from './map';

const MapComponent = {
    template: '',
    controller: function (appConfig) {
        const target = document.querySelector(appConfig.elementSelector);
        const options = Object.assign({}, appConfig.map, {
            env: appConfig.env,
            target: target
        });
        this.target = target;
        this.map = new Map(options);
    }
};

export default MapComponent;
