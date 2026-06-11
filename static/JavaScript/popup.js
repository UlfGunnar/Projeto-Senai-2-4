function openPopup(id, botao) {
  const idConsulta = botao.dataset.id;

  if (id === 'overlay1') {
    document.getElementById('id_concluir').value = idConsulta;
  } else if (id === 'overlay2') {
    document.getElementById('id_deletar').value = idConsulta;
  }

  document.getElementById(id).classList.add('open');
}

function closePopup(id) {
  document.getElementById(id).classList.remove('open');
}

// Fechar clicando fora — funciona para todos os overlays
document.querySelectorAll('.overlay').forEach(overlay => {
  overlay.addEventListener('click', function(e) {
    if (e.target === this) closePopup(this.id);
  });
});