var KanBanModule = angular.module('Yata', ['YataServices','ngRoute', 'oauth'])
.config(function($locationProvider) {
      $locationProvider.html5Mode(true).hashPrefix('!');
})
.config(['$routeProvider', '$resourceProvider', function($routeProvider, $resourceProvider) {
     $resourceProvider.defaults.stripTrailingSlashes = false; 

     $routeProvider.
         when('/timesheets', {templateUrl: yataUrls['template_timesheet_list'], controller: TimesheetListCtrl}).
         when('/timesheet/new', {templateUrl: yataUrls['template_timesheet_new'], controller: TimesheetNewCtrl}).
         when('/timesheet/:Id', {templateUrl: yataUrls['template_timesheet_view'], controller: TimesheetViewCtrl}).
         otherwise({redirectTo: '/timesheets'});
 }])
;
