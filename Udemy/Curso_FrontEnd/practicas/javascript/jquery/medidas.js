$(document).ready(function() {
    var titulo = $('#titulo');
    var info = $('#info');

    info.append('Ancho: ' + titulo.width() + '<br />');
    info.append('Ancho interno: ' + titulo.innerWidth() + '<br />');
    info.append('Ancho externo: ' + titulo.outerWidth() + '<br />');
    info.append('Ancho externo completo: ' + titulo.outerWidth(true) + '<br />');


    info.append('alto: ' + titulo.height() + '<br />');
    info.append('alto interno: ' + titulo.innerHeight() + '<br />');
    info.append('alto externo: ' + titulo.outerHeight() + '<br />');
    info.append('alto externo completo: ' + titulo.outerHeight(true) + '<br />');
});