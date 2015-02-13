angular.module('YataServices', ['ngResource']).
factory('api', function ($http, $cookies) {
    return {
        init: function (token) {
            token = token || $cookies.token;
            console.debug(token)
            if (token) {$http.defaults.headers.common['Authorization'] = "Token " + token;}
        }
    };
}).
factory('Login', function($resource){
    return $resource(BetaApiUrl + 'api-token-auth/', {}, {
        login: {method:'POST'}
    });
}).
factory('Project', function($resource){
    return $resource(BetaApiUrl + 'projects/:projectId', {}, {
        query: {method:'GET', params:{projectId:''}, isArray:true},
        get: {method:'GET', params:{projectId:''}, isArray:true}
    });
}).
factory('Company', function($resource){
    return $resource(BetaApiUrl + 'customers/:companyId', {}, {
        query: {method:'GET', params:{companyId:''}, isArray:true},
        get: {method:'GET', params:{companyId:''}, isArray:true}
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

