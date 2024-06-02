# TODO: completar con todas las otras consultas
queries = {
    0.0: {'SELECT': 'SELECT', 'FROM': 'FROM'},
    0.1: {'SELECT': 'SELECT', 'FROM': 'FROM', 'WHERE': 'WHERE'},
    1: 'SELECT DISTINCT Restaurante.nombre FROM Restaurante JOIN Menu ON Restaurante.nombre = Menu.restaurante_nombre JOIN Plato ON Plato.id = Menu.plato_id WHERE Plato.nombre = %s;',  # FUNCIONA
    2: "SELECT usuario.email, SUM(menu.precio) AS gasto_mensual FROM pedido JOIN realiza ON pedido.id = realiza.pedido_id JOIN usuario ON usuario.email = realiza.usuario_email JOIN contiene ON contiene.pedido_id = pedido.id JOIN menu on contiene.plato_id = menu.plato_id AND contiene.restaurante_nombre = menu.restaurante_nombre WHERE pedido.estado = 'entregado a cliente' AND usuario.email = %s GROUP BY usuario.email ORDER BY usuario.email;",
    3: 'SELECT pedido.id, SUM(menu.precio) FROM plato JOIN menu ON plato.id = menu.plato_id JOIN contiene ON plato.id = contiene.plato_id JOIN restaurante ON restaurante.nombre = contiene.restaurante_nombre JOIN pedido ON pedido.id = contiene.pedido_id WHERE restaurante.nombre = menu.restaurante_nombre GROUP BY pedido.id;',  # FUNCIONA
    4: 'SELECT DISTINCT plato.nombre AS plato, restaurante.nombre AS restaurante, delivery.nombre AS delivery FROM plato JOIN menu ON plato.id = menu.plato_id JOIN restaurante ON menu.restaurante_nombre = restaurante.nombre JOIN distribuye_a  ON restaurante.nombre = distribuye_a.restaurante_nombre  JOIN delivery ON distribuye_a.delivery_telefono = delivery.telefono WHERE plato.estilo = %s;',  # FUNCIONA
    5: 'SELECT nombre, restriccion FROM Plato WHERE estilo = %s;',  # FUNCIONA
    6: 'SELECT DISTINCT restaurante.nombre FROM usuario JOIN suscrito ON usuario.email = suscrito.usuario_email JOIN delivery ON suscrito.delivery_telefono = delivery.telefono JOIN distribuye_a ON distribuye_a.delivery_telefono = delivery.telefono JOIN restaurante ON restaurante.nombre = distribuye_a.restaurante_nombre WHERE suscrito.usuario_email = %s;',  # FUCNIONA
    7: 'SELECT realiza.usuario_email, SUM(menu.precio) AS costo FROM realiza JOIN pedido ON realiza.pedido_id = pedido.id JOIN contiene ON pedido.id = contiene.pedido_id JOIN menu ON menu.plato_id = contiene.plato_id LEFT JOIN suscrito ON realiza.usuario_email = suscrito.usuario_email WHERE suscrito.usuario_email IS NULL GROUP BY realiza.usuario_email;',  # FUNCIONA
    8: 'SELECT plato.nombre, restaurante.nombre FROM plato JOIN menu ON plato.id = menu.plato_id JOIN restaurante ON menu.restaurante_nombre = restaurante.nombre ORDER BY plato.nombre ASC;',  # FUNCIONA
    9: 'SELECT pedido.id AS id_del_pedido, pedido.eval_cliente AS Evaluacion_del_cliente, evalua.eval_despachador AS Evaluacion_del_despachador FROM pedido JOIN evalua ON evalua.pedido_id = pedido.id JOIN Despachador ON evalua.despachador_telefono = despachador.telefono WHERE pedido.eval_cliente >= %s AND evalua.eval_despachador >= %s ORDER BY pedido.id ASC;',  # FUNCIONA
    10: "SELECT nombre FROM plato WHERE ingredientes LIKE %s;",  # FUNCIONA
}

harmful_sql_keywords = (
    ';DROP', ';DELETE', ';UPDATE', ';INSERT INTO', ';ALTER TABLE',
    ';CREATE TABLE', ';CREATE DATABASE', ';TRUNCATE', ';REPLACE',
    ';GRANT', ';REVOKE', ';COMMIT', ';ROLLBACK', ';SAVEPOINT',
    ';LOCK TABLE', ';UNLOCK TABLES', ';SET TRANSACTION',
    ';SHOW DATABASES', ';SHOW TABLES', ';--', ';#'
)
