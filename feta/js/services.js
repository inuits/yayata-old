angular.module('YataServices', ['ngResource']).
factory('Project', function($resource){
    return $resource(BetaApiUrl + 'projects/:projectId', {}, {
        query: {method:'GET', params:{projectId:''}, isArray:true},
        get: {method:'GET', params:{projectId:''}, isArray:true}
    });
}).
factory('Timesheet', function($resource){
    return $resource(BetaApiUrl + 'timesheets/:timesheetId', {}, {
        query: {method:'GET', params:{timesheetId:''}, isArray:true},
        get: {method:'GET', params:{timesheetId:''}, isArray:true}
    });
});

