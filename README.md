# Nome: Agenda Cultural do Vale

## 📌O que busca resolver?
O sistema busca resolver a dificuldade de acesso a informações sobre eventos culturais realizados no Vale do São Francisco. Atualmente, essas informações costumam estar dispersas em diferentes redes sociais, sites e meios de comunicação, dificultando que a população acompanhe a programação cultural da região. A plataforma propõe centralizar em um único ambiente os eventos que acontecem não apenas em Petrolina e Juazeiro, mas também em cidades e localidades próximas, oferecendo uma forma organizada, acessível e prática para que moradores e visitantes encontrem informações sobre atividades culturais, artísticas e comunitárias.
---

## 👥 Tipos de Usuários

O sistema possui dois tipos de usuários:

### Usuário Comum

Usuário responsável por cadastrar e gerenciar seus próprios eventos culturais.

### Administrador

Usuário responsável pela supervisão geral da plataforma e gerenciamento de todos os eventos cadastrados.

---

## 🔐 Funcionalidades por Tipo de Usuário

### Usuário Comum

Após realizar cadastro e login, o usuário pode:

- Cadastrar novos eventos;
- Visualizar seus eventos cadastrados;
- Editar seus eventos;
- Excluir seus eventos;
- Visualizar todos os eventos disponíveis na página inicial.

### Administrador

Após realizar login, o administrador pode:

- Visualizar todos os eventos cadastrados no sistema;
- Editar qualquer evento;
- Excluir qualquer evento;
- Gerenciar o conteúdo disponível na plataforma.

---

## 🛠 Tecnologias Utilizadas

- Python
- Django
- SQLite
- HTML5
- CSS3
- Bootstrap 5

---

## 🚀 Passo a passo para instalação e execução do projeto em ambiente de testes

### 1. Clonar o repositório

```bash
git clone <url-do-repositorio>
```

### 2. Acessar a pasta do projeto

```bash
cd Agenda-Cultural-do-Vale
```

### 3. Criar o ambiente virtual

```bash
python -m venv venv
```

### 4. Ativar o ambiente virtual

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### 5. Instalar as dependências

```bash
pip install django pillow
```

O pacote **Pillow** é necessário para permitir o upload e a exibição de imagens nos eventos.

### 6. Executar as migrações

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Criar um superusuário administrador

```bash
python manage.py createsuperuser
```

Esse usuário será utilizado para acessar as funcionalidades administrativas do sistema.

### 8. Iniciar o servidor local

```bash
python manage.py runserver
```

### 9. Acessar o sistema

```text
http://127.0.0.1:8000/auth/
```

---

## 📖 Instruções para utilização das principais funcionalidades

### Visualizar eventos

Ao acessar a página inicial, qualquer visitante pode visualizar os eventos cadastrados no sistema, incluindo título, descrição, local, data, categoria e imagem.

### Cadastro de usuário comum

1. Na página inicial, clique em **Cadastrar**;
2. Informe nome de usuário, e-mail e senha;
3. Após o cadastro, realize o login no sistema.

### Login

1. Clique em **Entrar**;
2. Informe o nome de usuário e a senha;
3. Após o login, o sistema exibirá as opções disponíveis conforme o tipo de usuário.

### Cadastro de eventos

Usuários comuns autenticados podem cadastrar eventos:

1. Clique em **Cadastrar Evento**;
2. Preencha título, descrição, local, data, categoria e imagem;
3. Clique em **Salvar Evento**.

### Gerenciamento dos próprios eventos

Usuários comuns podem acessar **Meus Eventos** para:

- Visualizar os eventos que cadastraram;
- Editar informações dos seus eventos;
- Excluir seus próprios eventos.

### Gerenciamento pelo administrador

O administrador pode acessar a opção **Todos os Eventos** para:

- Visualizar todos os eventos cadastrados no sistema;
- Editar eventos cadastrados por qualquer usuário;
- Excluir eventos cadastrados por qualquer usuário.

### Logout

Para sair do sistema, clique em **Sair**. Após o logout, o usuário retorna para a página inicial, onde continuam sendo exibidos os eventos cadastrados.

---

## ⚙️ Procedimentos adicionais necessários para utilização do sistema

Após a instalação, é necessário realizar alguns procedimentos para que todas as funcionalidades funcionem corretamente.

### Instalação do Pillow

O sistema possui upload de imagens nos eventos. Por isso, é necessário instalar o pacote Pillow:

```bash
pip install pillow
```
```
### Criação do administrador

Para utilizar as funcionalidades administrativas, é necessário criar um superusuário:

```bash
python manage.py createsuperuser
```

Durante a criação, informe um nome de usuário, e-mail e senha.

Exemplo utilizado para testes:

```text
Usuário: Nunes
Senha: 1234
```

### Acesso do administrador

O administrador pode acessar o sistema pela tela de login comum:

```text
http://127.0.0.1:8000/auth/login/
```

Após o login, o administrador terá acesso à opção **Todos os Eventos**, podendo visualizar, editar e excluir todos os eventos cadastrados.