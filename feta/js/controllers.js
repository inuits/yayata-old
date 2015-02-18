function TimesheetListCtrl($scope, Timesheet, $location){
    var timesheet = Timesheet.query({},
        function(){
            $scope.timesheets = timesheet;
        }
    );
    $scope.lock = function(timesheet){
        Timesheet.update({'id': timesheet.id, 'locked': !timesheet.locked}).$promise.then(
            function(data){
                timesheet.locked = data.locked;
            }
            )
    }
    $scope.open = function(data){
        $location.path('/timesheet/'+data)
    }
}

function LogoutCtrl($scope, $location, api, $cookieStore) {
    $cookieStore.remove('token');
    api.init();
    $location.path('/login');
};


function LoginCtrl($rootScope, $scope, Login, Me, api, $cookies,$location) {
    $scope.use_cookies = false;

    $scope.login = function(){
        login_trial = Login.login({'username': $scope.username, 'password': $scope.password}).$promise.then(function(data) {
            api.init(data['token']);
            if ($scope.use_cookies){
                $cookies['token'] = data['token'];
            }
            $location.path('/');
        },
        function (data){
            $scope.errors=data.data;
            api.init();
        }
        )
    };
};

function TimesheetNewCtrl($scope, Customer, Project, Timesheet, Company, $location){
    var project = Project.query({}, function(){ $scope.projects = project; });
    var customer = Customer.query({}, function(){ $scope.customers = customer; });
    var company = Company.query({}, function(){ $scope.companies = company; });
    $scope.errors = {};
    $scope.create = function(){
        Timesheet.create($scope.timesheet).$promise.then(
            function(data){
                $location.path('/timesheet/'+data.id)
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
    $scope.monthonly = new Date().getMonth();
    var currentYear = new Date().getFullYear(), years = [];
    startYear = 2007;
    while ( startYear <= currentYear + 1 ) {
        years.push(startYear++);
    }
    $scope.years = years;
    $scope.year = currentYear;
}

function TimesheetViewCtrl($scope, $routeParams, Timesheet, Hour){
   Timesheet.get({'timesheetId': $routeParams.timesheetId},
        function(data){ $scope.timesheet = data; });
   Hour.get({'tid': $routeParams.timesheetId},
        function(data){ $scope.hours = data; });
    $scope.add = function(){
        Hour.create(angular.extend({'tid': $scope.timesheet.id},$scope.hour),
                function(data){
                    $scope.hours.push(data);
                });
    }
}
