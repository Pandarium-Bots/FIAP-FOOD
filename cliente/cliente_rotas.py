from flask import Blueprint, jsonify,request
import sys
from db import db_mysql_class

cliente_bp = Blueprint('cliente', __name__)




@cliente_bp.route('/cliente/cria_cliente', methods=['POST'])
def create_cliente():
    db_objt = db_mysql_class()
    conn = db_objt.get_db_connection()
    cursor = conn.cursor()
    try:
        data = request.json
        query = "INSERT INTO cliente (nome, cpf, telefone, email, data_nascimento, data_cadastro) VALUES (%s, %s, %s, %s, %s, NOW())"
        values = (data['nome'], data['cpf'], data['telefone'], data['email'], data['data_nascimento'])
        cursor.execute(query, values)
        conn.commit()
        return jsonify({"message": "Cliente criado com sucesso"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()



# Rota para consultar um cliente pelo ID
@cliente_bp.route('/cliente/consulta_cliente/<int:id>', methods=['GET'])
def get_cliente(id):
    db_objt = db_mysql_class()
    conn = db_objt.get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        query = "SELECT * FROM cliente WHERE id_cliente = %s"
        cursor.execute(query, (id,))
        cliente = cursor.fetchone()
        if cliente:
            return jsonify(cliente), 200
        else:
            return jsonify({"message": "Cliente não encontrado"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()






# Rota para atualizar um cliente pelo ID
@cliente_bp.route('/cliente/atualiza_cliente/<int:id>', methods=['PUT'])
def update_cliente(id):
    db_objt = db_mysql_class()
    conn = db_objt.get_db_connection()
    cursor = conn.cursor()
    try:
        data = request.json
        query = "UPDATE cliente SET nome = %s, cpf = %s, telefone = %s, email = %s, data_nascimento = %s WHERE id_cliente = %s"
        values = (data['nome'], data['cpf'], data['telefone'], data['email'], data['data_nascimento'], id)
        cursor.execute(query, values)
        conn.commit()
        return jsonify({"message": "Cliente atualizado com sucesso"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()




# Rota para excluir um cliente pelo ID
@cliente_bp.route('/cliente/deleta_cliente/<int:id>', methods=['DELETE'])
def delete_cliente(id):
    db_objt = db_mysql_class()
    conn = db_objt.get_db_connection()
    cursor = conn.cursor()
    try:
        query = "DELETE FROM cliente WHERE id_cliente = %s"
        cursor.execute(query, (id,))
        conn.commit()
        return jsonify({"message": "Cliente excluído com sucesso"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()


