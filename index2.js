// app.js
angular.module('todoApp', [])
    .controller('TodoController', ['$scope', function($scope) {
        $scope.tasks = [];

        $scope.addTask = function() {
            if ($scope.newTask) {
                $scope.tasks.push($scope.newTask);
                $scope.newTask = ''; // Clear input field
            }
        };
    }]);
