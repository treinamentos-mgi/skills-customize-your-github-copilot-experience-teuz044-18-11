# 📘 Atividade: Building REST APIs com FastAPI

## 🎯 Objetivo

Aprenda a criar uma API REST com FastAPI, definir modelos de dados e implementar operações HTTP para consultar e modificar recursos.

## 📝 Tarefas

### 🛠️ Criar a Aplicação e uma Rota de Status

#### Descrição
Configure a aplicação FastAPI do código inicial e crie uma rota simples para verificar se o servidor está funcionando.

#### Requisitos
O programa concluído deve:

- Criar uma aplicação FastAPI chamada `app`.
- Implementar `GET /health` para retornar `{"status": "ok"}`.
- Instalar e iniciar a aplicação com os comandos:

  ```bash
  python -m pip install fastapi uvicorn
  python starter-code.py
  ```

- Permitir que a documentação interativa da API seja acessada em `/docs`.

### 🛠️ Listar e Criar Tarefas

#### Descrição
Use os modelos Pydantic fornecidos no código inicial para criar endpoints que listem tarefas e adicionem novas tarefas a uma coleção em memória.

#### Requisitos
O programa concluído deve:

- Implementar `GET /tasks` para retornar todas as tarefas.
- Implementar `POST /tasks` para criar uma tarefa com título e estado de conclusão.
- Atribuir um identificador único a cada tarefa criada.
- Retornar a tarefa criada com o status HTTP `201`.
- Aceitar um corpo JSON como:

  ```json
  {"title": "Revisar APIs", "completed": false}
  ```

### 🛠️ Consultar, Atualizar e Remover Tarefas

#### Descrição
Complete a API com operações para buscar uma tarefa pelo identificador, atualizar seu estado de conclusão e removê-la.

#### Requisitos
O programa concluído deve:

- Implementar `GET /tasks/{task_id}` para retornar uma tarefa específica.
- Implementar `PATCH /tasks/{task_id}` para atualizar o campo `completed`.
- Implementar `DELETE /tasks/{task_id}` para remover uma tarefa existente.
- Retornar o status HTTP `404` quando o identificador não corresponder a uma tarefa.
- Retornar o status HTTP `204` após remover uma tarefa com sucesso.