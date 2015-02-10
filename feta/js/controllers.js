function TimesheetListCtrl($scope, Timesheet){
    timesheets = Timesheet.query({},
            function(){
                $scope.timesheets = timesheets;
            }
            );
}

function TimesheetViewCtrl($scope, $routeParams, Timesheet){
    var timesheet = Timesheet.query({'timesheetId': $routeParams.timesheetId},
        function(){
            $scope.timesheet = timesheet;
        }
    );
}
