app.controller('MainController', ['$scope', '$http',  function($scope, $http) {
	$scope.taskToAdd = {
        title: "",
        description: "",
    };

    $scope.submit = function(){ $http.post('/task', JSON.stringify($scope.taskToAdd)) };


    $scope.currentTasks = []
           $http.get('/tasks').
            success(function(response) {
                $scope.currentTasks = response
            }
         );


}]);