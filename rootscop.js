// app.js
angular.module('myApp', [])
    .run(['$rootScope', function($rootScope) {
        // Initialize a root scope variable
        $rootScope.rootMessage = "Hello from the Root Scope!";
    }])
    .controller('FirstController', ['$scope', function($scope) {
        // Initialize a local scope variable
        $scope.message = "Initial message from First Controller";

        $scope.updateMessage = function() {
            // Update the local scope variable
            $scope.message = $scope.newMessage;
        };
    }])
    .controller('SecondController', ['$scope', function($scope) {
        // Access the root scope variable
        $scope.rootMessage = $scope.$root.rootMessage;
    }]);
