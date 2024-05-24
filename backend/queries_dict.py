# TODO: completar con todas las otras consultas
queries = {
    0.0: {'SELECT': 'SELECT', 'FROM': 'FROM'},
    0.1: {'SELECT': 'SELECT', 'FROM': 'FROM', 'WHERE': 'WHERE'},
    1: 'SELECT nombre FROM restaurant WHERE plato = %s;',  # ejemplo
    2: 'SELECT pedido FROM pedidos WHERE pedido.usuario_email = %s;',  # ejemplo
    3: 'SELECT *, SUM(precio) FROM pedido JOIN menu ON pedido.id = menu.pedido_id GROUP BY pedido.id;',
    4: 'SELECT plato.nombre, restaurant.nombre, delivery.nombre FROM plato JOIN menu ON plato.id = menu.plato_id JOIN restaurant ON menu.restaurant_nombre = restaurant.nombre JOIN distribuye_a ON restaurant.nombre = distribuye_a.restaurant_nombre JOIN delivery ON distribuye_a.delivery_telefono = delivery.telefono WHERE P.estilo = %s;',
    5: 'SELECT nombre, restriccion FROM Plato WHERE estilo = %s;',
    6: 'SELECT DISTINCT restaurant.nombre FROM restaurant JOIN distribuye_a ON restaurant.nombre = distribuye_a.restaurant_nombre JOIN suscrito ON distribuye_a.delivery_telefono = suscrito.delivery_telefono WHERE suscrito.usuario_email = %s;',
    7: 'SELECT usuario_email, SUM(precio) FROM realiza JOIN pedido ON realiza.pedido_id = pedido.id JOIN menu ON pedido.id = menu.pedido_id LEFT JOIN suscrito ON realiza.usuario_email = suscrito.usuario_email WHERE suscrito.usuario_email IS NULL GROUP BY usuario_email;',
    8: 'SELECT plato.nombre, restaurant.nombre FROM plato JOIN menu ON plato.id = menu.plato_id JOIN Restaurant ON menu.restaurant_nombre = restaurant.nombre;',
    9: 'SELECT * FROM evalua JOIN pedido ON plato.id = menu.plato_id WHERE eval_despachador >= valor_ingresado_por_usuario OR eval_cliente >= %s;',
    10: "SELECT nombre FROM plato WHERE ingredientes LIKE %s:",
}
