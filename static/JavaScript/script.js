document.getElementById('exibir_senha').addEventListener('change', function() {
    const campo = document.getElementById('senha');
    campo.type = this.checked ? 'text' : 'password';
})