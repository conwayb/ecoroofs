import 'angular-resource';

export default function locationResourceFactory ($resource) {
    const url = '/_/locations/:id';
    const Location = $resource(url);
    return Location;
}
