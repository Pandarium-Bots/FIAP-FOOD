# FIAP-FOOD Tech Challenge FIAP


## Grupo 5 – 3SOAT:
rm351636: Leonilson Sousa de Alencar Filho

rm351654: Bruno Pulice Faccio

rm351640: William de Magalhães Pereira




Repositório: https://github.com/Pandarium-Bots/FIAP-FOOD

Miro: https://miro.com/app/board/uXjVMognDeM=/?share_link_id=774417067533

Swagger: https://fiap-food-app-7qsvg.ondigitalocean.app/apidocs/#/

Insomnia: https://github.com/Pandarium-Bots/FIAP-FOOD/blob/main/Insomnia_2023-11-01.json



Toda a aplicação está sendo executada no Digital Ocean, na URL:
 https://fiap-food-app-7qsvg.ondigitalocean.app/  


Deixamos a API aberta para a internet, e sem token de segurança por enquanto, para que possam utilizar as APIs e consultar nosso banco de dados.


## Banco de dados

Instância de Banco de dados MySQL criado e hospedado no DigitalOcean também.




# Guia de Utilização da API de Gerenciamento de Pedidos

## **Passo 1: Conhecendo a API**
- **Descrição Geral**: Esta API permite gerenciar pedidos, clientes, produtos e entregadores em um sistema de restaurante. Com ela, você pode criar, atualizar, excluir e consultar informações detalhadas.

## **Passo 2: Configuração Inicial**
- **Obtenção de Credenciais**: Para usar a API, utilize suas credenciais (API Key) que foram previamente fornecida no arquivo entregue no Tech Challenge.
- **Configuração do Ambiente**: Instale as ferramentas necessárias, como Postman ou cURL, para fazer requisições à API.

## **Passo 3: Autenticação**
- **Utilizando a API Key**: Em todas as suas requisições, inclua a API Key no cabeçalho para autenticação.

   ```json
   
    {
        "Authorization": "bearer TOKEN_FORNECIDO"
    }
   ```

## **Passo 4: Entendimento das APIs**
- **Sobre os tópicos**: Abaixo segue a explicação de cada chamada e exemplo de utilização da chamada.


<details><summary>Explicação APIs</summary>

## Gerenciando Restaurantes
1. **Registrar um Entregador**:
   - Endpoint: `/create_restaurante`, Método: POST.
   - Inclua as informações do entregador.
   ```json
   
    {
        "id_restaurante": 5,
        "nome_produto": "Chá de Ohara - Explosivo!",
        "descricao": "Um chá aromático servido no Robin História Café.",
        "valor": 6.99,
        "disponivel": true
    }
   ```
2. **Consultar Restaurantes**:
   - Endpoint: `/consulta_restaurante/{id}`, Método: GET.
   - Use este endpoint para obter uma lista de restaurantes.

   
3. **Consultar Todos Restaurantes**:
   - Endpoint: `/consulta_all`, Método: GET.
   - Use este endpoint para obter uma lista de todos restaurantes.

   
4. **Atualizar Restaurantes**:
   - Endpoint: `/atualiza_restaurante/{id}`, Método: PUT.
   - Use este endpoint + o id do restaurante para atualizar algum restaurante.
   ```json
   
    {
        "bairro": "string",
        "categoria": "string",
        "cep": "string",
        "cidade": "string",
        "cnpj": "string",
        "descricao": "string",
        "estado": "string",
        "nome": "string",
        "numero": 0,
        "rua": "string"
    }
   ```
   
5. **Consultar Restaurantes dentro de Categoria**:
   - Endpoint: `/consulta_categoria/{categoria}`, Método: GET.
   - Use este endpoint para obter um restaurantes de uma categoria especifica.

   
6. **deletar Restaurantes**:
   - Endpoint: `/delete_restaurante/{id}`, Método: DELETE.
   - Use este endpoint para deletar o restaurante da lista.




## Gerenciando Produtos
1. **Adicionar um Novo Cliente**:
   - Endpoint: `/create_produto`, Método: POST.
   - Forneça informações do produto no corpo da requisição.
   ```json
   
    {
        "descricao": "string",
        "disponivel": 0,
        "id_restaurante": 0,
        "nome_produto": "string",
        "valor": "Unknown Type: float"
    }
   ```

2. **Atualizar Informações de um Produto**:
   - Endpoint: `/atualiza_produto/{id}`, Método: PUT.
   - Passe o ID do produto na requisição mais o body para alterar o produto.
   ```json
   
    {
        "descricao": "string",
        "disponivel": 0,
        "id_restaurante": 0,
        "nome_produto": "string",
        "valor": 0.0
    }
   ```

3. **Consulta Informações de um Produto**:
   - Endpoint: `/consulta_produto/{id}`, Método: GET.
   - Passe o ID do produto e os novos detalhes no corpo da requisição.


4. **Consulta Informações de um Produto por Categoria**:
   - Endpoint: `/consulta_produto_categoria/{categoria}`, Método: GET.
   - Passe o Categoria do produto para consultar informações.


5. **Consulta Informações de um Produto por Restaurante**:
   - Endpoint: `/consulta_restaurante/{id}`, Método: GET.
   - Passe o ID do restaurante para consultar.


6. **Atualizar Informações de um Produto**:
   - Endpoint: `/delete_produto/{id}`, Método: DELETE.
   - Passe o ID do produto para deletar o produto.



## Gerenciando Entregadores 
1. **Registrar um Entregador**:
   - Endpoint: `/create_entregador`, Método: POST.
   - Inclua as informações do entregador.
   ```json
   
    {
        "cpf": "string",
        "disponivel": true,
        "email": "string",
        "nome": "string",
        "placa": "string",
        "telefone": "string",
        "tipo_veiculo": "string"
    }
   ```

2. **Atualiza Entregador**:
   - Endpoint: `/atualiza_entregador/{id}`, Método: PUT.
   - Use este endpoint para atualizar um Entregador.
   ```json
   
    {  
        "cpf": "string",
        "disponivel": true,
        "email": "string",
        "nome": "string",
        "placa": "string",
        "telefone": "string",
        "tipo_veiculo": "string"
    }
   ```

3. **Consultar Todos Entregadores**:
   - Endpoint: `/consulta_all`, Método: GET.
   - Use este endpoint para obter uma lista de todos Entregador.


4. **Consultar Entregador**:
   - Endpoint: `/consulta_entregador/{id}`, Método: GET.
   - Use este endpoint para obter um Entregador de acordo com o ID passado.

5. **Consultar Entregador Disponivel**:
   - Endpoint: `/consulta_entregador_disponivel`, Método: GET.
   - Use este endpoint para obter uma lista de Entregadores Disponiveis.


6. **Consultar Entregador Indisponivel**:
   - Endpoint: `/seleciona_entregador`, Método: GET.
   - Use este endpoint para obter uma lista de Entregadores Indisponiveis.


7. **Atualiza Entregador para Disponivel**:
   - Endpoint: `/atualiza_entregador_disponivel/{id}`, Método: PUT.
   - Use este endpoint para obter um Entregador **DISPONIVEL** de acordo com o ID passado.


8. **Atualiza Entregador para Indisponivel**:
   - Endpoint: `/atualiza_entregador_indisponivel/{id}`, Método: PUT.
   - Use este endpoint para obter uma lista de Entregador.
   - Use este endpoint para obter um Entregador **INDISPONIVEL** de acordo com o ID passado.


9. **Deletar Entregador**:
   - Endpoint: `/delete_entregador/{id}`, Método: DELETE.
   - Use este endpoint para deletar um Entregador.



## Gerenciando Clientes 
1. **Adicionar um Novo Cliente**:
   - Endpoint: `/create_cliente`, Método: POST.
   - Forneça informações do cliente no corpo da requisição.

   ```json
   
    {
        "cpf": "string",
        "data_nascimento": "2024-01-27",
        "email": "string",
        "nome": "string",
        "telefone": "string"
    }
   ```

2. **Atualizar Informações de um Cliente**:
   - Endpoint: `/atualiza_cliente/{id}`, Método: PUT.
   - Passe o ID do cliente e os novos detalhes no corpo da requisição.

   ```json
   
    {
        "cpf": "string",
        "data_nascimento": "2024-01-27",
        "email": "string",
        "nome": "string",
        "telefone": "string"
    }
   ```

3. **Consulta Informações de um Cliente**:
   - Endpoint: `/consulta_cliente/{id}`, Método: GET.
   - Passe o ID do cliente para receber a descrição dele.


4. **Consulta Informações de um Cliente pelo CPF**:
   - Endpoint: `/consulta_cliente_cpf/{cpf}`, Método: GET.
   - Passe o CPF do cliente para receber a descrição dele.


5. **Atualizar Informações de um Cliente**:
   - Endpoint: `/delete_cliente`, Método: DELETE.
   - Passe o ID do cliente para deletar da base.




##  Gerenciando EnderecoClientes 
1. **Adicionar um Novo EnderecoClientes (`create_EnderecoClientes.yaml`)**:
   - Endpoint: `/create_EnderecoClientes`, Método: POST.
   - Forneça informações do EnderecoClientes no corpo da requisição.

   ```json
   
    {
        "bairro": "string",
        "cep": "string",
        "cidade": "string",
        "complemento": "string",
        "estado": "string",
        "id_cliente": 0,
        "numero": 0,
        "rua": "string"
    }
   ```

2. **Atualizar Informações de um EnderecoClientes (`atualiza_enderecoclientes.yaml`)**:
   - Endpoint: `/atualiza_enderecoclientes/{id}`, Método: PUT.
   - Passe o ID do EnderecoClientes e os novos detalhes no corpo da requisição.

   ```json
   
    {
        "bairro": "string",
        "cep": "string",
        "cidade": "string",
        "complemento": "string",
        "estado": "string",
        "id_cliente": 0,
        "numero": 0,
        "rua": "string"
    }
   ```

2. **Consulta Informações de um EnderecoClientes (`consulta_enderecoclientes.yaml`)**:
   - Endpoint: `/consulta_enderecoclientes/{id}`, Método: GET.
   - Passe o ID do EnderecoClientes e receba as informações.


2. **Deleta Informações de um EnderecoClientes (`delete_enderecoclientes.yaml`)**:
   - Endpoint: `/delete_enderecoclientes/{id}`, Método: DELETE.
   - Passe o ID do EnderecoClientes e delete da base.




## Gerenciando Pedidos 
1. **Criar um Novo Pedido**:
   - Use o endpoint `/create_pedido` com o método POST.
   - Inclua detalhes do pedido no corpo da requisição.

   ```json
   
    {
        "forma_pagamento": "string",
        "id_cliente": 0,
        "id_endereco_cliente": 0,
        "produtos": [
            {
            "descricao": "string",
            "id_produto": 0
            }
        ]
    }
   ```
   
2. **Atualiza um Pedido**:
   - Use o endpoint `/atualiza_pedido/{id}` com o método PUT.
   - Inclua detalhes do pedido no corpo da requisição.

   ```json
   
    {
        "forma_pagamento": "string",
        "id_cliente": 0,
        "id_endereco_cliente": 0,
        "produtos": [
            {
            "descricao": "string",
            "id_produto": 0
            }
        ]
    }
   ```
3. **Atualiza um Pedido para 'A Caminho'**:
   - Use o endpoint `/atualiza_pedido_a_caminho/{id}` com o método PUT.
   - Atualização para mudar o status do pedido para 'A Caminho'.

   
4. **Atualiza um Pedido para 'Aguardando'**:
   - Use o endpoint `/atualiza_pedido_aguardando/{id}` com o método PUT.
   - Atualização para mudar o status do pedido para 'Aguardando'.

   
5. **Atualiza um Pedido para 'Entregue'**:
   - Use o endpoint `/atualiza_pedido_pago_entregue/{id}` com o método PUT.
   - Atualização para mudar o status do pedido para 'Entregue'.

   
6. **Atualiza um Pedido para 'Em preparacao'**:
   - Use o endpoint `/atualiza_pedido_preparacao/{id}` com o método PUT.
   - Atualização para mudar o status do pedido para 'Em preparação'.

   
7. **Consultar um Pedido**:
   - Use o endpoint `/consulta_pedido/{id}` com o método GET.
   - Consulte um pedido.

   
8. **Consultar um Pedido com base no Status**:
   - Use o endpoint `/consulta_pedido_status/{id}` com o método GET.
   - Consulte pedidos com base no status de pedido.

   
9. **Consultar todos os Pedidos**:
   - Use o endpoint `/consulta_all_pedido_status` com o método GET.
   -Consulte todos os pedidos.

   
10. **Delete um  Pedido**:
   - Use o endpoint `/delete_pedido/{id}` com o método DELETE.
   - Inclua detalhes do pedido no corpo da requisição.

   





## Gerenciando Fatura 
1. **Criar um Novo Fatura**:
   - Use o endpoint `/create_fatura` com o método POST.
   - Inclua detalhes do Fatura no corpo da requisição.
   
   ```json
   
    {
        "id_pedido": "",
        "id_cliente": "Sat, 16 Sep 2023 21:47:25 GMT",
        "valor": "Wed, 05 May 2004 00:00:00 GMT",
        "status": "luffy@pirateking.com"

    }
   ```

2. **Atualiza uma Fatura**:
   - Use o endpoint `/atualiza_fatura` com o método PUT.
   - Inclua detalhes do Fatura no corpo da requisição.
   
   ```json
   
    {
        "id_pedido": "",
        "id_cliente": "Sat, 16 Sep 2023 21:47:25 GMT",
        "valor": "Wed, 05 May 2004 00:00:00 GMT",
        "status": "luffy@pirateking.com"

    }
   ```

3. **Atualiza uma Fatura para Pago**:
   - Use o endpoint `/atualiza_fatura_pago/{id}` com o método PUT.
   - Muda o status da fatura para **Pago**.
   

4. **Atualiza uma Fatura para Não Pago**:
   - Use o endpoint `/atualiza_fatura_nao_pago/{id}` com o método PUT.
   - Muda o status da fatura para **Não Pago**.
   

5. **Criar um Novo Fatura para Cancelado**:
   - Use o endpoint `/atualiza_fatura_cancelado/{id}` com o método PUT.
   - Muda o status da fatura para **Cancelado**.
   

6. **consulta uma Fatura**:
   - Use o endpoint `/consulta_fatura` com o método get.
   - Inclua detalhes do Fatura no corpo da requisição.
   


## Gerenciando Avaliação 
1. **Criar um Novo Avaliação**:
   - Use o endpoint `/create_avaliacao` com o método POST.
   - Inclua detalhes do Avaliação no corpo da requisição.
   
   ```json
   
    {
        "comentario": "string",
        "data_avaliacao": "2024-01-27",
        "nota": 0,
        "referencia": "string",
        "tipo": "string"

    }
   ```

2. **Atualiza uma Avaliação**:
   - Use o endpoint `/atualiza_avaliacao/{id}` com o método PUT.
   - Inclua detalhes do Avaliação no corpo da requisição.
   
   ```json
   
    {
        "comentario": "string",
        "data_avaliacao": "2024-01-27",
        "nota": 0,
        "referencia": "string",
        "tipo": "string"

    }
   ```

3. **Consulta uma Avaliação**:
   - Use o endpoint `/consulta_avaliacao/{id}` com o método GET.
   - Consulta uma avaliação com base no id informado.


4. **Delete uma Avaliação**:
   - Use o endpoint `/delete_avaliacao/{id}` com o método DELETE.
   - Deleta uma avaliação com base no id informado
   
</details>









## **Passo 5: Práticas Recomendadas**
- **Segurança**: Mantenha sua API Key segura e não a compartilhe.
- **Eficiência nas Requisições**: Evite requisições desnecessárias para não sobrecarregar o sistema.

## **Passo 6: Suporte e Ajuda**
- Se tiver dúvidas ou problemas, entre em contato com nosso suporte técnico através do Aluno **Leonilson Sousa de Alencar Filho**.

