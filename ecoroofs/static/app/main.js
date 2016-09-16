import angular from 'angular';
import 'angular-material';
import 'angular-resource';
import 'angular-route';
import commonConfig from 'config/config';
import commonRun from 'config/run';
import Map from 'map/map';
import MapComponent from 'map/map.component';
import PageComponent from 'pages/page.component';
import SidenavComponent from 'sidenav/sidenav.component';
import ToolbarComponent from 'toolbar/toolbar.component';
import pageResourceFactory from 'pages/page';

const ecoroofsApp = angular
    .module('ecoroofsApp', [
        'ngMaterial',
        'ngResource',
        'ngRoute'
    ])
    .config(commonConfig)
    .run(commonRun)
    .constant('appConfig', APP_CONFIG)
    .factory('Page', pageResourceFactory)
    .service('map', Map)
    .component('ecoroofsMap', MapComponent)
    .component('ecoroofsPage', PageComponent)
    .component('ecoroofsSidenav', SidenavComponent)
    .component('ecoroofsToolbar', ToolbarComponent)
    .component('notFound', {
        template: `
            <md-content class="standard-padding">
                <h1>Not Found</h1>
                <p>That page could not be found.</p>
            </md-content>
        `
    })

angular.bootstrap(document.body, [ecoroofsApp.name]);

export default ecoroofsApp;
