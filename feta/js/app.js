var KanBanModule = angular.module('Yata', ['YataServices','ngRoute','ngCookies'])
.config(['$routeProvider', '$resourceProvider', function($routeProvider, $resourceProvider) {
     $resourceProvider.defaults.stripTrailingSlashes = false;

     $routeProvider.
         when('/timesheet/new', {templateUrl: yataUrls['template_timesheet_new'], controller: TimesheetNewCtrl}).
         when('/timesheet/:Id', {templateUrl: yataUrls['template_timesheet_view'], controller: TimesheetViewCtrl}).
         when('/', {templateUrl: yataUrls['template_timesheet_list'], controller: TimesheetListCtrl})
         .otherwise({ redirectTo: '/' });
 }])
.controller('LoginCtrl', function($rootScope, $scope, Login, api, $cookies) {
    $scope.login = function(){
        api.init();
        login_trial = Login.login({'username': $scope.username, 'password': $scope.password}).$promise.then(function(data) {
        api.init(data['token']);
            $cookies['token']=data['token'];
        })
    };
    }
)
.run(function (api) {
      api.init();
});
//.config(['$locationProvider', function($locationProvider) {
//      $locationProvider.html5Mode(true).hashPrefix('!');
//}])
;
