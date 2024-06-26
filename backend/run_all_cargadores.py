import cargador_usuario as usuario
import cargador_pedido as pedido
import cargador_despachador as despachador
import cargador_delivery as delivery
import cargador_plato as plato
import cargador_restaurante as restaurante
import cargador_sucursal as sucursal
import cargador_direccion as direccion
import cargador_realiza as realiza
import cargador_evalua as evalua
import cargador_residencia as residencia
import cargador_suscrito as suscrito
import cargador_trabaja as trabaja
import cargador_distribuye_a as distribuye_a
import cargador_localizado_en as localizado_en
import cargador_de as de
import cargador_menu as menu
import cargador_contiene as contiene


if __name__ == '__main__':
    usuario.load()  # 1.
    pedido.load()  # 3.
    despachador.load()  # 4.
    delivery.load()  # 5.
    plato.load()  # 6.
    restaurante.load()  # 7.
    sucursal.load()  # 8.
    direccion.load()  # 9.
    realiza.load()  # 10.
    evalua.load()  # 11.
    residencia.load()  # 12.
    suscrito.load()  # 13.
    trabaja.load()  # 14.
    distribuye_a.load()  # 15.
    localizado_en.load()  # 16.
    de.load()  # 17.
    menu.load()  # 18.
    contiene.load()  # 19.
