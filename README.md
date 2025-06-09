# Full-Stack-Cadastro-Estacionamento

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.x-brightgreen.svg)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-14%2B-blue.svg)](https://www.postgresql.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Built with Docker](https://img.shields.io/badge/Built%20with-Docker-blue.svg)](https://www.docker.com/) 
 
--- 

## 📄 Sumário

* [Visão Geral do Projeto](#-visão-geral-do-projeto)
* [Objetivos](#-objetivos)
* [Funcionalidades Principais](#-funcionalidades-principais)
* [Tecnologias Utilizadas](#-tecnologias-utilizadas)
* [Arquitetura do Sistema](#-arquitetura-do-sistema)
    * [Arquitetura Lógica](#arquitetura-lógica)
    * [Arquitetura Física/Implantação](#arquitetura-físicadeploymente)
* [Como Começar](#-como-começar)
    * [Pré-requisitos](#pré-requisitos)
    * [Instalação e Configuração (Ambiente de Desenvolvimento)](#instalação-e-configuração-ambiente-de-desenvolvimento)
    * [Execução do Projeto](#execução-do-projeto)
* [Testes](#-testes)
* [Documentação da API](#-documentação-da-api)
* [Estrutura do Projeto](#-estrutura-do-projeto)
* [Contribuição](#-contribuição)
* [Licença](#-licença)
* [Autores](#-autores)

---

## 🚀 Visão Geral do Projeto

O **Sistema de Cadastro de Estacionamento** é uma aplicação web Full-Stack desenvolvida com o objetivo de modernizar e automatizar a gestão de veículos em estacionamentos de instituições e empresas. Este projeto visa substituir métodos de controle manuais por uma solução digital eficiente, segura e escalável, proporcionando um gerenciamento otimizado de clientes, veículos, vagas, e registros de entrada e saída.

O sistema permite o cadastro completo de entidades, oferece funcionalidades de autenticação e filtros avançados, e integra-se com serviços externos para autocompletar dados de veículos e notificar proprietários em tempo real.

## 🎯 Objetivos

* **Modernizar e Automatizar:** Transformar o processo manual de gestão de estacionamento em um sistema digital.
* **Controle Eficiente:** Proporcionar um controle preciso e em tempo real da ocupação de vagas e movimentação de veículos.
* **Melhorar a Experiência do Usuário:** Oferecer acesso simplificado aos clientes para visualizarem seus próprios registros e veículos.
* **Comunicação Efetiva:** Notificar proprietários sobre a entrada e saída de seus veículos.
* **Escalabilidade e Manutenibilidade:** Construir uma solução robusta que possa crescer e ser facilmente mantida.

## ✨ Funcionalidades Principais

* **Cadastros Completos:** Gerenciamento de clientes, veículos, vagas e registros de entrada/saída.
* **Autenticação e Autorização:** Sistema de login seguro com controle de usuários, acessos e permissões.
* **Acesso de Clientes:** Clientes podem visualizar seus veículos e registros de estacionamento.
* **Autocompletar Dados de Veículos:** Preenchimento automático de informações do veículo (marca, modelo, cor) ao informar a placa, via consulta a uma API externa.
* **Notificações em Tempo Real:** Envio de notificações via WhatsApp (Evolution API) e E-mail (SMTP) aos proprietários na entrada e saída dos veículos.
* **Status de Vagas Automático:** Atualização automática do status das vagas (ocupado/livre) ao registrar entradas e saídas.
* **Sistema de Administração Interno:** Painel administrativo para gerenciamento completo do sistema (via Jazzmin).
* **API RESTful:** Exposição de endpoints para futuras integrações e comunicação eficiente entre frontend e backend.

## 🛠️ Tecnologias Utilizadas

O projeto foi desenvolvido utilizando um stack tecnológico moderno e robusto:

* **Linguagem de Programação:** Python 3.x
* **Framework Web:** Django (para o backend e a lógica de negócio).
* **Banco de Dados:**
    * SQLite3 (para desenvolvimento local rápido e inicial).
    * PostgreSQL (recomendado para ambientes de produção, conforme requisitos).
* **API / Autenticação:**
    * Django REST Framework: Construção de APIs RESTful.
    * JWT Token: Autenticação segura e sem estado para a API.
    * RQL: Linguagem de consulta para filtragem de dados na API.
* **Processamento Assíncrono:**
    * Celery: Fila de tarefas distribuída para processamento em segundo plano (ex: autocompletar dados de veículos, notificações).
    * RabbitMQ: Broker de mensagens que atua como a fila para o Celery.
* **Comunicação Externa:**
    * Evolution API: Serviço de integração para envio de notificações via WhatsApp.
    * SMTP: Protocolo para envio de notificações via e-mail.
* **Contêinerização:** Docker (para empacotamento e execução consistente em diferentes ambientes).
* **Qualidade de Código:**
    * Linter: Para garantir a consistência e qualidade do código.
    * PEP08: Guia de estilo de código Python.
* **Documentação da API:** Swagger (para documentação interativa e visualização dos endpoints da API).
* **Painel Administrativo:** Jazzmin (customização e melhoria da interface de administração do Django).

## 🏛️ Arquitetura do Sistema

A arquitetura do Sistema de Cadastro de Estacionamento é baseada em um modelo de **Arquitetura em Camadas (Layered Architecture)**, promovendo a separação de responsabilidades e a modularidade.

### Arquitetura Lógica

O diagrama abaixo ilustra a organização lógica dos componentes e suas interações:

```plantuml
@startuml
component "Frontend (Browser/Mobile)" as Frontend
component "Backend API (Django REST Framework)" as Backend
database "Banco de Dados (PostgreSQL)" as DB
component "Fila de Tarefas (RabbitMQ)" as RabbitMQ
component "Worker de Tarefas (Celery)" as Celery
component "Serviço de Notificação (Evolution API/SMTP)" as NotificationService
component "API Externa de Consulta de Veículos" as APIExterna
component "Dashboard Administrativo (Jazzmin)" as AdminDashboard

Frontend --> Backend : Requisições HTTP/HTTPS
Backend --> DB : Acesso a Dados (ORM Django)
Backend --> RabbitMQ : Enviar Tarefas Assíncronas
RabbitMQ --> Celery : Consumir Tarefas
Celery --> NotificationService : Enviar Notificações (WhatsApp/Email)
Celery --> APIExterna : Consulta de Dados de Veículos
AdminDashboard --> Backend : Gerenciamento (Django Admin)
@enduml
Como visualizar o diagrama: Copie o código acima e cole em um editor PlantUML online (como http://www.plantuml.com/plantuml/) ou em uma ferramenta com suporte a PlantUML para gerar a imagem.

Arquitetura Física/Implantação
O sistema é projetado para ser implantado utilizando Docker Containers, garantindo portabilidade, isolamento e escalabilidade.

Snippet de código

@startuml
node "Servidor de Aplicação" {
  folder "Container Web Server (Nginx)" as Nginx {
    component "Gunicorn" as Gunicorn
  }
  folder "Container Aplicação Django" as DjangoApp
  folder "Container Banco de Dados (PostgreSQL)" as DBContainer
  folder "Container Fila de Mensagens (RabbitMQ)" as RabbitMQContainer
  folder "Container Worker de Tarefas (Celery)" as CeleryContainer
}

cloud "Internet" as Internet {
  cloud "API Externa de Consulta de Veículos" as ExternalAPI
  cloud "Serviço WhatsApp (Evolution API)" as WhatsAppAPI
  cloud "Serviço E-mail (SMTP)" as EmailSMTP
}

user "Usuário Cliente" as ClientUser
user "Usuário Administrativo" as AdminUser

ClientUser --> Internet
AdminUser --> Internet
Internet --> Nginx : Requisições HTTP/HTTPS
Nginx --> Gunicorn : Comunicação Proxy Reversa
Gunicorn --> DjangoApp : Comunicação WSGI
DjangoApp --> DBContainer : Conexão BD
DjangoApp --> RabbitMQContainer : Publicar Mensagens

RabbitMQContainer --> CeleryContainer : Consumir Mensagens
CeleryContainer --> ExternalAPI : Consulta de Placa
CeleryContainer --> WhatsAppAPI : Envio WhatsApp
CeleryContainer --> EmailSMTP : Envio E-mail
@enduml
Como visualizar o diagrama: Copie o código acima e cole em um editor PlantUML online ou em uma ferramenta com suporte a PlantUML para gerar a imagem.

🚀 Como Começar
Para configurar e executar o projeto em seu ambiente de desenvolvimento:

Pré-requisitos
Certifique-se de ter instalado:

Python 3.x
pip (gerenciador de pacotes do Python)
Git
Docker e Docker Compose (opcional, mas recomendado para ambiente de desenvolvimento/produção)
Instalação e Configuração (Ambiente de Desenvolvimento)
Clone o Repositório:

Bash

git clone [https://github.com/P4dro-Dev/Full-Stack-Cadastro-Estacionamento.git](https://github.com/P4dro-Dev/Full-Stack-Cadastro-Estacionamento.git)
cd Full-Stack-Cadastro-Estacionamento
Crie e Ative um Ambiente Virtual:

Bash

python -m venv venv
# No Windows
.\venv\Scripts\activate
# No Linux/macOS
source venv/bin/activate
Instale as Dependências:

Bash

pip install -r requirements.txt # Certifique-se de ter um arquivo requirements.txt com as dependências do projeto
Se requirements.txt não existir, você pode gerar um com pip freeze > requirements.txt após instalar as bibliotecas.

Configurações do Projeto (Arquivo .env):
Crie um arquivo .env na raiz do projeto (ou configure diretamente em core/settings.py para desenvolvimento) com variáveis de ambiente para chaves de API, configurações de e-mail, etc.
Exemplo de .env:

SECRET_KEY='sua_chave_secreta_django'
DEBUG=True
ALLOWED_HOSTS='*'
DATABASE_URL='sqlite:///db.sqlite3' # Para desenvolvimento com SQLite
# Ou para PostgreSQL:
# DATABASE_URL='postgresql://user:password@host:port/dbname'
# EVOLUTION_API_URL='url_da_evolution_api'
# EVOLUTION_API_TOKEN='seu_token_evolution_api'
# EMAIL_HOST='seu_host_smtp'
# EMAIL_PORT='porta_smtp'
# EMAIL_USE_TLS=True
# EMAIL_HOST_USER='seu_email'
# EMAIL_HOST_PASSWORD='sua_senha_email'
Aplique as Migrações do Banco de Dados:

Bash

python manage.py migrate
Crie um Superusuário (para acesso ao Admin Django):

Bash

python manage.py createsuperuser
Execução do Projeto
Inicie o Servidor de Desenvolvimento Django:

Bash

python manage.py runserver
O sistema estará acessível em http://127.0.0.1:8000/. O painel administrativo estará em http://127.0.0.1:8000/admin/.

Inicie os Workers Celery (em um terminal separado):
Para processar tarefas assíncronas (como autocompletar e notificações), você precisará de um broker de mensagens (RabbitMQ) e workers Celery.

Com Docker Compose (Recomendado): Se você tiver um docker-compose.yml para RabbitMQ e Celery, inicie-os:
Bash

docker-compose up -d rabbitmq celery
Sem Docker (se RabbitMQ e Redis estiverem instalados localmente):
Bash

celery -A core worker -l info
🧪 Testes
O projeto inclui uma suíte de testes abrangente para garantir a qualidade e o correto funcionamento das funcionalidades.

Para executar todos os testes:

Bash

python manage.py test
Para gerar um relatório de cobertura de código (requer coverage.py instalado: pip install coverage):

Bash

coverage run manage.py test
coverage report
coverage html # Para um relatório HTML detalhado
📚 Documentação da API
A documentação da API RESTful é gerada automaticamente usando Swagger (se implementado e configurado no projeto). Uma vez que o servidor esteja rodando, a documentação estará disponível em um endpoint específico, como http://127.0.0.1:8000/swagger/ ou http://127.0.0.1:8000/redoc/.

📁 Estrutura do Projeto
A estrutura principal do projeto segue a convenção do Django:

.
├── core/                  # Configurações globais do Django
├── customers/             # Módulo de gerenciamento de clientes
│   ├── migrations/
│   ├── models.py          # Definição do modelo Customer
│   └── admin.py           # Configurações do admin para Customer
├── vehicles/              # Módulo de gerenciamento de veículos
│   ├── migrations/
│   ├── models.py          # Definição dos modelos VehicleType, Vehicle
│   └── admin.py           # Configurações do admin para VehicleType, Vehicle
├── parking/               # Módulo de gerenciamento de estacionamento e registros
│   ├── migrations/
│   ├── models.py          # Definição dos modelos ParkingSpot, ParkingRecord
│   ├── signals.py         # Lógica para atualização automática de vagas
│   └── admin.py           # Configurações do admin para ParkingSpot, ParkingRecord
├── venv/                  # Ambiente virtual (ignorada pelo Git)
├── manage.py              # Utilitário de linha de comando do Django
├── requirements.txt       # Dependências do projeto
├── .env.example           # Exemplo de arquivo de variáveis de ambiente
└── README.md              # Este arquivo
🤝 Contribuição
Contribuições são bem-vindas! Se você deseja contribuir com o projeto, siga estes passos:

Faça um fork do repositório.
Crie uma nova branch (git checkout -b feature/sua-feature).
Implemente suas alterações e escreva testes adequados.
Execute os testes e verifique a cobertura.
Faça commit de suas alterações (git commit -m 'feat: Adiciona nova funcionalidade X').
Envie para a branch original (git push origin feature/sua-feature).
Abra um Pull Request.
📝 Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

👥 Autores
P4dro-Dev
Rafael Roseno
