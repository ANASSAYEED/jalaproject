// app.js
angular.module('myApp', [])
    .controller('MainController', ['$scope', function($scope) {
        $scope.color = ''; // Initialize color
    }])
    .directive('colorBox', function() {
        return {
            restrict: 'E',
            scope: {
                color: '='
            },
            template: '<div class="color-box" ng-style="{\'background-color\': color}"></div>'
        };
    });
