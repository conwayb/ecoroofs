import template from './toolbar.html!text';

const ToolbarComponent = {
    template: template,
    controller: function ($mdSidenav, appConfig) {
        const sidenavId = 'sidenav-left';
        this.appConfig = appConfig;
        this.user = appConfig.user;
        this.openSidenav = () => {
            $mdSidenav(sidenavId).open();
        };
        this.closeSidenav = () => {
            $mdSidenav(sidenavId).close();
        };
    }
};

export default ToolbarComponent;
