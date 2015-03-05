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
factory('httpInterceptor', function ($q, $window, $location, $cookieStore, $rootScope) {
    return {
     'responseError': function(response) {
            if (response.status === 401) {
                $cookieStore.remove('token');
                $location.url('/login');
            }
            if ('detail' in response.data){
                $rootScope.errors.push(
                        {code: response.status, message: response.data.detail}
                        )
            };
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
    return $resource(BetaApiUrl + 'companies/:companyId', {}, {
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
    return $resource(BetaApiUrl + 'timesheets/:timesheetId/', {}, {
        query: {method:'GET', url:BetaApiUrl + 'timesheets/', isArray:true},
        update: {method:'PATCH', params:{timesheetId:'@id'}, isArray:false},
        get: {method:'GET', params:{timesheetId:''}},
        create: {method:'POST', isArray:false}
    });
}).
factory('Hour', function($resource){
    return $resource(BetaApiUrl + 'timesheets/:timesheet/hours/:hour/', {}, {
        create: {method:'POST', params:{timesheetId:'@tid'}, url: BetaApiUrl + 'timesheets/:timesheetId/hours/', isArray:false},
        get: {method:'GET', url: BetaApiUrl + 'timesheets/:tid/hours/', isArray:true},
        update: {method:'PUT', params:{timesheet:'@tid', hour:'@hid'}},
        delete: {
            method:'DELETE',
            params:{
            },
            isArray:true
        },
    });
});

