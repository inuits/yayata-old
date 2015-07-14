var KanBanModule = angular.module('Yata', ['YataServices', ,'ngRoute','ngCookies','ngSanitize'])
.config(['$routeProvider', '$resourceProvider', '$httpProvider', function($routeProvider, $resourceProvider,$httpProvider) {
     $resourceProvider.defaults.stripTrailingSlashes = false;
     $httpProvider.interceptors.push('httpInterceptor');

     $routeProvider.
         when('/timesheet/new', {templateUrl: yataUrls['timesheet_new'], controller: TimesheetNewCtrl}).
         when('/timesheet/:timesheetId', {templateUrl: yataUrls['timesheet_view'], controller: TimesheetViewCtrl}).
         when('/login', {templateUrl: yataUrls['login_view'], controller: LoginCtrl}).
         when('/logout', {templateUrl: yataUrls['logout_view'], controller: LogoutCtrl}).
         when('/timesheets', {templateUrl: yataUrls['timesheet_list'], controller: TimesheetListCtrl}).
         when('/companies', {templateUrl: yataUrls['company_list'], controller: CompanyListCtrl}).
         when('/company/new', {templateUrl: yataUrls['company_new'], controller: CompanyNewCtrl}).
         when('/company/:companyId', {templateUrl: yataUrls['company_view'], controller: CompanyViewCtrl}).
         when('/customers', {templateUrl: yataUrls['customer_list'], controller: CompanyListCtrl}).
         when('/customer/new', {templateUrl: yataUrls['customer_new'], controller: CompanyNewCtrl}).
         when('/customer/:customerId', {templateUrl: yataUrls['customer_view'], controller: CompanyViewCtrl}).
         when('/projects', {templateUrl: yataUrls['project_list'], controller: CompanyListCtrl}).
         when('/project/new', {templateUrl: yataUrls['project_new'], controller: CompanyNewCtrl}).
         when('/project/:projectId', {templateUrl: yataUrls['project_view'], controller: CompanyViewCtrl}).
         otherwise({ redirectTo: '/timesheets' });
 }])
.run(function (api) {
      api.init();
}).run(function ($rootScope){
    $rootScope.messages = [];
})
//.config(['$locationProvider', function($locationProvider) {
//      $locationProvider.html5Mode(true).hashPrefix('!');
//}])
;
