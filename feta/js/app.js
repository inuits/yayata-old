var KanBanModule = angular.module('Yata', ['YataServices', 'YataControllers']).
config(['$routeProvider', function($routeProvider) {
     $routeProvider.
         when('/timesheets', {templateUrl: YataUrls['template_timesheet_list'], controller: TimesheetListCtrl}).
         when('/timesheet/:Id', {templateUrl: yataUrls['template_timesheet_view'], controller: TimesheetViewCtrl}).
         otherwise({redirectTo: '/timesheets'});
 }]);
