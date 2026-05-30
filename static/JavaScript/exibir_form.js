const consultaResidencial = document.getElementById('consulta_residencial');
if (consultaResidencial) {
    consultaResidencial.addEventListener('change', function() {
        const campo = document.getElementById('form_endereco');
        const checkbox = document.getElementById('proprio_endereco');

        campo.style.display = this.checked ? 'block' : 'none';
        checkbox.style.display = this.checked ? 'block' : 'none';
    });
}

const option_especie = document.getElementById('option_especie');
if (option_especie) {
    option_especie.addEventListener('change', function() {
        const campo = document.getElementById('form_especie');
        campo.style.display = this.value === '0' ? 'block' : 'none';
    });
}

