from flask import render_template, request, redirect, session, flash, url_for, send_from_directory
import time

import sys
import logging

from models import Jogo
from dao import JogoDao, UsuarioDao

from helpers import deleta_arquivo, recupera_imagem
from app import db, app


jogo_dao = JogoDao(db)
usuario_dao = UsuarioDao(db)


@app.route('/')
def index():
    lista = jogo_dao.listar()
    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Novo Jogo')


@app.route('/criar', methods=['POST','GET'])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    jogo = jogo_dao.salvar(jogo)

    arquivo = request.files['arquivo']
    upload_path = app.config['UPLOAD_PATH']
    timestamp = time.time()
    arquivo.save(f'{upload_path}/capa{jogo.id}-{timestamp}.jpg')
    return redirect(url_for('index'))


@app.route('/editar/<int:id>')
def editar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        flash('Você precisa estar logado para isso!')
        return redirect(url_for('login', proxima=url_for('index')))
    else:
        jogo = jogo_dao.busca_por_id(id)
        nome_imagem = recupera_imagem(id)
        capa_jogo = f'capa{id}.jpg'
        return render_template('editar.html', titulo='Editando jogo', jogo=jogo, capa_jogo=nome_imagem)

@app.route('/jogo/<int:id>')
def info(id):
    jogo = jogo_dao.busca_por_id(id)
    nome_imagem = recupera_imagem(id)
    capa_jogo = f'capa{id}.jpg'
    return render_template('jogo.html', titulo=f" {jogo.nome} - {jogo.console}", jogo=jogo, capa_jogo=nome_imagem)


@app.route('/atualizar', methods=['POST','GET'])
def atualizar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console, id=request.form['id'])
    jogo_dao.salvar(jogo)

    arquivo = request.files['arquivo']
    upload_path = app.config['UPLOAD_PATH']
    timestamp = time.time()

    arquivo.save(f'{upload_path}/capa{jogo.id}-{timestamp}.jpg')
    deleta_arquivo(jogo.id)
    flash('O jogo foi editado com sucesso!')
    return redirect(url_for('index'))


@app.route('/deletar/<int:id>')
def deletar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        flash('Você precisa estar logado para isso!')
        return redirect(url_for('login', proxima=url_for('index')))
    jogo_dao.deletar(id)
    flash('O jogo foi removido com sucesso!')
    return redirect(url_for('index'))


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    if proxima == None:
        proxima = '/'
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return render_template('login.html', proxima=proxima, titulo='Faça seu Login')
    else:
        flash('Você já esta logado!')
        return redirect(url_for('index'))


@app.route('/autenticar', methods=['POST','GET'])
def autenticar():
    usuario = usuario_dao.buscar_por_id(request.form['usuario'])
    if usuario:
        if usuario.senha == request.form['senha']:
            session['usuario_logado'] = usuario.id
            flash(usuario.nome + ' logou com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('Usuário não logado.')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        flash('Você não está logado!')
    else:
        session['usuario_logado'] = None
        flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))


@app.route('/uploads/<nome_arquivo>')
def imagem(nome_arquivo):
    return send_from_directory('uploads', nome_arquivo)