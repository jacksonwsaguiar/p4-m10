# Ponderada 4 - Incremento da P3 Aplicação de Microserviços com Node.js, RabbitMQ e Logs Nginx

Esta aplicação é composta por múltiplos microserviços desenvolvidos em Node.js e Python, utilizando RabbitMQ para comunicação assíncrona entre eles. O objetivo principal é fazer o upload de imagens, processá-las (convertendo para preto e branco), e retornar para o usuário quando o processamento estiver concluído. Além do sistema de logger utilizando o mongoDB como armazenamento.

## Microserviços

1. **Serviço de User (user-service)**
    - Gerencia a criação de contas e o login dos usuários.

2. **Serviço de Processamento de Imagens (proccess-image-service)**
    - Gerencia o upload de imagens pelos usuários.
    - Converte a imagen para preto e branco.
    - Notifica que o processo acabou.
    - Envia logs das etapadas.

3. **Serviço de Log (log-service)**
    - Registra ações dos usuários, como login, criação de conta e upload e processamento de imagens.

4. **Backend base (sistema02)**
    - CRUD de usuarios.
    - CRUD de produtos.

5. **Gateway**
    - Porta de entrada para os microserviços.
    - Logs gerais do sistema.
    - Encaminha as requisições para os serviços apropriados.

## Estrutura do Projeto

```bash
├── user-service
│   ├── server.js
│   ├── Dockerfile
│   └── ...
├── proccess-image-service
│   ├── server.js
│   ├── Dockerfile
│   └── ...
├── logger-service
│   ├── server.js
│   ├── Dockerfile
│   └── ...
├── sistema02
│   ├── main.py
│   ├── logs
│   ├── Dockerfile
│   └── ...
└── gateway
│   ├── nginx.conf
│   ├── Dockerfile
│   └── ...
└── docker-compose.yaml
```
## Executando com docker

```bash
    docker-compose up --build
```

## Detalhes
Os microserviços realizam suas tarefas e para cada nova ação ou enpoint acessado é enviado para o rabbitmq que adiciona no mongoDB o log do ocorrido, na aplicação sistema02 foi incrementado para também executar as mesmas rotinas sendo a cada acesso a api, além de ser gerado o arquivo de log também é enviado para serviço de logger ao qual envia ao NoSql.

Nginx foi configurado para gerar logs mais gerais de toda a aplicação, sendo eles logs de acesso, para cada novo acesso a qualquer endpoint do microserviço ou logs de erro para cada bad request de enpoints.