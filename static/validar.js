// Validar
function isValidate() {
    var mail = document.getElementById('user_email').value;
    var expression = /\w+@\w+\.+[a-z]/;
    if (!expression.test(mail) || mail === "") {
        alert('Correo no válido');
        return false;
    } else {
        alert('Infomación enviada al correo');
        return true;
    }
}