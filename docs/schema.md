# Esquema relacional


### 1. Usuario 
```sql
Usuario(
    email VARCHAR(40) NOT NULL UNIQUE,
    nombre VARCHAR(30) NOT NULL,
    telefono CHAR(11) NOT NULL,
    clave VARCHAR(30) NOT NULL,
    PRIMARY KEY (email)
)
```


### 2. Administrador
(Is A Usuario)
```sql
Administrador(
	usuario_email VARCHAR(30) NOT NULL UNIQUE,
	permiso_edit_despachadores BOOLEAN,
	permiso_edit_empresas BOOLEAN,
	permiso_edit_restaurante BOOLEAN,
	permiso_edit_menu BOOLEAN,
	FOREIGN KEY (usuario_email) REFERENCES Usuario(email)
)
```


### 3. Pedido
```sql
Pedido(
	id INTEGER NOT NULL UNIQUE,
	eval_cliente INTEGER,
	estado VARCHAR(30) NOT NULL,
	hora TIME WITH TIME ZONE NOT NULL,
	fecha DATE NOT NULL,
	PRIMARY KEY (id),
	CHECK (1 <= eval_cliente AND eval_cliente <= 5),
	CHECK (estado IN ('pendiente', 'en preparación', 'entregado a
    despachador', 'entregado a cliente', 'cliente cancela', 'delivery
    cancela', 'restaurant cancela'))
)
```


### 4. Despachador
```sql
Despachador(
	telefono CHAR(11) NOT NULL UNIQUE,
	nombre VARCHAR(30) NOT NULL,
	PRIMARY KEY (telefono)
)
```

### 5. Delivery
```sql
Delivery(
	nombre VARCHAR(30) NOT NULL,
	vigente BOOLEAN NOT NULL,
	telefono CHAR(11) NOT NULL UNIQUE,
	tiempo_reparto INTEGER NOT NULL,
	precio_unitario_despacho INTEGER,
	precio_sus_mensual INTEGER,
	precio_sus_anual INTEGER,
	PRIMARY KEY (telefono),
	CHECK (precio_sus_mensual <= 4 * precio_unitario_despacho)	
	CHECK (precio_sus_anual <= 4 * precio_unitario_despacho)	
)
```

### 6. Plato
```sql
Plato(
	id SERIAL,
	estilo VARCHAR(30) NOT NULL,
	nombre VARCHAR(40) NOT NULL,
    restriccion VARCHAR(30),
    ingredientes TEXT,
	PRIMARY KEY (id),
	UNIQUE (estilo, nombre, restriccion, ingredientes)
)
```


### 7. Restaurante
```sql
Restaurante(
	nombre VARCHAR(30) NOT NULL UNIQUE,
	vigente BOOLEAN NOT NULL,
	estilo VARCHAR(30) NOT NULL,
	precio_min_reparto_gratis INTEGER,
	PRIMARY KEY(nombre)
)
```

### 8. Sucursal
```sql
Sucursal(
	nombre VARCHAR(30) NOT NULL,
	telefono VARCHAR(20) NOT NULL,
	PRIMARY KEY (telefono)
)
```

### 9. Direccion
```sql
Direccion(
	comuna VARCHAR(30) NOT NULL,
	calle VARCHAR(80) NOT NULL,
	PRIMARY KEY (comuna, calle)
)
```

### 10. Realiza
```sql
Realiza(
	pedido_id INTEGER NOT NULL,
	usuario_email VARCHAR(30) NOT NULL,
	FOREIGN KEY (pedido_id) REFERENCES Pedido(id),
	FOREIGN KEY (usuario_email) REFERENCES Usuario(email)
)
```

### 11. Evalua
```sql
Evalua(
	pedido_id INTEGER NOT NULL,
	despachador_telefono CHAR(11) NOT NULL,
	delivery_telefono CHAR(11) NOT NULL,
	eval_despachador INTEGER,
	CHECK (1 <= eval_despachador AND eval_despachador <=5),
	FOREIGN KEY (pedido_id) REFERENCES Pedido(id),
    FOREIGN KEY (despachador_telefono) REFERENCES Despachador(telefono),
    FOREIGN KEY (delivery_telefono) REFERENCES Delivery(telefono)
)
```

### 12. Residencia
```sql
Residencia(
	usuario_email VARCHAR(30) NOT NULL,
	direccion_calle VARCHAR(80) NOT NULL,
	direccion_comuna VARCHAR(30) NOT NULL,
	FOREIGN KEY (usuario_email) REFERENCES Usuario(email),
    FOREIGN KEY (direccion_calle, direccion_comuna) REFERENCES Direccion(calle, comuna)
)
```


### 13. Suscrito
```sql
Suscrito(
	delivery_telefono CHAR(11) NOT NULL,
	usuario_email VARCHAR(40) NOT NULL,
	pago INTEGER,
	fecha DATE,
	ciclo VARCHAR(30) NOT NULL,
	estado VARCHAR(30),
	CHECK (ciclo IN (‘mensual’, ’anual’)),
	CHECK (estado IN (‘vigente’, ‘cancelada’)),
	FOREIGN KEY (delivery_telefono) REFERENCES Delivery(telefono),
	FOREIGN KEY (usuario_email) REFERENCES Usuario(email)
)
```

### 14. Trabaja
```sql
Trabaja(
	delivery_telefono CHAR(11) NOT NULL,
	despachador_telefono CHAR(11) NOT NULL,
	FOREIGN KEY (delivery_telefono) REFERENCES Delivery(telefono),
	FOREIGN KEY (despachador_telefono) REFERENCES Despachador(telefono)
)
```

### 15. Distribuye_a
```sql
Distribuye_a(
	delivery_telefono CHAR(11) NOT NULL,
	restaurante_nombre VARCHAR(30) NOT NULL,
	FOREIGN KEY (delivery_telefono) REFERENCES Delivery(telefono),
    FOREIGN KEY (restaurant_nombre) REFERENCES Restaurante(nombre)
)
```

### 16. Localizado_en
```sql
Localizado_en(
	sucursal_telefono CHAR(11) NOT NULL,
	direccion_calle VARCHAR(80) NOT NULL,
	direccion_comuna VARCHAR(30) NOT NULL,
	FOREIGN KEY (sucursal_telefono) REFERENCES Sucursal(telefono),
    FOREIGN KEY (direccion_calle, direccion_comuna) REFERENCES Direccion(calle, comuna)
)
```


### 17. De
```sql
De(
	restaurante_nombre VARCHAR(30) NOT NULL,
	sucursal_telefono VARCHAR(30) NOT NULL,
	FOREIGN KEY (restaurant_nombre) REFERENCES Restaurante(nombre),
    FOREIGN KEY (sucursal_telefono) REFERENCES Sucursal(telefono)
)
```

### 18. Menu
```sql
Menu(
	plato_id INTEGER NOT NULL,
	restaurante_nombre VARCHAR(30) NOT NULL,
	porcion INTEGER DEFAULT 1,
	tiempo_preparacion INTEGER NOT NULL DEFAULT 5,
	disponibilidad BOOLEAN NOT NULL,
	descripcion VARCHAR NOT NULL,
	precio INTEGER NOT NULL,
	CHECK (porcion >= 1),
	CHECK (1 <= tiempo_preparacion AND tiempo_preparacion <= 60),
    FOREIGN KEY (plato_id) REFERENCES Plato(id),
    FOREIGN KEY (restaurant_nombre) REFERENCES Restaurante(nombre)
)
```

### 19. Contiene
```sql
Contiene(
	plato_id INTEGER NOT NULL,
	pedido_id INTEGER NOT NULL,
	restaurante_nombre VARCHAR(30) NOT NULL,
	FOREIGN KEY (plato_id) REFERENCES Plato(id),
	FOREIGN KEY (pedido_id) REFERENCES Pedido(id)
	FOREIGN KEY (restaurante_nombre) REFERENCES Restaurante(nombre)
)
```
