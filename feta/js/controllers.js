function TimesheetListCtrl($scope, Timesheet){
    var timesheet = Timesheet.query({},
        function(){
            $scope.timesheets = timesheet;
        }
    );
}

function LogoutCtrl($scope, $location, api, $cookieStore) {
    $cookieStore.remove('token');
    api.init();
    $location.path('/login');
};


function LoginCtrl($scope, Login, api, $cookies,$location) {
    $scope.login = function(){
        login_trial = Login.login({'username': $scope.username, 'password': $scope.password}).$promise.then(function(data) {
            api.init(data['token']);
            $cookies['token']=data['token'];
            $location.path('/');
        })
    };
};

function TimesheetNewCtrl($scope, Customer, Project, Timesheet, Company){
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
    var company = Company.query({},
        function(){
            $scope.companies = company;
        }
    );

    $scope.fields = ['project', 'company', 'month']

    $scope.styles = {};

    var resetStyles = function(){
        for (i = 0; i < $scope.fields.length; i++) { 
            $scope.styles[$scope.fields[i]] = "";
        }
    }

    $scope.errors = {};

    $scope.create = function(){Timesheet.create($scope.timesheet).$promise.then(function(data){
        console.log(data);
    },
        function(data){
            $scope.errors=data.data;
            resetStyles();
            for (i = 0; i < $scope.fields.length; i++) {
            if ($scope.fields[i] in data.data){
                $scope.styles[$scope.fields[i]] = {"color":"red"};
            }
            }
        }
    )};

    var month = {};
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
    $scope.thismonth = new Date().getMonth();
    var currentYear = new Date().getFullYear(), years = [];
    startYear = 2007;
    while ( startYear <= currentYear + 1 ) {
        years.push(startYear++);
    }
    $scope.years = years;
    $scope.currentyear = currentYear;
}

function TimesheetViewCtrl($scope, $routeParams, Timesheet){
    var timesheet = Timesheet.query({'timesheetId': $routeParams.timesheetId},
        function(){
            $scope.timesheet = timesheet;
        }
    );
}
