import mongoengine as me
import datetime

# Conexión a la base de datos MongoDB
me.connect(
    'inventario_empresa_db',
    host='localhost',
    port=27017,
    username='mongo',
    password='mongo',
    authentication_source='admin'
)

# Colección Usuarios
class Usuario(me.Document):
    email = me.StringField(required=True, unique=True)
    nombre = me.StringField(required=True)
    apellido = me.StringField(required=True)
    fecha_creado = me.DateTimeField(default=datetime.datetime.now)

# Colección Artículos
class Articulo(me.Document):
    nombre = me.StringField(required=True)
    descripcion = me.StringField()
    marca = me.StringField()
    usuario_modifico = me.ReferenceField(Usuario, required=True)
