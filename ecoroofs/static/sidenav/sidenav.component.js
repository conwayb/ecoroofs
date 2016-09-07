import angular from 'angular';
import template from './sidenav.html!text';

const SidenavComponent = {
    template: template,
    controller: function ($mdSidenav, appConfig, Page) {
        const sidenavId = 'sidenav-left';
        this.appConfig = appConfig;
        this.user = appConfig.user;
        this.pages = Page.query();

        this.$onInit = () => {
            const sidenavLinks = document.querySelectorAll('md-sidenav a');
            for (let i = 0; i < sidenavLinks.length; ++i) {
                angular.element(sidenavLinks[i]).on('click', () => this.close());
            }
        };

        this.open = () => {
            $mdSidenav(sidenavId).open();
        };
        this.close = () => {
            $mdSidenav(sidenavId).close();
        };
    }
};

export default SidenavComponent;
