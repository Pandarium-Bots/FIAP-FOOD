from flask import Blueprint, jsonify,request
import sys
from db import db_mysql_class


restaurante_bp = Blueprint('restaurante', __name__)


#Rota para criar um novo restaurante
@restaurante_bp.route('/restaurante/cria_restaurante', methods=['POST'])
def create_restaurante():
    """
    Cria um novo restaurante.
    ---
    tags:
      - Restaurante
    parameters:
      - in: body
        name: body
        schema:
          type: object
          required:
            - nome
            - rua
            - numero
            - bairro
            - cep
            - estado
            - cidade
            - descricao
            - categoria
            - cnpj
          properties:
            nome:
              type: string
            rua:
              type: string
            numero:
              type: integer
            bairro:
              type: string
            cep:
              type: string
            estado:
              type: string
            cidade:
              type: string
            descricao:
              type: string
            categoria:
              type: string
            cnpj:
              type: string
    responses:
      201:
        description: Restaurante criado com sucesso
      400:
        description: Erro ao criar o restaurante
    """
    db_objt = db_mysql_class()
    conn = db_objt.get_db_connection()
    cursor = conn.cursor()
    try:
        data = request.json
        query = "INSERT INTO restaurante (nome, rua, numero, bairro, cep, estado, cidade, descricao, categoria, cnpj) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (data['nome'], data['rua'], data['numero'], data['bairro'], data['cep'], data['estado'], data['cidade'], data['descricao'], data['categoria'], data['cnpj'])
        cursor.execute(query, values)
        conn.commit()
        return jsonify({"message": "Restaurante criado com sucesso"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()



# Rota para recuperar todos os restaurantes
@restaurante_bp.route('/restaurante/consulta_restaurante/<int:id>', methods=['GET'])
def get_restaurantes(id):
    """
    Recupera informações de um restaurante pelo ID.
    ---
    tags:
      - Restaurante
    parameters:
      - in: path
        name: id
        type: integer
        required: true
        description: ID do restaurante a ser consultado
    responses:
      200:
        description: Retorna informações do restaurante
        schema:
          type: object
          properties:
            nome:
              type: string
            rua:
              type: string
            numero:
              type: integer
            bairro:
              type: string
            cep:
              type: string
            estado:
              type: string
            cidade:
              type: string
            descricao:
              type: string
            categoria:
              type: string
            cnpj:
              type: string
      404:
        description: Restaurante não encontrado
      400:
        description: Erro ao recuperar informações do restaurante
    """
    db_objt = db_mysql_class()
    conn = db_objt.get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        query = "SELECT * FROM restaurante WHERE id_restaurante = %s"
        cursor.execute(query, (id,))
        restaurante = cursor.fetchone()
        if restaurante:
            return jsonify(restaurante), 200
        else:
            return jsonify({"message": "restaurante não encontrado"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()




# Rota para atualizar um restaurante pelo ID
@restaurante_bp.route('/restaurante/atualiza_restaurante/<int:id>', methods=['PUT'])
def update_restaurante(id):
    """
    Atualiza um restaurante pelo ID.
    ---
    tags:
      - Restaurante
    parameters:
      - in: path
        name: id
        type: integer
        required: true
        description: ID do restaurante a ser atualizado
      - in: body
        name: body
        schema:
          type: object
          required:
            - nome
            - rua
            - numero
            - bairro
            - cep
            - estado
            - cidade
            - descricao
            - categoria
            - cnpj
          properties:
            nome:
              type: string
            rua:
              type: string
            numero:
              type: integer
            bairro:
              type: string
            cep:
              type: string
            estado:
              type: string
            cidade:
              type: string
            descricao:
              type: string
            categoria:
              type: string
            cnpj:
              type: string
    responses:
      200:
        description: Restaurante atualizado com sucesso
      400:
        description: Erro ao atualizar o restaurante
    """
    db_objt = db_mysql_class()
    conn = db_objt.get_db_connection()
    cursor = conn.cursor()
    try:
        data = request.json
        query = "UPDATE restaurante SET nome = %s, rua = %s, numero = %s, bairro = %s, cep = %s, estado = %s, cidade = %s, descricao = %s, categoria = %s, cnpj = %s  WHERE id_restaurante = %s"
        values = (data['nome'], data['rua'], data['numero'], data['bairro'], data['cep'], data['estado'], data['cidade'], data['descricao'], data['categoria'], data['cnpj'], id)
        cursor.execute(query, values)
        conn.commit()
        return jsonify({"message": "Restaurante atualizado com sucesso"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()








# Rota para excluir um restaurante pelo ID
@restaurante_bp.route('/restaurante/deleta_restaurante/<int:id>', methods=['DELETE'])
def delete_restaurante(id):
    """
    Exclui um restaurante pelo ID.
    ---
    tags:
      - Restaurante
    parameters:
      - in: path
        name: id
        type: integer
        required: true
        description: ID do restaurante a ser excluído
    responses:
      200:
        description: Restaurante excluído com sucesso
      400:
        description: Erro ao excluir o restaurante
    """
    db_objt = db_mysql_class()
    conn = db_objt.get_db_connection()
    cursor = conn.cursor()
    try:
        query = "DELETE FROM restaurante WHERE id_restaurante = %s"
        cursor.execute(query, (id,))
        conn.commit()
        return jsonify({"message": "Restaurante excluído com sucesso"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()









# Rota para recuperar todos os restaurantes
@restaurante_bp.route('/restaurante/consulta_all/', methods=['GET'])
def get_restaurantes_all():
    """
    Recupera informações de todos os restaurantes.
    ---
    tags:
      - Restaurante
    responses:
      200:
        description: Retorna uma lista de restaurantes
        schema:
          type: array
          items:
            type: object
            properties:
              nome:
                type: string
              rua:
                type: string
              numero:
                type: integer
              bairro:
                type: string
              cep:
                type: string
              estado:
                type: string
              cidade:
                type: string
              descricao:
                type: string
              categoria:
                type: string
              cnpj:
                type: string
      404:
        description: Nenhum restaurante encontrado
      400:
        description: Erro ao recuperar informações dos restaurantes
    """
    db_objt = db_mysql_class()
    conn = db_objt.get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        query = "SELECT * FROM restaurante"
        cursor.execute(query)
        restaurante = cursor.fetchall()
        if restaurante:
            return jsonify(restaurante), 200
        else:
            return jsonify({"message": "restaurante não encontrado"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()







# Rota para recuperar todos os restaurantes
@restaurante_bp.route('/restaurante/consulta_categoria/<string:categoria>', methods=['GET'])
def get_restaurantes_categoria(categoria):
    """
    Recupera informações dos restaurantes por categoria.
    ---
    tags:
      - Restaurante
    parameters:
      - in: path
        name: categoria
        type: string
        required: true
        description: Categoria dos restaurantes a ser consultada
    responses:
      200:
        description: Retorna uma lista de restaurantes da categoria especificada
        schema:
          type: array
          items:
            type: object
            properties:
              nome:
                type: string
              rua:
                type: string
              numero:
                type: integer
              bairro:
                type: string
              cep:
                type: string
              estado:
                type: string
              cidade:
                type: string
              descricao:
                type: string
              categoria:
                type: string
              cnpj:
                type: string
      404:
        description: Nenhum restaurante da categoria especificada encontrado
      400:
        description: Erro ao recuperar informações dos restaurantes da categoria
    """
    db_objt = db_mysql_class()
    conn = db_objt.get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        query = "SELECT * FROM restaurante where categoria = %s"
        cursor.execute(query, (categoria,))
        restaurante = cursor.fetchall()
        if restaurante:
            return jsonify(restaurante), 200
        else:
            return jsonify({"message": "restaurante não encontrado"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()


