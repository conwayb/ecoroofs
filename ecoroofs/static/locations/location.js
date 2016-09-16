import 'angular-resource';

export default function locationResourceFactory ($resource) {
    const url = '/_/locations/:slug';
    const Location = $resource(url);
    return Location;
}
