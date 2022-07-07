# TCC II

## Desenvolvimento prático do projeto:

Este projeto representa a implementação do [artigo de TCC](link_do_artigo.com.br) da Unisociesc que envolve os alunos:

- Everton Freire Segur
- Luis Fernando Bezerra da Silva

O mesmo contém um dataset configurado dinamicamente para simular acessos de pessoas a qualquer ambiente protegido.
Devido ao tempo disposto para realizarmos demais testes nos limitamos ao uso de um dado imutável e um dado mutável
simulando um relacionamento de confiança, tal como disposto no artigo mencionado acima.

### Projetos no repositório:

* Serviço de autorização web com machine learning em python
* Serviço de SSO web utilizando Keycloak
* Serviço web visual para input dos dados

## Instruções

Ao iniciar o projeto é necessário definir um usuário de login. Esta configuração pode ser realizada através dos
seguintes passos:

1. [Acesso ao SSO](http://localhost:8083/auth/realms/master/protocol/openid-connect/auth?client_id=security-admin-console&redirect_uri=http%3A%2F%2Flocalhost%3A8083%2Fauth%2Fadmin%2Fmaster%2Fconsole%2F%23%2Frealms%2Fbaeldung%2Fusers%2F8fa8ea4c-3116-4995-9c58-0723ea0051d3&state=5c7fa663-0d72-40ec-8271-5bb2a1509a9c&response_mode=fragment&response_type=code&scope=openid&nonce=3290798f-514e-498f-8ac6-8d5c2d289fe2&code_challenge=oZwOusL01jq6wPTizXIbUFFPBqpjBT2wDHaJb1dKhJE&code_challenge_method=S256)
2. Utilize o usuário e senha definidos em `sso/sso-authorization-server/src/main/resources/application.yml`
   como keycloak.server.adminUser
3. [Acesso aos usuários](http://localhost:8083/auth/admin/master/console/#/realms/baeldung/users)
4. Adicione o usuário conforme desejado e altere a senha em credentials. *Temos um exemplo utilizando o usuário: `user1`
   e senha: `1`*
5. [Acesso ao enpoint](http://localhost:3000/)

## Como executar

### Para gerenciar as aplicações são disponibilizados os comandos:

Iniciar `make run-all`

Parar `make stop-all`

### Para efetuar login via shell são disponibilizados os comandos:

Executar autenticação pelo sso `execute-auth-on-token`

Executar autenticação diretamente na api de ML `execute-auth-on-ia`

### Para realizar login via navegador:

- [Login via interface web](http://localhost:3000)

# Creditos

Everton:

- [Linkedin](https://www.linkedin.com/in/everton-freire/)
- [Github](https://github.com/devsegur)

Luis:

- [Linkedin](/dev/null)
- [Github](/dev/null)