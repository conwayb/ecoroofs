import angular from 'angular';
import 'angular-material';
import commonConfig from 'config';
import AdminComponent from './admin.component';

const ecoroofsAdmin = angular
    .module('ecoroofsAdmin', [
        'ngMaterial'
    ])
    .config(commonConfig)
    .component('ecoroofsAdmin', AdminComponent)

angular.bootstrap(document.body, [ecoroofsAdmin.name]);

export default ecoroofsAdmin;
