# TODO: completar con todas las otras consultas
queries = {
    0.0: {'SELECT': 'SELECT', 'FROM': 'FROM'},
    0.1: {'SELECT': 'SELECT', 'FROM': 'FROM', 'WHERE': 'WHERE'},
    1: 'SELECT DISTINCT Restaurante.nombre FROM Restaurante JOIN Menu ON Restaurante.nombre = Menu.restaurante_nombre JOIN Plato ON Plato.id = Menu.plato_id WHERE Plato.nombre = %s;',  # FUNCIONA
    2: 'SELECT pedido FROM pedidos WHERE pedido.usuario_email = %s;',  # ejemplo
    3: 'SELECT pedido.id, SUM(menu.precio) FROM plato JOIN menu ON plato.id = menu.plato_id JOIN contiene ON plato.id = contiene.plato_id JOIN restaurante ON restaurante.nombre = contiene.restaurante_nombre JOIN pedido ON pedido.id = contiene.pedido_id WHERE restaurante.nombre = menu.restaurante_nombre GROUP BY pedido.id;',  # FUNCIONA
    4: 'SELECT plato.nombre, restaurant.nombre, delivery.nombre FROM plato JOIN menu ON plato.id = menu.plato_id JOIN restaurant ON menu.restaurant_nombre = restaurant.nombre JOIN distribuye_a ON restaurant.nombre = distribuye_a.restaurant_nombre JOIN delivery ON distribuye_a.delivery_telefono = delivery.telefono WHERE P.estilo = %s;',
    5: 'SELECT nombre, restriccion FROM Plato WHERE estilo = %s;',  # FUNCIONA
    6: 'SELECT DISTINCT restaurant.nombre FROM restaurant JOIN distribuye_a ON restaurant.nombre = distribuye_a.restaurant_nombre JOIN suscrito ON distribuye_a.delivery_telefono = suscrito.delivery_telefono WHERE suscrito.usuario_email = %s;',
    7: 'SELECT usuario_email, SUM(precio) FROM realiza JOIN pedido ON realiza.pedido_id = pedido.id JOIN menu ON pedido.id = menu.pedido_id LEFT JOIN suscrito ON realiza.usuario_email = suscrito.usuario_email WHERE suscrito.usuario_email IS NULL GROUP BY usuario_email;',
    8: 'SELECT plato.nombre, restaurante.nombre FROM plato JOIN menu ON plato.id = menu.plato_id JOIN Restaurante ON menu.restaurante_nombre = restaurante.nombre GROUP restaurante.nombre;',
    9: 'SELECT * FROM evalua JOIN pedido ON plato.id = menu.plato_id WHERE eval_despachador >= valor_ingresado_por_usuario OR eval_cliente >= %s;',
    10: "SELECT nombre FROM plato WHERE ingredientes LIKE %s;",  # FUNCIONA
}

harmful_sql_keywords = (
    ';DROP', ';DELETE', ';UPDATE', ';INSERT INTO', ';ALTER TABLE',
    ';CREATE TABLE', ';CREATE DATABASE', ';TRUNCATE', ';REPLACE',
    ';GRANT', ';REVOKE', ';COMMIT', ';ROLLBACK', ';SAVEPOINT',
    ';LOCK TABLE', ';UNLOCK TABLES', ';SET TRANSACTION',
    ';SHOW DATABASES', ';SHOW TABLES', ';--', ';#'
)
