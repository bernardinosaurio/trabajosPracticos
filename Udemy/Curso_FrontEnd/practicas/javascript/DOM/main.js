var cajas = document.getElementsByTagName('div');

var primeraCaja = document.getElementById('primeraCaja');

///primeraCaja.innerHTML = '<u>Hola Mundo</u>';

var caja = document.createElement('div');
var contenido = document.createTextNode('Hola Mundo');
caja.appendChild(contenido);


var contenedor = document.getElementById('contenedor');
contenedor.appendChild(caja);
caja.id = 'primera';
caja.className = 'caja naranja';
var padre = cajas[0].parentNode;
padre.insertBefore(caja, primeraCaja);