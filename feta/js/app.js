var KanBanModule = angular.module('Yata', ['YataServices','ngRoute']).
config(['$routeProvider', function($routeProvider) {
     $routeProvider.
         when('/timesheets', {templateUrl: yataUrls['template_timesheet_list'], controller: TimesheetListCtrl}).
         when('/timesheet/:Id', {templateUrl: yataUrls['template_timesheet_view'], controller: TimesheetViewCtrl}).
         otherwise({redirectTo: '/timesheets'});
 }]);
