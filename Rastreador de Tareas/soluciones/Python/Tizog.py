# Importamos la libreria datetime para manejar las fechas y horas
import datetime

# Creamos la clase GestroTareas para gestionar tareas


class GestorTareas:
    # Creamos el constructor de la clase para inicializar las variables
    def __init__(self):
        # Creamos las variables para almacenar tareas y estados
        self.tareas = []  # lista para almacenar tareas
        self.estado = ["pendiente", "en progreso",
                       "completada"]  # lista de estados posibles
        self.id = 1  # identificador unico para cada tarea

# Creamos los metodos
# Metodo para agregar tareas
    def agregar_tarea(self, tarea, descripcion, estado):
        """"
        Agrega una nueva tarea con titulo, descripcion y estado.
        Args:
            tarea(str): titulo de la tarea
            descripcion(str): descripcion de la tarea
            estado(str): estado de la tarea
        """
        # Comprobamos que el estado sea correcto
        if estado not in self.estado:
            print("debes introducir un estado correcto.")
        else:
            # Creamos la tarea con la fecha actual y la agregamos a la lista
            fecha_actual = datetime.datetime.now()
            self.tareas.append(
                {
                    "ID": self.id,
                    "Titulo": tarea,
                    "Descripcion": descripcion,
                    "Fecha": fecha_actual.strftime("%d/%m/%Y %H:%M:%S"),
                    "Estado": estado

                })
            print("Tarea agregada.")
            self.id += 1  # incrementamos el id

# Metodo para modificar tareas
    def modificar_tarea(self, titulo, descripcion, estado):
        """
        Modifica una tarea existente con el tiitulo, descripcion y estado
        Args:
            titulo(str): titulo de la tarea
            descripcion(str): descripcion de la tarea
            estado(str): estado de la tarea
        """
        # Modificamos la tarea si existe
        for tarea in self.tareas:
            if tarea["Titulo"] == titulo:
                if descripcion:
                    tarea["Descripcion"] = descripcion
                if estado:
                    tarea["Estado"] = estado
                print(f"Tarea {tarea["ID"]} modificada.")

# Metodo para eliminar tareas
    def eliminar_tarea(self, titulo):
        """
        Elimina una tarea existente con titulo
        Args:
            titulo(str): titulo de la tarea
        """
        # Eliminamos la tarea si existe
        for tarea in self.tareas:
            if tarea["Titulo"] == titulo:
                self.tareas.remove(tarea)
                print(f" {tarea["Titulo"]} ha sido eliminada.")

#   Metodo para mostrar tareas
    def mostrar_tareas(self):
        # Mostramos las tareas
        for tarea in self.tareas:
            print(
                f"\nID: {tarea["ID"]}\nTitutlo: {tarea["Titulo"]}\nDescripcion: {tarea["Descripcion"]}\nFecha: {tarea["Fecha"]}\nEstado: {tarea["Estado"]}")


# Creamos un objeto GestorTareas
gestor = GestorTareas()

# Creamos un menu para interactuar con el objeto GestorTareas
while True:
    print("\n======== MENU ========\n")
    print("1. Agregar tarea")
    print("2. Modificar tarea")
    print("3. Mostrar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")

    options = input("Seleccione una opcion: ")
    match options:
        case "1":
            titulo = input("Introduce el titulo de la tarea: ")
            descripcion = input("Introduce la descripcion de la tarea: ")
            estados = input(
                "Introduce el estado de la tarea (pendiente, en progreso, completada): ")
            gestor.agregar_tarea(titulo, descripcion, estados)
        case "2":
            titulo = input("Introduce el titulo de la tarea: ")
            descripcion = input("Introduce la descripcion de la tarea: ")
            estados = input(
                "Introduce el estado de la tarea (pendiente, en progreso, completada): ")
            gestor.modificar_tarea(titulo, descripcion, estados)
        case "3":
            gestor.mostrar_tareas()
        case "4":
            titulo = input("Introduce el titulo de la tarea: ")
            gestor.eliminar_tarea(titulo)
        case "5":
            print("Saliendo...")
            break
        case _:
            print("Opcion no valida.")
