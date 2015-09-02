app.controller('taskController', ['$scope', 'taskService',  function($scope, taskService) {
    $scope.currentTasks = []
	$scope.taskToAdd = {
        title: "",
        description: "",
    };

    $scope.readAllTasks = function(){
       taskService.readAllTasks().success(
           function(response) {
                $scope.currentTasks = response;
           }
       );
    }

    $scope.submit = function(){
         postRequest = taskService.postTask($scope.taskToAdd);
         postRequest.success(
             function(response){
                $scope.currentTasks.push(response);
             }
         );
    }

    $scope.readAllTasks();

}]);