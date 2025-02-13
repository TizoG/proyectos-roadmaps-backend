---

## GESTOR DE TAREAS EN LA TERMINAL

Este proyecto consiste en una aplicación de línea de comandos (CLI) diseñada para gestionar tareas de manera eficiente. Permitirá registrar, actualizar y organizar actividades en distintas categorías, ofreciendo una forma sencilla de visualizar el estado de cada una. A través de este ejercicio, se podrán practicar habilidades clave como el manejo de archivos, la interacción con el usuario mediante la terminal y la gestión de datos en formato JSON.

### 📌 FUNCIONALIDADES

El sistema debe ejecutarse desde la terminal y procesar comandos del usuario para gestionar un listado de tareas almacenadas en un archivo JSON. La aplicación debe permitir:

- **Añadir, modificar y eliminar tareas**
- **Marcar tareas como pendientes, en progreso o completadas**
- **Listar todas las tareas disponibles**
- **Filtrar tareas según su estado** (pendientes, en progreso, completadas)

#### 🔹 Consideraciones para la implementación

- Se puede utilizar cualquier lenguaje de programación.
- La entrada de comandos debe realizarse mediante argumentos en la terminal.
- Las tareas deben almacenarse en un archivo JSON en el directorio del proyecto.
- Si el archivo JSON no existe, la aplicación debe crearlo automáticamente.
- No se deben emplear bibliotecas externas para gestionar los datos o la lógica de la CLI.
- Se deben manejar adecuadamente los errores y casos excepcionales.

### 📋 ESTRUCTURA DE UNA TAREA

Cada tarea almacenada debe incluir la siguiente información:

- **ID**: Identificador único de la tarea.
- **Descripción**: Texto breve que explique la tarea.
- **Estado**: Puede ser "pendiente", "en progreso" o "completada".
- **Fecha de creación**: Registro de la fecha y hora en que se creó la tarea.
- **Última actualización**: Momento en que la tarea fue editada por última vez.

El archivo JSON debe actualizarse correctamente con cada modificación en la lista de tareas.

---

### 🚀 CÓMO EMPEZAR

1️⃣ **Configuración inicial**

- Escoge un lenguaje de programación con el que te sientas cómodo.
- Asegúrate de contar con un editor de código o entorno de desarrollo adecuado.

2️⃣ **Estructura del proyecto**

- Crea una carpeta para almacenar los archivos del proyecto.
- Configura un sistema de control de versiones como Git.

3️⃣ **Implementación de funcionalidades**

- Define la estructura básica de la CLI y la forma en que procesará los comandos.
- Implementa cada función de manera progresiva, validando su correcto funcionamiento.

4️⃣ **Pruebas y depuración**

- Asegúrate de que cada comando actúe como se espera.
- Verifica que los datos se almacenen y actualicen correctamente en el archivo JSON.
- Corrige cualquier error o comportamiento inesperado antes de finalizar.

5️⃣ **Entrega y documentación**

- Confirma que todas las funciones requeridas están implementadas.
- Mejora la estructura del código y añade comentarios cuando sea necesario.
- Escribe una guía clara en el README explicando cómo usar la aplicación.

---

## 🛠 CÓMO CLONAR EL REPOSITORIO Y CONTRIBUIR

Si deseas participar en este proyecto con tu propia solución, sigue estos pasos:

### 1️⃣ Clonar el repositorio

Abre una terminal y ejecuta el siguiente comando para clonar el repositorio en tu máquina:

```bash
git clone https://github.com/tu-usuario/nombre-del-repositorio.git
```

Luego, entra en la carpeta del proyecto:

```bash
cd nombre-del-repositorio
```

### 2️⃣ Crea una nueva rama para tu solución

Antes de empezar a trabajar, crea una nueva rama con tu nombre o una descripción de la solución:

```bash
git checkout -b mi-solucion
```

### 3️⃣ Implementa tu solución

Añade tu código dentro de una nueva carpeta con tu nombre de usuario de GitHub o una breve descripción de tu enfoque.

Ejemplo:

```
📂 soluciones
 ├── 📂 usuario-ejemplo
 │   ├── 📄 main.py
 │   ├── 📄 README.md
 │   ├── 📄 tareas.json
```

### 4️⃣ Sube tu solución al repositorio

Guarda los cambios y súbelos a tu rama en GitHub:

```bash
git add .
git commit -m "Mi solución al gestor de tareas"
git push origin mi-solucion
```

### 5️⃣ Crea un Pull Request (PR)

- Ve a tu repositorio en GitHub.
- Haz clic en el botón **"Compare & pull request"**.
- Escribe una breve descripción de tu solución y envía el PR.

Cuando tu contribución sea revisada y aprobada, se fusionará con el proyecto principal.

---

¡Anímate a participar y mejorar el gestor de tareas con tu propia versión! 🚀💡

---
