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
- **Obtenção de Credenciais**: Para usar a API, primeiro obtenha suas credenciais (API Key) através do nosso portal de usuário.
- **Configuração do Ambiente**: Instale as ferramentas necessárias, como Postman ou cURL, para fazer requisições à API.

## **Passo 3: Autenticação**
- **Utilizando a API Key**: Em todas as suas requisições, inclua a API Key no cabeçalho para autenticação.

## **Passo 4: Realizando Operações Básicas**
1. **Criar um Novo Pedido (`create_pedido.yaml`)**:
   - Use o endpoint `/create_pedido` com o método POST.
   - Inclua detalhes do pedido no corpo da requisição.
2. **Consultar Pedidos (`get_pedido.yaml`)**:
   - Acesse o endpoint `/get_pedido` com o método GET para ver detalhes de um pedido específico.

## **Passo 5: Gerenciando Clientes e Produtos**
1. **Adicionar um Novo Cliente (`create_cliente.yaml`)**:
   - Endpoint: `/create_cliente`, Método: POST.
   - Forneça informações do cliente no corpo da requisição.
2. **Atualizar Informações de um Produto (`update_produto.yaml`)**:
   - Endpoint: `/update_produto`, Método: PUT.
   - Passe o ID do produto e os novos detalhes no corpo da requisição.

## **Passo 6: Trabalhando com Entregadores e Restaurantes**
1. **Registrar um Entregador (`create_entregador.yaml`)**:
   - Endpoint: `/create_entregador`, Método: POST.
   - Inclua as informações do entregador.
2. **Consultar Restaurantes (`get_restaurantes.yaml`)**:
   - Endpoint: `/get_restaurantes`, Método: GET.
   - Use este endpoint para obter uma lista de restaurantes.

## **Passo 7: Práticas Recomendadas**
- **Segurança**: Mantenha sua API Key segura e não a compartilhe.
- **Eficiência nas Requisições**: Evite requisições desnecessárias para não sobrecarregar o sistema.

## **Passo 8: Suporte e Ajuda**
- Se tiver dúvidas ou problemas, consulte nossa seção de FAQs ou entre em contato com nosso suporte técnico através do [suporte@apiempresa.com].
