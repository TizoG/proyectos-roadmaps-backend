import datetime


class GestorTareas:
    def __init__(self):
        self.tareas = []
        self.estado = ["pendiente", "en progreso", "completada"]
        self.id = 1

    def agregar_tarea(self, tarea, descripcion, estado):
        if estado not in self.estado:
            print("debes introducir un estado correcto.")
        else:
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
            self.id += 1

    def modificar_tarea(self, titulo, descripcion, estado):
        for tarea in self.tareas:
            if tarea["Titulo"] == titulo:
                if descripcion:
                    tarea["Descripcion"] = descripcion
                if estado:
                    tarea["Estado"] = estado
                print(f"Tarea {tarea["ID"]} modificada.")

    def eliminar_tarea(self, titulo):
        for tarea in self.tareas:
            if tarea["Titulo"] == titulo:
                self.tareas.remove(tarea)
                print(f" {tarea["Titulo"]} ha sido eliminada.")

    def mostrar_tareas(self):
        for tarea in self.tareas:
            print(tarea["ID"], tarea["Titulo"],
                  tarea["Descripcion"], tarea["Fecha"], tarea["Estado"])


gestor = GestorTareas()
gestor.agregar_tarea("Tarea 1", "Descripcion 1", "pendiente")
gestor.agregar_tarea("Tarea 2", "Descripcion 2", "en progreso")
gestor.agregar_tarea("Tarea 3", "Descripcion 3", "completada")
gestor.mostrar_tareas()
gestor.modificar_tarea("Tarea 2", "", "completada")
gestor.mostrar_tareas()
gestor.eliminar_tarea("Tarea 2")
gestor.eliminar_tarea("Tarea 3")
gestor.mostrar_tareas()


# Futuros cambios podemos implementar que podamos introducir las tareas desde el teclado
