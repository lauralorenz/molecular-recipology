(function() {
    var app = angular.module('recipes', []);

     app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
      });

    app.controller('recipeCtrl', function () {

        this.ingredients = ingredients;
        this.scale = function(ml, density,moldb_average_mass){
            return (density * ml) / moldb_average_mass;
        };

    });

   var ingredients = [
    {
        "compound_id": 753,
        "average_content_mg": 0,
        "name": "Ethanol",
        "moldb_average_mass": "46.0684",
        "density": "0.79"
    },
    {
        "compound_id": 3011,
        "average_content_mg": 0,
        "name": "Dodecanoicacid",
        "moldb_average_mass": "200.3178",
        "density": "200.88"
    },
    {
        "compound_id": 3337,
        "average_content_mg": 0,
        "name": "Octanoicacid",
        "moldb_average_mass": "144.2114",
        "density": "0.91"
    },
    {
        "compound_id": 8052,
        "average_content_mg": 0,
        "name": "Heptanoicacid",
        "moldb_average_mass": "130.1849",
        "density": "0.92"
    },
    {
        "compound_id": 12030,
        "average_content_mg": 0.00175,
        "name": "Decanoicacid",
        "moldb_average_mass": "172.2646",
        "density": "4400.89"
    },
    {
        "compound_id": 12065,
        "average_content_mg": 0,
        "name": "Butanoicacid",
        "moldb_average_mass": "88.1051",
        "density": "0.96"
    },
    {
        "compound_id": 12193,
        "average_content_mg": null,
        "name": "Allicin",
        "moldb_average_mass": "162.273",
        "density": "1.11"
    },
    {
        "compound_id": 12199,
        "average_content_mg": null,
        "name": "Di-2-propenyldisulfide,9CI",
        "moldb_average_mass": "146.274",
        "density": "1.01"
    },
    {
        "compound_id": 12465,
        "average_content_mg": 0.0213333333333,
        "name": "alpha-Linolenicacid",
        "moldb_average_mass": "278.4296",
        "density": "0.92"
    },
    {
        "compound_id": 12763,
        "average_content_mg": 0.299,
        "name": "(Z,Z)-9,12-Octadecadienoicacid",
        "moldb_average_mass": "280.4455",
        "density": "0.9"
    },
    {
        "compound_id": 13393,
        "average_content_mg": 32.5325,
        "name": "Water",
        "moldb_average_mass": "18.0153",
        "density": "3.981"
    },
    {
        "compound_id": 13900,
        "average_content_mg": 0,
        "name": "Hexanoicacid",
        "moldb_average_mass": "116.1583",
        "density": "0.93"
    },
    {
        "compound_id": 15392,
        "average_content_mg": null,
        "name": "Di-2-propenylsulfide",
        "moldb_average_mass": "114.209",
        "density": "0.89"
    }
]
})();