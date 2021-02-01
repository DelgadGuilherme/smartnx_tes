from app import app
from flask import Flask, render_template, Response, request, redirect, url_for
from model.cliente import Cliente, banco
import json


@app.route('/')
def index():
    clientes = Cliente.query.all()
    result = [cliente.to_dict() for cliente in clientes]
    Response(response=json.dumps(result), status=200, content_type='applications/json')
    return render_template('index.html', clientes = clientes) 


@app.route('/cliente/busca', methods=['GET'])
def view():
    cliente_codigo = request.args.get('codigo')
    if cliente_codigo:
        cliente =  Cliente.query.get(cliente_codigo)
        Response(response=json.dumps(cliente.to_dict()), status = 200, content_type='application/json')
        return render_template('busca.html', cliente = cliente)

@app.route('/adicionar', methods=['GET','POST'])
def add():
    if request.method == 'POST':
        cliente = Cliente(request.form['nome'], request.form['razao_social'], request.form['cnpj'], request.form['data_inclusao'])
        banco.session.add(cliente)
        banco.session.commit()
        Response(response=json.dumps(cliente.to_dict()), status=200, content_type='applications/json')
        return redirect(url_for('index'))
    return render_template('adicionar.html')


@app.route('/editar/<int:codigo>', methods=['GET', 'POST'])
def edit(codigo):
    cliente =  Cliente.query.get(codigo)
    if request.method == 'POST':
        cliente.nome = request.form['nome']
        cliente.razao_social = request.form['razao_social']
        cliente.cnpj = request.form['cnpj']
        cliente.data_inclusao = request.form['data_inclusao']
        banco.session.commit()
        return redirect(url_for('index'))
    return render_template('editar.html', cliente = cliente)


@app.route('/delete/<int:codigo>', methods=['GET','DELETE'])
def delete(codigo):
    cliente = Cliente.query.get(codigo)
    banco.session.delete(cliente)
    banco.session.commit()
    Response(response=json.dumps(cliente.to_dict()), status = 200, content_type='application/json')
    return redirect(url_for('index'))
