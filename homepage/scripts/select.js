 $(function() {

  $('#random').on('click', function() {
        //searchTerms = document.getElementById("search").value;
        //window.location.href = '/homepage/shoppingCart.filter/'
        //console.log(searchTerms);
        $.ajax({
            url: '/homepage/select.random_color/',
            success: function(data){
                //$('#colorForm').find('.form-control').html(data)
                document.getElementById("id_Color").value = "#" + data;
                console.log(data);
            },//success
        });//ajax
        
    });//click

});