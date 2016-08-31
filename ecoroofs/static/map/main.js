import angular from 'angular';
import 'angular-material';
import { commonConfig, commonRun } from 'config';
import MapComponent from './map.component';

const ecoroofsMap = angular
    .module('ecoroofsMap', [
        'ngMaterial'
    ])
    .config(commonConfig)
    .run(commonRun)
    .constant('appConfig', APP_CONFIG)
    .component('ecoroofsMap', MapComponent)

angular.bootstrap(document.body, [ecoroofsMap.name]);

export default ecoroofsMap;
