import mongoengine as me
from modelos import Usuario, Articulo

# Operaciones Usuarios
def registrar_usuario(email, nombre, apellido):
    email = email.strip()
    if not email:
        raise ValueError("El email no puede estar vacío.")
    
    if Usuario.objects(email=email).first():
        raise ValueError(f"Ya existe un usuario con el email {email}.")

    usuario = Usuario(email=email, nombre=nombre.strip(), apellido=apellido.strip())
    return usuario.save()

def obtener_usuarios():
    return Usuario.objects()

def buscar_usuario_por_email(email):
    usuario = Usuario.objects(email=email.strip()).first()
    if not usuario:
        raise ValueError(f"Usuario con email {email} no encontrado.")
    return usuario

def actualizar_usuario(email, nuevo_nombre, nuevo_apellido):
    usuario = buscar_usuario_por_email(email)
    if nuevo_nombre.strip():
        usuario.nombre = nuevo_nombre.strip()
    if nuevo_apellido.strip():
        usuario.apellido = nuevo_apellido.strip()
    return usuario.save()

def eliminar_usuario(email):
    usuario = buscar_usuario_por_email(email)
    # Verificar si el usuario está referenciado en algún artículo antes de borrar
    if Articulo.objects(usuario_modifico=usuario).count() > 0:
        raise ValueError("No se puede eliminar el usuario. Tiene artículos asociados.")
    usuario.delete()
    return True

# Operaciones Artículos
def registrar_articulo(nombre, descripcion, marca, email_usuario):
    if not nombre or not nombre.strip():
        raise ValueError("El nombre del artículo no puede estar vacío.")
    
    usuario = buscar_usuario_por_email(email_usuario)
    
    articulo = Articulo(
        nombre=nombre.strip(),
        descripcion=descripcion.strip(),
        marca=marca.strip(),
        usuario_modifico=usuario
    )
    return articulo.save()

def obtener_articulos():
    return Articulo.objects()

def buscar_articulo_por_id(id_articulo):
    try:
        articulo = Articulo.objects.get(id=id_articulo)
        return articulo
    except me.DoesNotExist:
        raise ValueError(f"Artículo con ID {id_articulo} no encontrado.")
    except me.ValidationError:
        raise ValueError("Formato de ID inválido.")

def actualizar_articulo(id_articulo, nombre, descripcion, marca, email_usuario):
    articulo = buscar_articulo_por_id(id_articulo)
    
    if nombre is not None:
        if not nombre.strip():
            raise ValueError("El nombre del artículo no puede estar vacío.")
        articulo.nombre = nombre.strip()
        
    if descripcion is not None:
        articulo.descripcion = descripcion.strip()
        
    if marca is not None:
        articulo.marca = marca.strip()
        
    if email_usuario is not None and email_usuario.strip():
        usuario = buscar_usuario_por_email(email_usuario)
        articulo.usuario_modifico = usuario
        
    return articulo.save()

def eliminar_articulo(id_articulo):
    articulo = buscar_articulo_por_id(id_articulo)
    articulo.delete()
    return True
