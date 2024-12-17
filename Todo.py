from flask import Flask, request, redirect, jsonify
import json
import os

app = Flask(__name__)

# Caminho do arquivo JSON onde as tarefas serão armazenadas
TASKS_FILE = 'tasks.json'

# Função para carregar tarefas do arquivo JSON
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r', encoding='utf-8') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []  # Retorna uma lista vazia em caso de erro de leitura
    return []

# Função para salvar tarefas no arquivo JSON
def save_tasks(tarefas):
    with open(TASKS_FILE, 'w', encoding='utf-8') as file:
        json.dump(tarefas, file, ensure_ascii=False, indent=4)

# Carregar as tarefas do arquivo JSON ao iniciar
tarefas = load_tasks()

@app.route('/')
def index():
    lista_tarefas = "<h1>Lista de Tarefas</h1><ul>"
    for i, tarefa in enumerate(tarefas):
        lista_tarefas += f"<li>{tarefa} <a href='/deletar/{i}'>Deletar</a></li>"
    lista_tarefas += "</ul><form method='POST' action='/adicionar'><input name='tarefa' placeholder='Nova Tarefa' required><button type='submit'>Adicionar</button></form>"
    return lista_tarefas

@app.route('/adicionar', methods=['POST'])
def adicionar_tarefa():
    tarefa = request.form.get('tarefa')
    if tarefa:
        tarefas.append(tarefa)
        save_tasks(tarefas)  # Salvar as tarefas no arquivo
    return redirect('/')

@app.route('/deletar/<int:id_tarefa>')
def deletar_tarefa(id_tarefa):
    if 0 <= id_tarefa < len(tarefas):
        tarefas.pop(id_tarefa)
        save_tasks(tarefas)  # Salvar as tarefas no arquivo
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
