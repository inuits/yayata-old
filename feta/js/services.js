angular.module('YataServices', ['ngResource']).
factory('timesheets', function($resource){
    return $resource(BetaApiUrl + 'timesheets/:timesheetId', {}, {
        query: {method:'GET', params:{timesheetId:''}, isArray:false},
        get: {method:'GET', params:{timesheetId:''}, isArray:false}
    });
});

