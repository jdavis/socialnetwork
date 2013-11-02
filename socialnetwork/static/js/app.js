'use strict';

var app = window.app = {};

/*
 * Angular App Values
 */

// Name of the app
app.name = 'tsn';

// Modules defined for the app
app.modules = [
    'ngRoute',
    app.name + '.controllers',
    app.name + '.directives',
    app.name + '.filters',
    app.name + '.routing',
    app.name + '.services',
];


// Create our app
angular.module(app.name, app.modules);
