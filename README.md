# ✈️ SkyControl Aviation Management

Sistema web para gerenciamento aeronáutico desenvolvido com Flask, SQLAlchemy e SQLite.

---

## 📋 Funcionalidades

- 📊 Dashboard com estatísticas
- ✈️ Cadastro de Aeronaves
- 👨‍✈️ Cadastro de Pilotos
- 🌎 Cadastro de Aeroportos
- 🛫 Cadastro de Voos
- 🔗 Relacionamento entre tabelas
- 🎨 Interface moderna e responsiva

---

## 🏗️ Estrutura do Projeto

```text
SkyControl
│
├── backend
│   ├── routes
│   │   ├── avioes.py
│   │   ├── pilotos.py
│   │   ├── aeroportos.py
│   │   └── voos.py
│   │
│   ├── app.py
│   ├── database.py
│   └── models.py
│
├── database
│   └── aviacao.db
│
├── frontend
│   ├── templates
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── avioes.html
│   │   ├── pilotos.html
│   │   ├── aeroportos.html
│   │   └── voos.html
│   │
│   └── static
│       ├── css
│       │   └── style.css
│       └── js
│
└── README.md
```

---

## 💻 Tecnologias Utilizadas

- Python
- Flask
- SQLAlchemy
- SQLite
- HTML5
- CSS3

---

## 🚀 Como Executar

Instale as dependências:

```bash
pip install flask
pip install flask-sqlalchemy
```

Execute o projeto:

```bash
python backend/app.py
```

Acesse:

```text
http://127.0.0.1:5000
```

---

## 👩‍💻 Desenvolvedora

**Rayssa Rebeca**

Projeto desenvolvido para fins acadêmicos e aprendizado de desenvolvimento web com Flask.