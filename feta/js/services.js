angular.module('YataServices', ['ngResource']).
factory('Project', function($resource){
    return $resource(BetaApiUrl + 'projects/:projectId', {}, {
        query: {method:'GET', params:{projectId:''}, isArray:true},
        get: {method:'GET', params:{projectId:''}, isArray:true}
    });
}).
factory('Project', function($resource){
    return $resource(BetaApiUrl + 'projects/:projectId', {}, {
        query: {method:'GET', params:{projectId:''}, isArray:true},
        get: {method:'GET', params:{projectId:''}, isArray:true}
    });
}).
factory('Customer', function($resource){
    return $resource(BetaApiUrl + 'customers/:customerId', {}, {
        query: {method:'GET', params:{customerId:''}, isArray:true},
        get: {method:'GET', params:{customerId:''}, isArray:true}
    });
}).
factory('Timesheet', function($resource){
    return $resource(BetaApiUrl + 'timesheets/:timesheetId', {}, {
        query: {method:'GET', params:{timesheetId:''}, isArray:true},
        get: {method:'GET', params:{timesheetId:''}, isArray:true},
        create: {method:'POST', isArray:false}
    });
});

