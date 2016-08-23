import angular from 'angular';
import 'angular-material';
import commonConfig from 'config';

const ecoroofsPages = angular
    .module('ecoroofsPages', [
        'ngMaterial'
    ])
    .config(commonConfig)

angular.bootstrap(document.body, [ecoroofsPages.name]);

export default ecoroofsPages;
