$(document).ready(function() {
    $('#sendMessage').on('click', function(event) {

        /* This is our Ajax Call */
        $.ajax({
            data : {
                name : $('#name').val(),
                email : $('#email').val(),
                message : $('#message').val(),
                 'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
            },
            /* Here we specify the request */
            type : 'POST',
            /* The route that we created */
            url : 'http://florian-b.herokuapp.com/ajax_test'
        })
        /* Here we specify what happends after the ajax call is complete.
        We'll use the .done function */
        .done(function(data) { /* If error exists */
            if (data.error){
              alert('not working');
            }
            else { /* If error doesnt exist */
                $('form').hide();
                if ($('#nom').html() == 'Envoyez'){
                $('#formtitle').html('Je vous reviendrai le plutôt possible.');

                }
                else {
                $('#formtitle').html('I will get back to you shortly!');
                }
                $('#contactForm').css("background-color","rgba(237,242,243,255)");
                $('#hideH2').hide();
            }
        });

        event.preventDefault(); /* Prevents the form from doing what it typically does, submit the form its way */
    });
});