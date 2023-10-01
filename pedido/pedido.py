from flask import Blueprint, jsonify,request
import sys
from db import db_mysql_class
from produto import get_produto as gp
from produto import get_produto_lote 
from itertools import groupby

pedido_bp = Blueprint('pedido', __name__)



def check(list):
    check = all(i == list[0] for i in list)
    if check:
        return list[0],check
    return 'Erro', check 



# Rota para criar um novo pedido
@pedido_bp.route('/pedido/cria_pedido', methods=['POST'])
def create_pedido():
    db_objt = db_mysql_class()
    conn = db_objt.get_db_connection()
    cursor = conn.cursor()
    #create pedido
    #lista de dict produto [{id_produto:2,descricao:'xablau'},{id_produto:2,descricao:'xablau'},{id_produto:2,descricao:'sem_bacon'}]
    #cliente
    #endereço do cliente
    #seleciona entregador
    #forma de pagamento
    #
    try:
        data = request.json

        produtos_list = list(get_produto_lote( [produto['id_produto'] for produto in data['produtos']] ))

        # for produto in data['produtos']:
        #     produto_info = gp(produto['id_produto'])
        #     produtos_list.append(produto_info)

        disponivel_check = next((item for item in produtos_list if item['disponivel'] == 0), None)


        id_restaurante, id_check = check([x['id_restaurante'] for x in  produtos_list])

        if id_check and disponivel_check == None:
            valor_lista = [float(x['valor']) for x in produtos_list]
            valor_total = sum(valor_lista)
            
            produtos_texto_lista = []

            for produto in data['produtos']:
                
                produto_selecionado = next((item for item in produtos_list if item['id_produto'] == produto['id_produto']), None)
                produto_selecionado['descricao'] = produto['descricao']

                produtos_texto_lista.append(produto_selecionado)

            produtos_texto_string = str(produtos_texto_lista)


            query = "INSERT INTO pedido (id_cliente, id_restaurante, id_entregador, id_endereco_cliente, forma_pagamento, produtos, status_pedido, valor, data_hora_pedido) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (data['id_cliente'], id_restaurante, data['id_entregador'], data['id_endereco_cliente'], data['forma_pagamento'], produtos_texto_string, data['status_pedido'], valor_total, data['data_hora_pedido'])
            # arrumar ali no DATA[entregador] para pegar sem o data 
            cursor.execute(query, values)
            conn.commit()
            return jsonify({"message": "pedido criado com sucesso"}), 201
        else:
           return jsonify({"message": "Pedido invalido, produtos de mais de um restaurante no pedido"}), 400
        
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()




# Rota para recuperar o pedido
@pedido_bp.route('/pedido/consulta_pedido/<int:id>', methods=['GET'])
def get_pedido(id):
    db_objt = db_mysql_class()
    conn = db_objt.get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        query = "SELECT * FROM pedido WHERE id_pedido = %s"
        cursor.execute(query, (id,))
        pedido = cursor.fetchone()
        if pedido:
            return jsonify(pedido), 200
        else:
            return jsonify({"message": "pedido não encontrado"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()






# Rota para atualizar um pedido pelo ID
@pedido_bp.route('/pedido/atualiza_pedido/<int:id>', methods=['PUT'])
def update_pedido(id):
    db_objt = db_mysql_class()
    conn = db_objt.get_db_connection()
    cursor = conn.cursor()
    try:
        data = request.json
        query = "UPDATE pedido SET id_cliente = %s, id_restaurante = %s, id_entregador = %s, id_endereco_cliente = %s, forma_pagamento = %s, produtos = %s, status_pedido = %s, valor = %s, data_hora_pedido = %s WHERE id_pedido = %s"
        values = (data.get('id_cliente'), data.get('id_restaurante'), data.get('id_entregador'), data.get('id_endereco_cliente'), data.get('forma_pagamento'), data.get('produtos'), data.get('status_pedido'), data.get('valor'), data.get('data_hora_pedido'), id)
        cursor.execute(query, values)
        conn.commit()
        return jsonify({"message": "Pedido atualizado com sucesso"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()





# Rota para excluir um pedido pelo ID
@pedido_bp.route('/pedido/deleta_pedido/<int:id>', methods=['DELETE'])
def delete_pedido(id):
    db_objt = db_mysql_class()
    conn = db_objt.get_db_connection()
    cursor = conn.cursor()
    try:
        query = "DELETE FROM pedido WHERE id_pedido = %s"
        cursor.execute(query, (id,))
        conn.commit()
        return jsonify({"message": "pedido excluído com sucesso"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()
