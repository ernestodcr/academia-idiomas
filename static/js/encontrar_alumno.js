document.addEventListener("DOMContentLoaded", function() {
    const input = document.getElementById("alumno");
    const alumnos = document.querySelectorAll(".alumno-card");

    input.addEventListener("input", function() {
        const filtro = input.value.toLowerCase();

        alumnos.forEach(function(alumno) {
            const nombre = alumno.querySelector(".nombre").textContent.toLowerCase();
            if(nombre.includes(filtro)) {
                alumno.style.display = ""; // mostrar
            } else {
                alumno.style.display = "none"; // ocultar
            }
        });
    });
});
