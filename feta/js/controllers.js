function TimesheetListCtrl($scope, Timesheet){
    var timesheet = Timesheet.query({},
        function(){
            $scope.timesheets = timesheets;
        }
    );
}

function TimesheetNewCtrl($scope, Customer, Project){
    var project = Project.query({},
        function(){
            $scope.projects = project;
        }
    );
    var customer = Customer.query({},
        function(){
            $scope.customers = customer;
        }
    );

    var month = new Array();
    month[0] = "January";
    month[1] = "February";
    month[2] = "March";
    month[3] = "April";
    month[4] = "May";
    month[5] = "June";
    month[6] = "July";
    month[7] = "August";
    month[8] = "September";
    month[9] = "October";
    month[10] = "November";
    month[11] = "December";
    $scope.month = month;
}

function TimesheetViewCtrl($scope, $routeParams, Timesheet){
    var timesheet = Timesheet.query({'timesheetId': $routeParams.timesheetId},
        function(){
            $scope.timesheet = timesheet;
        }
    );
}
