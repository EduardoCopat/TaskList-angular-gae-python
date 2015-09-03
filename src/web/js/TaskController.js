app.controller('taskController', ['$scope', 'taskService',  function($scope, taskService) {
    $scope.currentTasks = []
	$scope.taskToAdd = {
        title: "",
        description: "",
    };

    $scope.readAllTasks = function(){
       readRequest = taskService.readAllTasks();
       readRequest.success(
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
                $scope.taskToAdd.title="";
                $scope.taskToAdd.description="";
             }
         );
    }

    $scope.readAllTasks();
}]);