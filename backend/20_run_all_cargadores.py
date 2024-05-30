import cargador_usuario as usuario
# TODO import cargador_pedido as pedido
import cargador_despachador as despachador
import cargador_delivery as delivery
# TODO import cargador_plato as plato
import cargador_restaurante as restaurante
import cargador_sucursal as sucursal
import cargador_direccion as direccion
import cargador_realiza as realiza
# TODO import cargador_evalua as evalua
import cargador_residencia as residencia
# TODO import cargador_suscrito as suscrito
import cargador_trabaja as trabaja
# TODO import cargador_distribuye_a as distribuye_a
# TODO import cargador_localizado_en as localizado_en
# TODO import cargador_de as de
# TODO import cargador_menu as menu
# TODO import cargador_contiene as contiene


if __name__ == '__main__':
    usuario.load()  # 1.
    # pedido.load()  # 2.
    despachador.load()  # 4.
    delivery.load()  # 5.
    # plato.load()  # 6.
    restaurante.load()  # 7.
    sucursal.load()  # 8.
    direccion.load()  # 9.
    realiza.load()  # 10.
    # evalua.load()  # 11.
    residencia.load()  # 12.
    # suscrito.load()  # 13.
    trabaja.load()  # 14.
    # distribuye_a.load()  # 15.
    # localizado_en.load()  # 16.
    # de.load()  # 17.
    # menu.load()  # 18.
    # contiene.load()  # 19.
