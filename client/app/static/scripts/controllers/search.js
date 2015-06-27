'use strict';

/**
 * @ngdoc function
 * @name frontendApp.controller:AboutCtrl
 * @description
 * # AboutCtrl
 * Controller of the frontendApp
 */

/////////////////sharedProperties services//////////////////////////
angular.module('frontendApp')
   .factory('sharedPropertyAddress', function () {
      var property = 'Def';

      return {
            getProperty: function () {
                return property;
            },
            setProperty: function(value) {
            property = value;
   }
   };
   });

angular.module('frontendApp')
   .factory('sharedPropertySport', function () {
      var property = 'Def';

      return {
            getProperty: function () {
                return property;
            },
            setProperty: function(value) {
            property = value;
   }
   };
   });

angular.module('frontendApp')
   .factory('sharedPropertyResults', function () {
      var property = 'Def';

      return {
            getProperty: function () {
                return property;
            },
            setProperty: function(value) {
            property = value;
   }
   };
   });
   
 angular.module('frontendApp')
   .factory('sharedPropertyFromMain', function () {
      var property = 'Def';

      return {
            getProperty: function () {
                return property;
            },
            setProperty: function(value) {
            property = value;
   }
   };
   });
/////////////////////////////////////////////////////////////////////
////////////////////////////Custom directive for page reload////////////////////////////////
/* angular.module('frontendApp').directive('xref',function($route, $location){
  return {
    link: function(scope, elm,attr){
      elm.on('click',function(){
        if ( $location.path() === attr.xref ) {
			console.log($location.path());
          $route.reload();
        } else {
          scope.$apply(function(){
            $location.path(attr.xref);
          });
        }      
      });
    }
  };
}); */
/////////////////////////////////////////////////////////////////////





angular.module('frontendApp')
  .controller('searchController', function ($route,$cookies,$location,$templateCache,sharedPropertyAddress,sharedPropertySport,sharedPropertyResults,sharedPropertyFromMain,$http,$scope) {
     console.log('Ctrl Search');
	$scope.place = null
	     console.log(sharedPropertyAddress.getProperty());
      console.log(sharedPropertySport.getProperty());

    console.log(sharedPropertyFromMain.getProperty());
	if(sharedPropertyFromMain.getProperty()=="Y")
	{
			console.log("From main");
			sharedPropertyFromMain.setProperty("N");
	console.log($scope.$$phase);

		 try{
				
					 $scope.$apply();
			}
		catch(err){
				console.log('**********');
			} 

	}


$scope.myFunction = function() {
    sharedPropertySport.setProperty($scope.sport);
    sharedPropertyAddress.setProperty($scope.place);
     console.log(sharedPropertyAddress.getProperty());
      console.log(sharedPropertySport.getProperty());


}; 
  });






angular.module('frontendApp')
  .controller('httpReqController', ['$location','$scope','$cookies', '$http','sharedPropertyAddress','sharedPropertySport','sharedPropertyResults','sharedPropertyFromMain', function( $location,$scope,$http,$cookies,sharedPropertyAddress,sharedPropertySport,sharedPropertyResults,sharedPropertyFromMain) {
    console.log('Ctrol Main');
	console.log($scope.$$phase);
		 if(!$scope.$$phase) {
         scope.$apply();
		}
		try{
				
					 $scope.$apply();
			}
		catch(err){
				console.log('**********');
			} 


$scope.myFunction = function() {
	
    sharedPropertySport.setProperty($scope.sport);


    sharedPropertyAddress.setProperty($scope.place);

    console.log(sharedPropertyAddress.getProperty());
    console.log(sharedPropertySport.getProperty());
	sharedPropertyFromMain.setProperty("Y");
	console.log("i main ctrl");
	console.log(sharedPropertyFromMain.getProperty());
	$location.path( '#/search.html' );

};

}]);



var myApp = angular.module('frontendApp');

function MyController($scope) {
			
			$scope.currentPage = 1;
			$scope.pageSize = 10;
			var venues = [];
			
			/* $scope.venues = [];
			$scope.phoneno = [];
			$scope.timings = []; */
			$scope.results = [];
           			for (var i = 0; i<23;i++) 
					{
						console.log('in the for loop for the '+i+'th time');

						
							var name = 'venue'+i;
							var phone = '99889988'+i;
							var timing = '10AM - 12 PM';
							
							var clubDetails= {
							"name": name,
    						"phone": phone,
    						"timing":timing
							}
			   

							venues.push(clubDetails);
						


					}

			$scope.results = venues;
			

			
  
  
  $scope.pageChangeHandler = function(num) {
      console.log('page changed to ' + num);
  };
}



function OtherController($scope) {
  $scope.pageChangeHandler = function(num) {
    console.log('going to page ' + num);
  };
}

myApp.controller('MyController', MyController);
myApp.controller('OtherController', OtherController);



