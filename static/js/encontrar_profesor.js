document.addEventListener("DOMContentLoaded", function() {
    const input = document.getElementById("profesor");
    const profesores = document.querySelectorAll(".profesor-card"); // selecciona todas las tarjetas

    input.addEventListener("input", function() {
        const filtro = input.value.toLowerCase().trim();

        profesores.forEach(function(profesor) {
            const nombre = profesor.querySelector(".nombre").textContent.toLowerCase();
            if(nombre.includes(filtro)) {
                profesor.style.display = ""; // mostrar
            } else {
                profesor.style.display = "none"; // ocultar
            }
        });
    });
});
