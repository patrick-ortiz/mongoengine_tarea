import controlador

# Menús y UI
def menu_usuarios():
    while True:
        print("\n--- Módulo de Usuarios ---")
        print("1. Registrar Usuario (Create)")
        print("2. Consultar Usuarios (Read)")
        print("3. Modificar Usuario (Update)")
        print("4. Eliminar Usuario (Delete)")
        print("5. Regresar al Menú Principal")
        
        opcion = input("Seleccione una opción: ")
        
        try:
            if opcion == '1':
                email = input("Email: ")
                nombre = input("Nombre: ")
                apellido = input("Apellido: ")
                controlador.registrar_usuario(email, nombre, apellido)
                print("Usuario registrado exitosamente.")
                
            elif opcion == '2':
                usuarios = controlador.obtener_usuarios()
                if not usuarios:
                    print("No hay usuarios registrados.")
                for u in usuarios:
                    print(f"[{u.email}] {u.nombre} {u.apellido} (Creado: {u.fecha_creado.strftime('%Y-%m-%d')})")
                    
            elif opcion == '3':
                email = input("Email del usuario a modificar: ")
                nombre = input("Nuevo nombre (dejar en blanco para no cambiar): ")
                apellido = input("Nuevo apellido (dejar en blanco para no cambiar): ")
                controlador.actualizar_usuario(email, nombre, apellido)
                print("Usuario modificado exitosamente.")
                
            elif opcion == '4':
                email = input("Email del usuario a eliminar: ")
                controlador.eliminar_usuario(email)
                print("Usuario eliminado exitosamente.")
                
            elif opcion == '5':
                break
            else:
                print("Opción inválida.")
        except Exception as e:
            print(f"Error: {e}")

def menu_articulos():
    while True:
        print("\n--- Módulo de Artículos ---")
        print("1. Registrar Artículo (Create)")
        print("2. Consultar Artículos (Read)")
        print("3. Modificar Artículo (Update)")
        print("4. Eliminar Artículo (Delete)")
        print("5. Regresar al Menú Principal")
        
        opcion = input("Seleccione una opción: ")
        
        try:
            if opcion == '1':
                nombre = input("Nombre del artículo (Obligatorio): ")
                desc = input("Descripción: ")
                marca = input("Marca: ")
                email = input("Email del usuario que registra (Obligatorio): ")
                controlador.registrar_articulo(nombre, desc, marca, email)
                print("Artículo registrado exitosamente.")
                
            elif opcion == '2':
                articulos = controlador.obtener_articulos()
                if not articulos:
                    print("No hay artículos registrados.")
                for a in articulos:
                    print(f"ID: {a.id} | {a.nombre} - {a.marca} | Modificado por: {a.usuario_modifico.email}")
                    
            elif opcion == '3':
                id_art = input("ID del artículo a modificar: ")
                nombre = input("Nuevo nombre (dejar en blanco para no cambiar): ")
                desc = input("Nueva descripción (dejar en blanco para no cambiar): ")
                marca = input("Nueva marca (dejar en blanco para no cambiar): ")
                email = input("Email del usuario que modifica: ")
                
                nombre = nombre if nombre else None
                desc = desc if desc else None
                marca = marca if marca else None
                
                controlador.actualizar_articulo(id_art, nombre, desc, marca, email)
                print("Artículo modificado exitosamente.")
                
            elif opcion == '4':
                id_art = input("ID del artículo a eliminar: ")
                controlador.eliminar_articulo(id_art)
                print("Artículo eliminado exitosamente.")
                
            elif opcion == '5':
                break
            else:
                print("Opción inválida.")
        except Exception as e:
            print(f"Error: {e}")

def menu_principal():
    while True:
        print("\n=== SISTEMA DE AUDITORÍA DE INVENTARIO ===")
        print("1. Gestión de Usuarios")
        print("2. Gestión de Artículos")
        print("3. Salir")
        
        opcion = input("Seleccione un módulo: ")
        
        if opcion == '1':
            menu_usuarios()
        elif opcion == '2':
            menu_articulos()
        elif opcion == '3':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu_principal()
