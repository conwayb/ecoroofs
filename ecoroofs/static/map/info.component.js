import template from './info.html!text';

const ContentComponent = {
    template: template,
    controller: function ($mdSidenav, map, Location) {
        const mapView = map.getView();
        const sidenavId = 'sidenav-map-info';
        const width = 320;  // XXX

        this.location = null;

        this.pan = (direction) => {
            const center = mapView.getCenter();
            const centerPixel = map.getPixelFromCoordinate(center);
            const x = centerPixel[0];
            const y = centerPixel[1];
            const newX = x + (width * direction);
            const newCenter = map.getCoordinateFromPixel([newX, y]);
            const pan = ol.animation.pan({
                source: map.getView().getCenter(),
                duration: 200
            });
            map.beforeRender(pan);
            mapView.setCenter(newCenter);
        };

        this.open = () => {
            const sidenav = $mdSidenav(sidenavId);
            if (!sidenav.isOpen()) {
                sidenav.open();
                this.pan(1);
            }
        };

        this.close = () => {
            const sidenav = $mdSidenav(sidenavId);
            if (sidenav.isOpen()) {
                sidenav.close();
                this.pan(-1);
            }
        };

        map.on('singleclick', (event) => {
            const feature = map.forEachFeatureAtPixel(event.pixel, (feature) => feature);
            if (feature) {
                const slug = feature.get('slug');
                this.location = Location.get({
                    slug: slug
                }, () => {
                    this.open();
                }, () => {
                    this.close();
                });
            } else {
                this.close();
            }
        });
    }
};

export default ContentComponent;
