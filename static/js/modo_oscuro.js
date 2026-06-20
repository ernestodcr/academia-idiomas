const toggle = document.getElementById('toggleDarkMode');
        toggle.addEventListener('click', () => {
            document.body.classList.toggle('dark-mode');

            // Guardar preferencia
            if (document.body.classList.contains('dark-mode')) {
                localStorage.setItem('modoOscuro', 'true');
            } else {
                localStorage.setItem('modoOscuro', 'false');
            }
        });

        // Mantener preferencia al recargar
        if (localStorage.getItem('modoOscuro') === 'true') {
            document.body.classList.add('dark-mode');
        }