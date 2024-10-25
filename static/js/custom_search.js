$(document).ready(function () {
    var initial_car_brand = $("#id_car_brand").val();  
    var initial_car_model = $("#id_car_model").val();  
    if (initial_car_brand) {
        $.ajax({
            url: loadCarModelsUrl,
            data: {
                'car_brand': initial_car_brand
            },
            success: function (data) {
                $("#id_car_model").html(data); 
                if (initial_car_model) {
                    $("#id_car_model").val(initial_car_model);
                }
            }
        });
    }
    $("#id_car_brand").change(function () {
        
        var brandId = $(this).val();  

        $.ajax({
            url: loadCarModelsUrl,
            data: {
                'car_brand': brandId
            },
            success: function (data) {
                $("#id_car_model").html(data);  
            }
        });
    });
});