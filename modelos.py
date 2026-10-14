import mongoengine as me
import datetime
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_USER = os.getenv("MONGO_USER")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")

# Conexión a la base de datos MongoDB
me.connect(
    'inventario_empresa_db',
    host='localhost',
    port=27017,
    username=MONGO_USER,
    password=MONGO_PASSWORD,
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
