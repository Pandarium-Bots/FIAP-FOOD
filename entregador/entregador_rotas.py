from flask import Blueprint, jsonify,request
import sys
from db import db_mysql_class

entregador_bp = Blueprint('entregador', __name__)





# Rota para criar um novo entregador
@entregador_bp.route('/entregador/cria_entregador', methods=['POST'])
def create_entregador():
    db_objt = db_mysql_class()
    conn = db_objt.get_db_connection()
    cursor = conn.cursor()
    try:
        data = request.json
        query = "INSERT INTO entregador (nome, cpf, telefone, email, placa, tipo_veiculo, disponivel) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (data['nome'], data.get('cpf'), data.get('telefone'), data.get('email'), data.get('placa'), data.get('tipo_veiculo'), data.get('disponivel'))
        cursor.execute(query, values)
        conn.commit()
        return jsonify({"message": "Entregador criado com sucesso"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()




# Rota para recuperar o entregador
@entregador_bp.route('/entregador/consulta_entregador/<int:id>', methods=['GET'])
def get_entregador(id):
    db_objt = db_mysql_class()
    conn = db_objt.get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        query = "SELECT * FROM entregador WHERE id_entregador = %s"
        cursor.execute(query, (id,))
        entregador = cursor.fetchone()
        if entregador:
            return jsonify(entregador), 200
        else:
            return jsonify({"message": "entregador não encontrado"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()






# Rota para atualizar um entregador pelo ID
@entregador_bp.route('/entregador/atualiza_entregador/<int:id>', methods=['PUT'])
def update_entregador(id):
    db_objt = db_mysql_class()
    conn = db_objt.get_db_connection()
    cursor = conn.cursor()
    try:
        data = request.json
        query = "UPDATE entregador SET nome = %s, cpf = %s, telefone = %s, email = %s, placa = %s, tipo_veiculo = %s, disponivel = %s WHERE id_entregador = %s"
        values = (data['nome'], data.get('cpf'), data.get('telefone'), data.get('email'), data.get('placa'), data.get('tipo_veiculo'), data.get('disponivel'), id)
        cursor.execute(query, values)
        conn.commit()
        return jsonify({"message": "Entregador atualizado com sucesso"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()





# Rota para excluir um entregador pelo ID
@entregador_bp.route('/entregador/deleta_entregador/<int:id>', methods=['DELETE'])
def delete_entregador(id):
    db_objt = db_mysql_class()
    conn = db_objt.get_db_connection()
    cursor = conn.cursor()
    try:
        query = "DELETE FROM entregador WHERE id_entregador = %s"
        cursor.execute(query, (id,))
        conn.commit()
        return jsonify({"message": "Entregador excluído com sucesso"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()
