#1. Registrar usuario
#2. Ver usuarios
#3. Buscar usuario
#4. Eliminar usuario
#5. Salir


class Solution():
    def __init__(self):
        self.usuarios = []

    def menu_usuarios(self):
        print("\nGestionar usuarios:")
        print("1. Registrar usuario")
        print("2. Ver usuarios")
        print("3. Buscar usuario")
        print("4. Eliminar usuario")
        print("5. Salir")

    def registrar_usuario(self):
        nombre = input("ingresa tu nombre de usuario: ")
        edad = int(input("ingresa tu edad: "))
        corre = input("ingresa tu correo: ")
        usuario = {"nombre": nombre, "edad": edad, "correo": corre}
        self.usuarios.append(usuario)
    
    def ver_usuarios(self):
        if not self.usuarios:
            print("no hay usuarios registrados.")
            return
        print("\nUsuarios registrados:")
        for idx, usuario in enumerate(self.usuarios, start=1):
            print(f"{idx}. Nombre: {usuario['nombre']}, Edad: {usuario['edad']}, Correo: {usuario['correo']}")

    def buscar_usuario(self):
        nombre_buscar = input("ingrese el nombre del usuario que desee buscar: ")
        encontrados = [usuario for usuario in self.usuarios if usuario["nombre"] == nombre_buscar]
        if encontrados:
            for usuario in encontrados:
                print(f"Usuario encontrado: Nombre: {usuario['nombre']}, Edad: {usuario['edad']}, Correo: {usuario['correo']}")
        else:
            print("Usuario no encontrado.")

    def eliminar_usuario(self):
        self.ver_usuarios()
        nombre_eliminar = input("Ingrese el nombre del usuario que desea eliminar: ")
        for i, usuario in enumerate(self.usuarios):
            if usuario["nombre"] == nombre_eliminar:
                del self.usuarios[i]
                print(f"Usuario '{nombre_eliminar}' eliminado.")
                return
        print("Usuario no encontrado.")

    def run(self):
        while True:
            self.menu_usuarios()
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.registrar_usuario()
            elif opcion == "2":
                self.ver_usuarios()
            elif opcion == "3":
                self.buscar_usuario()
            elif opcion == "4":
                self.eliminar_usuario()
            elif opcion == "5":
                print("Saliendo del gestor de usuarios.")
                break
            else:
                print("Opción inválida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    app = Solution()
    app.run()


        
