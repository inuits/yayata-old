angular.module('YataServices', ['ngResource', 'ngSanitize']).
factory('api', function ($http, $cookies, Me, $rootScope) {
    return {
        init: function (token) {
            token = token || $cookies.token;
            if (token) {$http.defaults.headers.common['Authorization'] = "Token " + token;}
            else if ($http.defaults.headers.common['Authorization']){delete($http.defaults.headers.common['Authorization'])}
            $rootScope.user = Me.get();
        }
    }
}).
factory('httpInterceptor', function ($q, $window, $location, $cookieStore) {
    return {
//      'request': function(config) {
//        return config;
 //     },
     'responseError': function(response) {
            if (response.status === 401) {
                $cookieStore.remove('token');
                $location.url('/login');
            }
            return $q.reject(response);
      }
    };
}).
factory('Me', function($resource){
    return $resource(BetaApiUrl + 'me/', {}, {
        get: {method:'GET'}
    });
}).
factory('Login', function($resource){
    return $resource(BetaApiUrl + 'token/', {}, {
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

