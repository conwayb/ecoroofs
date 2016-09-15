import template from './toolbar.html!text';

const ToolbarComponent = {
    template: template,
    controller: function ($http, $mdSidenav, appConfig) {
        const sidenavId = 'sidenav-left';
        this.appConfig = appConfig;
        this.user = appConfig.user;
        this.totalSquareFootage = null;
        this.openSidenav = () => {
            $mdSidenav(sidenavId).open();
        };
        this.closeSidenav = () => {
            $mdSidenav(sidenavId).close();
        };
        $http.get('/_/locations/square-footage').then((response) => {
            this.totalSquareFootage = response.data.total;
        });
    }
};

export default ToolbarComponent;
