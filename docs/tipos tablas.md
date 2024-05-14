# suscripciones
Suscriciones(email:string, nombre:string, estado:string, ultimopago:int, fecha:date, ciclo:string)
- no hay celdas vacias en este csv
- no hay nada mal escrito

- gmail: pasar todo a minuscula
- Nombre: pasar todo a minuscula
- estado: pasarlo todo a minuscula
    - pasar a bool
    - si esta vacia, quitarlo de la lista
- ultimopago: bien, si esta vacio es 0
- fecha: esta formato DD-MM-YY



# platos
Platos(nombre:string,	descripcion:string,	disponibilidad:int,	estilo:string,	restriccion:string,	ingredientes:string, 	porciones: int,	precio: int,	tiempo:int,	restaurant:string	repartomin:int,	vigente:bool)

- nombre: pasarlo todo a minuscula
- descripcion: si esta vacio, poner no descripcion
- disponibilidad: un bool
- estilo: bien
- resticcion: bien
- ingrediente: no atomizado, pitearnosla de aca, crear una nueva tabla junto a platos
- porciones: bien, si es 0 pasar a 1
- precio: bien
- tiempo: asumimos minutos
- restaurant: bien, corregit
- reparto min: #TODO: ver que wea es
- vigente: bool


- estilo es lo mismo que tipo (ej. hamburguesas)


# clientes

Clientes(cliente:string, email:string,	telefono:int,	clave:string,	direccion:string,	comuna:string)

- cliente: bien 
- email: bien 
- telefono: bien 
- clave: bien 
- direccion: bien 
- comuna: id para la tabla comuna 

### Dependencias, cla
- cliente -> email, telefono, clave
- un cliente puede tener 2 direciones distintas 
- comuna -> direccion

# restaurantes
Restaurantes(nombre:string,	vigente:bool,	estilo:string,	repartomin:int,	sucursal:string,	direccion:string,	telefono:int,	area:string)
- llave: nombre, direccion
- telefono: hay datos con longitud distinta
- todo el resto bien 

# comuna
Comuna(cut:int,	nombre:string,	provincia:string,	region:string)
- BIEN

# cldeldes
Cldeldes(clientenombre:string, clientemail:string, clientetelefono:int, clienteclave:int, deliverynombre:string, deliveryurgente:bool, deliverytelefono:int, deliverytiempo:int, deliverypreciounitario:int,deliverypreciomensual:int, deliveryprecioanual:int, despachadornombre:string,	despachadortelefono:int)
- TABLA CON TODO
- une clientes con el delivery y el despachador 
- todo cliente esta de mas 


# calificacion
Calificacion(pedido:int, resdel:int, cliente:int)
- TODO: que es resdel
- tabla para hacer joins

# pedidos

Pedidos(id:int,	cliente:string,	restaurant:string,	sucursal:string,	delivery:string,	despachador:string,	plato:int,	fecha:date,	hora:hour,	estado:string)

- la fecha tiene este formato 19-12-23
- la hora tiene este formato 14:57:50
