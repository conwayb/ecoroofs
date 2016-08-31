import angular from 'angular';
import 'angular-material';
import { commonConfig, commonRun } from 'config';

const ecoroofsPages = angular
    .module('ecoroofsPages', [
        'ngMaterial'
    ])
    .config(commonConfig)
    .run(commonRun)

angular.bootstrap(document.body, [ecoroofsPages.name]);

export default ecoroofsPages;
