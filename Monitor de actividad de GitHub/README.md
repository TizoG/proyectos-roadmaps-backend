# 📢 MONITOR DE ACTIVIDAD DE GITHUB (CLI)

## 🎯 Descripción del Proyecto

Este proyecto consiste en desarrollar una aplicación de **línea de comandos (CLI)** que permita consultar la actividad reciente de un usuario de **GitHub** y mostrarla directamente en la terminal. Es una excelente práctica para mejorar habilidades de **manejo de API, manipulación de datos JSON y desarrollo de aplicaciones CLI**.

---

## ⚡ Funcionalidades

La aplicación debe permitir:

-   Ingresar el **nombre de usuario de GitHub** como argumento al ejecutar la CLI.
    ```bash
    github-activity <usuario>
    ```
-   Consultar la actividad reciente del usuario utilizando la **API de GitHub**.
    -   Endpoint: `https://api.github.com/users/<usuario>/events`
    -   Ejemplo: `https://api.github.com/users/octocat/events`
-   Mostrar en la terminal los eventos recientes de la cuenta consultada, como:
    ```bash
    - Realizó 3 commits en octocat/my-repo
    - Creó un nuevo issue en octocat/my-repo
    - Dio estrella a octocat/awesome-project
    ```
-   Manejar errores de manera adecuada, por ejemplo:
    -   Usuario no válido.
    -   Errores en la conexión con la API.
    -   Límite de solicitudes de la API alcanzado.

---

## 📌 Requisitos

-   La aplicación debe ejecutarse **exclusivamente desde la línea de comandos**.
-   Se debe utilizar cualquier **lenguaje de programación** a elección del desarrollador.
-   No está permitido el uso de **librerías externas** para la conexión con la API.
-   El código debe ser **claro y estructurado**, asegurando un buen manejo de errores.

---

## 🚀 Características Avanzadas (Opcionales)

Si deseas mejorar aún más la aplicación, aquí tienes algunas ideas:

-   **Filtrar eventos** por tipo (commits, stars, issues, etc.).
-   **Formatear la salida** para que sea más legible y estructurada.
-   **Implementar almacenamiento en caché** para reducir el número de llamadas a la API y mejorar el rendimiento.
-   **Explorar otros endpoints de la API de GitHub** para obtener información extra, como detalles de los repositorios o estadísticas del usuario.

---

## 🌍 Recursos Adicionales

Para conocer más sobre la API de GitHub y sus funcionalidades, puedes visitar su documentación oficial:
🔗 [GitHub API Documentation](https://docs.github.com/en/rest)

---

¡Anímate a desarrollar este proyecto y mejorar tus habilidades en el uso de API y desarrollo CLI! 🚀
