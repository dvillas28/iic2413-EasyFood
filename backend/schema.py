table_scheme = [
    """
  CREATE TABLE usuario(
  email VARCHAR(40) NOT NULL UNIQUE, 
  nombre VARCHAR(30) NOT NULL,
  telefono CHAR(11) NOT NULL,
  clave VARCHAR(30) NOT NULL,
  PRIMARY KEY (email));
  """,
    """
  CREATE TABLE administrador(
	usuario_email VARCHAR(30) NOT NULL UNIQUE,
	permiso_edit_despachadores BOOLEAN,
	permiso_edit_empresas BOOLEAN,
	permiso_edit_restaurantee BOOLEAN,
	permiso_edit_menu BOOLEAN,
	FOREIGN KEY (usuario_email) REFERENCES Usuario(email));
  """,
    """
  CREATE TABLE Pedido(
	id INTEGER NOT NULL UNIQUE,
	eval_cliente INTEGER,
	estado VARCHAR(30) NOT NULL,
	hora TIME WITH TIME ZONE NOT NULL,
	fecha DATE NOT NULL,
	PRIMARY KEY (id),
	CHECK (eval_cliente >= 1 AND eval_cliente <= 5),
	CHECK (estado IN ('pendiente', 'en preparacion', 'entregado a despachador', 'entregado a cliente', 'cliente cancela', 'delivery cancela', 'restaurant cancela')));
  """,
    """
  CREATE TABLE despachador(
	telefono CHAR(11) NOT NULL UNIQUE,
	nombre VARCHAR(30) NOT NULL,
	PRIMARY KEY (telefono));
  """,
    """
  CREATE TABLE delivery(
	nombre VARCHAR(30) NOT NULL,
	vigente BOOLEAN NOT NULL,
	telefono CHAR(11) NOT NULL UNIQUE,
	tiempo_reparto INTEGER NOT NULL,
	precio_unitario_despacho INTEGER,
	precio_sus_mensual INTEGER,
	precio_sus_anual INTEGER,
	PRIMARY KEY (telefono),
	CHECK (precio_sus_mensual <= 4 * precio_unitario_despacho));
  """,
    """
  CREATE TABLE plato(
	id SERIAL,
	estilo VARCHAR(30) NOT NULL,
	nombre VARCHAR(40) NOT NULL,
	restriccion VARCHAR(30) NOT NULL,
	ingredientes TEXT,
	PRIMARY KEY (id),
	UNIQUE (estilo, nombre, restriccion, ingredientes));
  """,
    """
  CREATE TABLE restaurante(
	nombre VARCHAR(30) NOT NULL UNIQUE,
	vigente BOOLEAN NOT NULL,
	estilo VARCHAR(30) NOT NULL,
	precio_min_reparto_gratis INTEGER,
	PRIMARY KEY(nombre));
  """,
    """
  CREATE TABLE sucursal(
	nombre VARCHAR(30) NOT NULL,
	telefono VARCHAR(20) NOT NULL,
	PRIMARY KEY (telefono));
  """,
    """
  CREATE TABLE direccion(
	comuna VARCHAR(30) NOT NULL,
	calle VARCHAR(60) NOT NULL,
	PRIMARY KEY (comuna, calle));
  """,
    """
  CREATE TABLE realiza(
  pedido_id INTEGER NOT NULL,
	usuario_email VARCHAR(30) NOT NULL,
	FOREIGN KEY (pedido_id) REFERENCES Pedido(id),
	FOREIGN KEY (usuario_email) REFERENCES Usuario(email)); 
  """,
    """
  CREATE TABLE evalua(
	pedido_id INTEGER NOT NULL,
	despachador_telefono CHAR(11) NOT NULL,
	delivery_telefono CHAR(11) NOT NULL,
	eval_despachador INTEGER,
	CHECK (eval_despachador >= 1 AND eval_despachador <=5),
	FOREIGN KEY (pedido_id) REFERENCES Pedido(id),
  FOREIGN KEY (despachador_telefono) REFERENCES Despachador(telefono),
  FOREIGN KEY (delivery_telefono) REFERENCES Delivery(telefono));
  """,
    """
  CREATE TABLE residencia(
	usuario_email VARCHAR(30) NOT NULL,
	direccion_calle VARCHAR(30) NOT NULL,
	direccion_comuna VARCHAR(30) NOT NULL,
	FOREIGN KEY (usuario_email) REFERENCES Usuario(email),
    FOREIGN KEY (direccion_calle, direccion_comuna) REFERENCES Direccion(calle, comuna));
  """,
    """
  CREATE TABLE suscrito(
	delivery_telefono VARCHAR(11) NOT NULL,
	usuario_email VARCHAR(40) NOT NULL,
	pago INTEGER,
	fecha DATE,
	ciclo VARCHAR(30) NOT NULL,
	estado VARCHAR(30),
	CHECK (ciclo IN ('mensual', 'anual')),
	CHECK (estado IN ('vigente', 'cancelada')),
	FOREIGN KEY (delivery_telefono) REFERENCES Delivery(telefono),
	FOREIGN KEY (usuario_email) REFERENCES Usuario(email));
  """,
    """
  CREATE TABLE trabaja(
	delivery_telefono CHAR(11) NOT NULL,
	despachador_telefono CHAR(11) NOT NULL,
	FOREIGN KEY (delivery_telefono) REFERENCES Delivery(telefono),
	FOREIGN KEY (despachador_telefono) REFERENCES Despachador(telefono)); 
  """,
    """
  CREATE TABLE distribuye_a(
	delivery_telefono CHAR(11) NOT NULL,
	restaurante_nombre VARCHAR(30) NOT NULL,
	FOREIGN KEY (delivery_telefono) REFERENCES Delivery(telefono),
  FOREIGN KEY (restaurante_nombre) REFERENCES restaurante(nombre));
  """,
    """
  CREATE TABLE localizado_en(
  sucursal_telefono CHAR(30) NOT NULL,
  direccion_calle VARCHAR(30) NOT NULL,
  direccion_comuna VARCHAR(30) NOT NULL,
  FOREIGN KEY (sucursal_telefono) REFERENCES Sucursal(telefono),
  FOREIGN KEY (direccion_calle, direccion_comuna) REFERENCES Direccion(calle, comuna)); 
  """,
    """
  CREATE TABLE de(
	restaurante_nombre VARCHAR(30) NOT NULL,
	sucursal_telefono VARCHAR(20) NOT NULL,
	FOREIGN KEY (restaurante_nombre) REFERENCES restaurante(nombre),
  FOREIGN KEY (sucursal_telefono) REFERENCES Sucursal(telefono));
  """,
    """
  CREATE TABLE menu(
	plato_id INTEGER NOT NULL,
	restaurante_nombre VARCHAR(30) NOT NULL,
	porcion INTEGER DEFAULT 1,
	tiempo_preparacion INTEGER NOT NULL DEFAULT 5,
	disponibilidad BOOLEAN NOT NULL,
	descripcion VARCHAR NOT NULL,
	precio INTEGER NOT NULL,
	CHECK (porcion >= 1),
	CHECK (tiempo_preparacion >= 1 AND tiempo_preparacion <= 60),
  FOREIGN KEY (plato_id) REFERENCES Plato(id),
  FOREIGN KEY (restaurante_nombre) REFERENCES restaurante(nombre));
  """,
    """
  CREATE TABLE Contiene(
	plato_id INTEGER NOT NULL,
	pedido_id INTEGER NOT NULL,
  restaurante_nombre VARCHAR(30) NOT NULL,
	FOREIGN KEY (plato_id) REFERENCES Plato(id),
	FOREIGN KEY (pedido_id) REFERENCES Pedido(id),
  FOREIGN KEY (restaurante_nombre) REFERENCES restaurante(nombre)); 
  """
]

# primero hay que limpiar las tablas que contienen llaves foraneas
table_names = [
    'realiza',  # 10.
    'evalua',  # 11.
    'residencia',  # 12.
    'suscrito',  # 13.
    'trabaja',  # 14.
    'distribuye_a',  # 15.
    'localizado_en',  # 16.
    'de',  # 17.
    'menu',  # 18.
    'contiene',  # 19.
    'usuario',  # 1.
    'pedido',  # 3.
    'despachador',  # 4.
    'delivery',  # 5.
    'plato',  # 6.
    'restaurante',  # 7.
    'sucursal',  # 8.
    'direccion',  # 9.
]
