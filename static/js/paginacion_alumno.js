const listaAlumnos = document.getElementById('listaAlumnos');
const alumnos = Array.from(listaAlumnos.children);
const prevBtn = document.getElementById('prev');
const nextBtn = document.getElementById('next');
const paginaActualSpan = document.getElementById('paginaActual');
const totalPaginasSpan = document.getElementById('totalPaginas');

const alumnosPorPagina = 5;
let paginaActual = 1;
const totalPaginas = Math.ceil(alumnos.length / alumnosPorPagina);
totalPaginasSpan.textContent = totalPaginas;

// Función para mostrar solo los alumnos de la página actual
function mostrarPagina(pagina) {
    const inicio = (pagina - 1) * alumnosPorPagina;
    const fin = inicio + alumnosPorPagina;
    
    alumnos.forEach((alumno, index) => {
        alumno.style.display = index >= inicio && index < fin ? 'block' : 'none';
    });

    paginaActualSpan.textContent = pagina;
    prevBtn.disabled = pagina === 1;
    nextBtn.disabled = pagina === totalPaginas;
}

// Eventos de botones
prevBtn.addEventListener('click', () => {
    if (paginaActual > 1) {
        paginaActual--;
        mostrarPagina(paginaActual);
    }
});

nextBtn.addEventListener('click', () => {
    if (paginaActual < totalPaginas) {
        paginaActual++;
        mostrarPagina(paginaActual);
    }
});

// Inicializar
mostrarPagina(paginaActual);