from flask import Blueprint, jsonify,request
import sys
from db import db_mysql_class

avaliacao_bp = Blueprint('avaliacao', __name__)

@avaliacao_bp.route('/avaliacao/cria_avaliacao', methods=['POST'])
def create_avaliacao():
    db_objt = db_mysql_class()
    conn = db_objt.get_db_connection()
    cursor = conn.cursor()
    try:
        data = request.json

        # Definir a consulta SQL e os valores
        query = "INSERT INTO avaliacao (tipo, referencia, nota, data_avaliacao, comentario) VALUES (%s, %s, %s, %s, %s)"
        values = (data['tipo'], data['referencia'], data['nota'], data['data_avaliacao'], data['comentario'])

        cursor.execute(query, values)
        conn.commit()
        return jsonify({"message": "Avaliação criada com sucesso!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()




@avaliacao_bp.route('/avaliacao/consulta_avaliacao/<int:id>', methods=['GET'])
def obter_avaliacao_por_id(id):
    db_objt = db_mysql_class()
    conn = db_objt.get_db_connection()  
    cursor = conn.cursor(dictionary=True)
    try:
        # Definir a consulta SQL para buscar uma avaliação pelo ID
        query = "SELECT * FROM avaliacao WHERE id_avaliacao = %s"
        cursor.execute(query, (id,))
        avaliacao = cursor.fetchone()

        if avaliacao:
            return jsonify({"avaliacao": avaliacao}), 200
        else:
            return jsonify({"message": "Avaliação não encontrada"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()



@avaliacao_bp.route('/avaliacao/atualiza_avaliacao/<int:id>', methods=['PUT'])
def update_avaliacao(id):
    db_objt = db_mysql_class()
    conn = db_objt.get_db_connection()
    cursor = conn.cursor()
    try:
        data = request.json
        query = "UPDATE avaliacao SET tipo = %s, referencia = %s, nota = %s, data_avaliacao = %s, comentario = %s WHERE id_avaliacao = %s"
        values = (data['tipo'], data['referencia'], data['nota'], data['data_avaliacao'], data['comentario'], id)
        cursor.execute(query, values)
        conn.commit()
        return jsonify({"message": "avaliacao atualizado com sucesso"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()




# Rota para excluir um avaliacao pelo ID
@avaliacao_bp.route('/avaliacao/deleta_avaliacao/<int:id>', methods=['DELETE'])
def delete_avaliacao(id):
    db_objt = db_mysql_class()
    conn = db_objt.get_db_connection()
    cursor = conn.cursor()
    try:
        query = "DELETE FROM avaliacao WHERE id_avaliacao = %s"
        cursor.execute(query, (id,))
        conn.commit()
        return jsonify({"message": "avaliacao excluído com sucesso"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()
