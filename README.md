# README - Projeto Case Nelogica - Victor Martins (Atualizado)

Este arquivo README contém informações sobre como configurar e executar o projeto utilizando Docker Compose e um script para facilitar a execução.

## Requisitos

- Docker
- Docker Compose

## Serviços

O projeto consiste nos seguintes serviços:

1. pgAdmin - Interface gráfica para administração do PostgreSQL
2. Postgres - Banco de dados PostgreSQL
3. Postgres Metabase - Banco de dados PostgreSQL para o Metabase
4. Metabase - Aplicação para visualização e análise de dados

## Configuração

1. Clone este repositório.
2. Certifique-se de ter o Docker e o Docker Compose instalados em sua máquina.
3. Navegue até a pasta do projeto.

## Execução

1. Abra um terminal na pasta do projeto e torne o script `run.sh` executável com o seguinte comando:

```
chmod +x run.sh
```

2. Execute o script `run.sh` com o seguinte comando:

```
./run.sh
```

3. Aguarde alguns minutos para que os serviços sejam inicializados e o backup do Metabase seja restaurado.

## Acesso

1. Acesse o Metabase no navegador através do seguinte endereço: http://localhost:3000
2. Faça login com as seguintes credenciais:
   - E-mail: victor@nelogica.com
   - Senha: nelogica1234
3. Após o login, vá para a página de marcadores e clique no dashboard chamado "Case Nelogica - Victor Martins" para visualizar os dados.

## Outros serviços

- pgAdmin: Acesse o pgAdmin no navegador através do seguinte endereço: http://localhost:5050
  - E-mail: victor@nelogica.com
  - Senha: nelogica1234

## Parar os serviços

Para parar os serviços e remover os containers, execute o seguinte comando no terminal:

```
docker-compose down
```

## Suporte

Em caso de problemas ou dúvidas, entre em contato com o autor do projeto através do e-mail: victorfm185@gmail.com# datarisk
