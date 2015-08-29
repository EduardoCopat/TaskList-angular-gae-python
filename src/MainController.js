app.controller('MainController', ['$scope', '$http',  function($scope, $http) {
	$scope.task = {
        title: "",
        description: "",

    };

    $scope.submit = function(){ $http.post('/task', JSON.stringify($scope.task)) };

}]);