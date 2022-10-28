$(document).ready(function(){

// Traduction en francais
$('#greetingFR').click(function(){
    $('#greeting').html("BONJOUR, JE SUIS FLORIAN, DÉVELOPPEUR DE WEB FULL STACK QUI AIME DONNER VIE À L'IMAGINATION.");
    $('#idProject').html('Projets');
    $('#idResume').html('CV');
    $('#idContact').html('Me Joindre');
    $('.visitez').html('Visitez');
    $('.codeSource').html('Code Source');

    // CV Francais
    $("#idResume").attr("href", "static/Florian-FR.pdf")

    // Description Projet 1
    $('#Project1Description').html("Réseau social qui permet aux utilisateurs de publier des messages, de suivre d'autres utilisateurs et d'aimer des messages, d'ajouter et de modifier un profil et une image de couverture, en utilisant Python, JavaScript, HTML et CSS.")

    // Description Projet 2
    $('#Project2Description').html("Simulateur d'application Web de trading de bourse et de crypto-monnaie. Fait pour les investisseurs curieux inexpérimentés, pour apprendre et pratiquer sans risque. Vous commencez avec 10.000$ et avez accès à des vrais stocks et prix !")

    // Description Projet 3
    $('#Project3Description').html("Projet d'encyclopédie en ligne qui se compose d'un certain nombre d'entrées d'encyclopédie sur divers sujets. Les entrées d'encyclopédie sont stockées à l'aide d'un langage de balisage appelé Markdown. Les utilisateurs peuvent créer, modifier et rechercher différentes entrées.")

    // Description Projet 4
    $('#Project4Description').html("Site d'enchères de commerce électronique de type eBay qui permet aux utilisateurs de publier des annonces d'enchères, de placer des enchères sur des annonces, de commenter ces annonces et d'ajouter des annonces à une << liste de surveillance >>.")

    // Description Projet 5
    $('#Project5Description').html("Un site front-end pour un client de messagerie qui effectue des appels d'API pour envoyer et recevoir des e-mails.")

    // Me Joindre
    $('#hideH2').html('Me Joindre');
    $('#nom').html('Nom');
    $('#courriel').html('Courriel');
    $('#sendMessage').val('Envoyez');
    $('#resetForm').val('Réinitialiser');
})
});
