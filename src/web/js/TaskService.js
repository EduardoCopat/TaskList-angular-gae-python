app.service('taskService', ['$http',  function($http) {
    this.readAllTasks = function(){
        return $http.get('/tasks')
    }

    this.postTask = function(task){
        return $http.post('/task', JSON.stringify(task))
    };
}]);
