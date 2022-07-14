$(document).ready(function(){
   //$('.basket_list input[type=number]').click(function(){
   //$('.basket_list').on(types: 'click', selector: 'input[type=number]', data: function(){
   $('.basket_list').on('click', 'input[type=number]', function(){
        let pk = event.target.name;
        let quantity = event.target.value;
        //$.ajax(url: {
        $.ajax({
            url: '/basket/edit/' + pk + '/' + quantity + '/',
            success: function(data){
                $('.basket_list').html(data.result);
                //console.log(data);
            }
        });
    });
});
