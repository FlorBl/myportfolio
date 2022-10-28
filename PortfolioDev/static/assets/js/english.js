$(document).ready(function(){

// English translation
$('#greetingEN').click(function(){
    $('#greeting').html("HI, I'M FLORIAN, A FULL STACK WEB DESIGNER & DEVELOPER THAT LOVES TO BRING IMAGINATION TO LIFE.");
    $('#idProject').html('Projects');
    $('#idResume').html('Resume');
    $('#idContact').html('Contact');
    $('.visitez').html('Visit');
    $('.codeSource').html('Source Code');

    // English Resume
    $("#idResume").attr("href", "static/Florian-EN.pdf")

    // Description Projet 1
    $('#Project1Description').html("Social network that allows users to make posts, follow other users, and “like” posts, add and change a profile and cover image, using Python, JavaScript, HTML, and CSS.")

    // Description Projet 2
    $('#Project2Description').html("Stock Market and Cryptocurrency trading web app simulator. Made for curious inexperienced investors, to learn and practice without risk. You start with 10.000$ and have access to real stocks and prices!")

    // Description Projet 3
    $('#Project3Description').html("Online encyclopedia project that consists of a number of encyclopedia entries on various topics. Encyclopedia entries are stored using a markup language called Markdown. Users can create, modify and search different entries!")

    // Description Projet 4
    $('#Project4Description').html('eBay-like e-commece auction site that allows users to post auction listings, place bids on listings, comment on those listings, and add listings to a "watchlist".')

    // Description Projet 5
    $('#Project5Description').html("A front-end for an email client that makes API calls to send and receive emails.")

    // Contact Form
    $('#hideH2').html('Contact');
    $('#nom').html('Name');
    $('#courriel').html('Email');
    $('#sendMessage').val('Send Message');
    $('#resetForm').val('Reset');
})
});
