function abrirModal(cod) {
    const modal = document.getElementById('modalEliminar');
    const form = document.getElementById('formEliminar');
    form.action = `/eliminar_profesor/${cod}`; // POST apunta al profesor correcto
    modal.style.display = "block"; 
}

function cerrarModal() {
    const modal = document.getElementById('modalEliminar');
    modal.style.display = "none";
}

// cerrar modal si se hace clic fuera de él
window.onclick = function(event) {
    const modal = document.getElementById('modalEliminar');
    if (event.target == modal) {
        modal.style.display = "none";
    }
}