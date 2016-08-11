import Map from './map';

const targetId = 'ecoroofs-map';

const MapComponent = {
    template: `<div id="${targetId}"></div>`,
    controller: function () {
        this.target = document.getElementById(targetId);
        this.map = new Map({
            target: this.target
        });
    }
};

export default MapComponent;
