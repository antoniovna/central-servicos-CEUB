from flask import Blueprint, render_template, request
from database.prestador_tao import PrestadorDAO
from database.setor_dao import SetorDAO

bp_pre = Blueprint('pre', __name__, url_prefix='/admin/prestador')


@bp_pre.route('/incluir')  # /adm/prestador/incluir
def incluir():
    dao_setor = SetorDAO()
    lst_setores = dao_setor.read_by_filters([('sts_setor', '=', 'A')])
    return render_template('adm/prestador/incluir.html', msg="", css_msg="", lst_setores=lst_setores)


@bp_pre.route('/salvar_incluir', methods=['POST'])  # /adm/prestador/salvar_incluir
def salvar_incluir():
    dao = PrestadorDAO()
    pre = dao.new_object()

    pre.mat_prestador = request.form['mat_prestador']
    pre.nme_prestador = request.form['nme_prestador']
    pre.eml_prestador = request.form['eml_prestador']
    pre.sts_prestador = request.form['sts_prestador']
    pre.tel_prestador = request.form['tel_prestador']
    pre.rml_prestador = request.form['rml_prestador']
    pre.pwd_prestador = request.form['pwd_prestador']
    pre.cod_setor = request.form['cod_setor']

    if dao.insert(pre):
        msg = f"Prestador {pre.nme_prestador} inserido com sucesso!"
        css_msg = "sucesso"
    else:
        msg = "Erro ao tentar incluir prestador!"
        css_msg = "erro"

    dao_setor = SetorDAO()
    lst_setores = dao_setor.read_by_filters([('sts_setor', '=', 'A')])
    return render_template('adm/prestador/incluir.html', msg=msg, css_msg=css_msg, lst_setores=lst_setores)


@bp_pre.route('/consultar')  # /adm/prestador/consultar
def consultar():
    dao_setor = SetorDAO()
    setores = dao_setor.read_by_filters([('sts_setor', '=', 'A')])
    return render_template('adm/prestador/consultar.html', prestadores=[], setores=setores, filtro_usado='')


@bp_pre.route('/roda_consultar', methods=['POST'])  # /adm/prestador/roda_consultar
def roda_consultar():
    nme_prestador = request.form['nme_prestador']
    cod_setor = request.form['cod_setor']

    filtros = []
    if nme_prestador:
        filtros.append(('nme_prestador', 'ilike', f'%{nme_prestador}%'))
    if cod_setor:
        filtros.append(('cod_setor', '=', int(cod_setor)))

    filtro_usado = f'Nome: {nme_prestador or "Não informado"} / Setor: {cod_setor or "Todos"}'

    dao = PrestadorDAO()
    prestadores = dao.read_by_filters(filtros)

    dao_setor = SetorDAO()
    setores = dao_setor.read_by_filters([('sts_setor', '=', 'A')])
    return render_template('adm/prestador/consultar.html', prestadores=prestadores, setores=setores,
                           filtro_usado=filtro_usado)


@bp_pre.route('/atualizar')  # /adm/prestador/atualizar
def atualizar():
    dao_setor = SetorDAO()
    setores = dao_setor.read_by_filters([('sts_setor', '=', 'A')])
    return render_template('adm/prestador/atualizar.html', prestadores=[], setores=setores, filtro_usado='')


@bp_pre.route('/roda_atualizar', methods=['POST'])  # /adm/prestador/rodar_atualizar
def roda_atualizar():
    nme_prestador = request.form['nme_prestador']
    cod_setor = request.form['cod_setor']

    filtros = []
    if nme_prestador:
        filtros.append(('nme_prestador', 'ilike', f'%{nme_prestador}%'))
    if cod_setor:
        filtros.append(('cod_setor', '=', int(cod_setor)))

    filtro_usado = f'Nome: {nme_prestador or "Não informado"} / Setor: {cod_setor or "Todos"}'

    dao = PrestadorDAO()
    prestadores = dao.read_by_filters(filtros)

    dao_setor = SetorDAO()
    setores = dao_setor.read_by_filters([('sts_setor', '=', 'A')])
    return render_template('adm/prestador/atualizar.html', prestadores=prestadores, setores=setores,
                           filtro_usado=filtro_usado)


@bp_pre.route('/excluir/<int:idt>')
def excluir(idt):
    dao = PrestadorDAO()
    if dao.delete(idt):
        msg = 'Prestador excluído com sucesso!'
        css_msg = "sucesso"
    else:
        msg = 'Falha ao tentar excluir prestador! Verifique se existe alguma dependência!'
        css_msg = "erro"

    dao_setor = SetorDAO()
    setores = dao_setor.read_by_filters([('sts_setor', '=', 'A')])
    return render_template('adm/prestador/atualizar.html', msg=msg, css_msg=css_msg, prestadores=[], setores=setores,
                           filtro_usado='')


@bp_pre.route('/alterar/<int:idt>')  # /adm/prestador/alterar/número
def alterar(idt):
    dao = PrestadorDAO()
    prestador = dao.read_by_idt(idt)

    dao_setor = SetorDAO()
    lst_setores = dao_setor.read_by_filters([('sts_setor', '=', 'A')])

    return render_template('adm/prestador/alterar.html', msg="", css_msg="", prestador=prestador,
                           lst_setores=lst_setores)


@bp_pre.route('/salva_alterar', methods=['POST'])  # /adm/prestador/salva_alterar
def salva_alterar():
    dao = PrestadorDAO()
    pre = dao.read_by_idt(int(request.form['idt_prestador']))

    pre.mat_prestador = request.form['mat_prestador']
    pre.nme_prestador = request.form['nme_prestador']
    pre.eml_prestador = request.form['eml_prestador']
    pre.sts_prestador = request.form['sts_prestador']
    pre.tel_prestador = request.form['tel_prestador']
    pre.rml_prestador = request.form['rml_prestador']
    pre.cod_setor = request.form['cod_setor']

    # Só altera a senha se uma nova for digitada
    if request.form['pwd_prestador']:
        pre.pwd_prestador = request.form['pwd_prestador']

    if dao.update(pre):
        msg = 'Prestador alterado com sucesso!'
        css_msg = "sucesso"
    else:
        msg = 'Falha ao tentar alterar prestador!'
        css_msg = "erro"

    dao_setor = SetorDAO()
    lst_setores = dao_setor.read_by_filters([('sts_setor', '=', 'A')])
    return render_template('adm/prestador/alterar.html', msg=msg, css_msg=css_msg, prestador=pre,
                           lst_setores=lst_setores)