import Map from './map';

const MapComponent = {
    template: '',
    controller: function (appConfig) {
        this.target = document.querySelector(appConfig.elementSelector);
        this.map = new Map({
            target: this.target
        });
    }
};

export default MapComponent;
