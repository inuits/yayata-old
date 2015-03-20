Array.prototype.sum = function (prop) {
        var total = 0
            for ( var i = 0, _len = this.length; i < _len; i++ ) {
                if (this[i][prop] != null) {
                total += parseFloat(this[i][prop])
                }
            }
        return total
}

function CompanyListCtrl($scope, Company, $location){
    var companies = Company.query({},
        function(){
            $scope.companies = companies;
        }
    );
    $scope.open = function(data){
        $location.path('/company/'+data)
    }
}
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
    $scope.submitted = false;

    $scope.login = function(){
        $scope.submitted = true;
        login_trial = Login.login({'username': $scope.username, 'password': $scope.password}).$promise.then(function(data) {
            $rootScope.errors = [];
            $scope.submitted = false;
            api.init(data['token']);
            if ($scope.use_cookies){
                $cookies['token'] = data['token'];
            }
            $location.path('/');
        },
        function (data){
            $scope.submitted = false;
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
            }
    )};

    var month = {};
    month[1] = "January";
    month[2] = "February";
    month[3] = "March";
    month[4] = "April";
    month[5] = "May";
    month[6] = "June";
    month[7] = "July";
    month[8] = "August";
    month[9] = "September";
    month[10] = "October";
    month[11] = "November";
    month[12] = "December";
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
    $scope.edithour = false;
    var days = {};
    days[0] = "Monday";
    days[1] = "Tuesday";
    days[2] = "Wednesday";
    days[3] = "Thursday";
    days[4] = "Friday";
    days[5] = "Saturday";
    days[6] = "Sunday";
    $scope.days = days;

    $scope.stopEditing = function() {
        $scope.newhour.id = false;
        $scope.edithour = false;
    }
    $scope.newhour = {};
    Timesheet.get({'timesheetId': $routeParams.timesheetId},
            function(data){ $scope.timesheet = data; });
    $scope.get_hours = function() {
    Hour.get({'tid': $routeParams.timesheetId},
            function(data){ $scope.hours = data; });
    }
    $scope.get_hours()
    $scope.add = function(){
        Hour.create(angular.extend({'tid': $scope.timesheet.id},$scope.newhour),
            function(data){
            $scope.errors={};
                $scope.hours.push(data);
                $scope.newhour.day = parseInt($scope.newhour.day)+1;
            },
            function(data){
                $scope.errors=data.data;
            }
        );
    }
    $scope.updatehour = function(hour){
        Hour.update(angular.extend({'tid': $scope.timesheet.id, 'hid': hour.id}, hour),
            function(data){
              $scope.get_hours();
              $scope.stopEditing();
            }
        );
    }
    $scope.deletehour = function(hour){
        Hour.delete({timesheet: $scope.timesheet.id, hour: hour.id},
            function(data){
                var idx = $scope.hours.indexOf(hour);
                $scope.hours.splice(idx,1);
                $scope.stopEditing();
            }
        );
    }
    $scope.lock = function(timesheet){
        Timesheet.update({'id': timesheet.id, 'locked': !timesheet.locked}).$promise.then(
            function(data){
                timesheet.locked = data.locked;
            }
            )
    }
}
