function abrirModal(cod) {
    const modal = document.getElementById('modalEliminar');
    const form = document.getElementById('formEliminar');
    form.action = `/eliminar_alumno/${cod}`; // aquí el POST apunta al curso correcto
    modal.style.display = "block"; // mostrar modal
}

function cerrarModal() {
    const modal = document.getElementById('modalEliminar');
    modal.style.display = "none";
}

// cerrar si se hace clic fuera del modal
window.onclick = function(event) {
    const modal = document.getElementById('modalEliminar');
    if (event.target == modal) {
        modal.style.display = "none";
    }
}