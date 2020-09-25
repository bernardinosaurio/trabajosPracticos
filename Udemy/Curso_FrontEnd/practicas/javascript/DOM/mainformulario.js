var formulario = document.getElementById('formulario');
var nombre = formulario.nombre;
var sexo = formulario.sexo;
var terminos = formulario.terminos;

function validar(e) {
    if (nombre.value > 18) {
        alert('Maximo de caracteres permitidos');
    } else if (nombre.value == '') {
        alert('por favor ingresa un nombre')
    }
    if (sexo[0].checked == false && sexo[1].checked == false) {
        alert('por favor elige sexo')
    }
    if (!terminos.checked) {
        alert('acepta los terminos y condiciones')

    }

    e.preventDefault();

}

formulario.addEventListener('submit', validar);