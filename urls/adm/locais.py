from flask import Blueprint, render_template, request
from database.locais_dao import LocaisDAO
from database.setor_dao import SetorDAO

bp_loc = Blueprint('loc', __name__, url_prefix='/admin/locais')


@bp_loc.route('/incluir')  # /admin/locais/incluir
def incluir():
    dao_setor = SetorDAO()
    lst_setores = dao_setor.read_by_filters([('sts_setor', '=', 'A')])
    print(lst_setores)
    return render_template('adm/locais/incluir.html', msg="", css_msg="", lst_setores=lst_setores)


@bp_loc.route('/salvar_incluir', methods=['POST'])  # /admin/locais/salvar_incluir
def salvar_incluir():
    dao = LocaisDAO()
    loc = dao.new_object()

    loc.nme_local = request.form['nme_local']
    loc.lat_local = request.form['lat_local']  # Atenção: Pode precisar de conversão para Decimal
    loc.lgt_local = request.form['lgt_local']  # Atenção: Pode precisar de conversão para Decimal
    loc.sts_local = request.form['sts_local']
    loc.cod_setor = request.form['cod_setor']  # Atenção: Pode precisar de conversão para int

    if dao.insert(loc):
        msg = f"Local {loc.nme_local} inserido com sucesso!"
        css_msg = "sucesso"
    else:
        msg = "Erro ao tentar incluir local!"
        css_msg = "erro"

    dao_setor = SetorDAO()
    lst_setores = dao_setor.read_by_filters([('sts_setor', '=', 'A')])

    return render_template('adm/locais/incluir.html', msg=msg, css_msg=css_msg, lst_setores=lst_setores)


@bp_loc.route('/consultar')  # /admin/locais/consultar
def consultar():
    dao_setor = SetorDAO()
    setores = dao_setor.read_by_filters([('sts_setor', '=', 'A')])
    return render_template('adm/locais/consultar.html', locais=[], setores=setores, filtro_usado='')


@bp_loc.route('/roda_consultar', methods=['POST'])  # /admin/locais/rodar_consultar
def roda_consultar():
    nme_local = request.form['nme_local']
    cod_setor = request.form['cod_setor']

    filtros = []
    if nme_local:
        filtros.append(('nme_local', 'ilike', f'%{nme_local}%'))
    if cod_setor:
        filtros.append(('cod_setor', '=', int(cod_setor)))

    filtro_usado = f'Nome: {nme_local or "Não informado"} / Setor: {cod_setor or "Todos"}'

    dao = LocaisDAO()
    locais = dao.read_by_filters(filtros)

    dao_setor = SetorDAO()
    setores = dao_setor.read_by_filters([('sts_setor', '=', 'A')])

    return render_template('adm/locais/consultar.html', locais=locais, setores=setores,
                           filtro_usado=filtro_usado)


@bp_loc.route('/atualizar')  # /admin/locais/atualizar
def atualizar():
    dao_setor = SetorDAO()
    setores = dao_setor.read_by_filters([('sts_setor', '=', 'A')])
    return render_template('adm/locais/atualizar.html', locais=[], setores=setores, filtro_usado='')


@bp_loc.route('/roda_atualizar', methods=['POST'])  # /admin/locais/rodar_atualizar
def roda_atualizar():
    nme_local = request.form['nme_local']
    cod_setor = request.form['cod_setor']

    filtros = []
    if nme_local:
        filtros.append(('nme_local', 'ilike', f'%{nme_local}%'))
    if cod_setor:
        filtros.append(('cod_setor', '=', int(cod_setor)))

    filtro_usado = f'Nome: {nme_local or "Não informado"} / Setor: {cod_setor or "Todos"}'

    dao = LocaisDAO()
    locais = dao.read_by_filters(filtros)

    dao_setor = SetorDAO()
    setores = dao_setor.read_by_filters([('sts_setor', '=', 'A')])

    return render_template('adm/locais/atualizar.html', locais=locais, setores=setores,
                           filtro_usado=filtro_usado)


@bp_loc.route('/excluir/<int:idt>')  # /admin/locais/excluir/<idt>
def excluir(idt):
    dao = LocaisDAO()

    if dao.delete(idt):
        msg = 'Local excluído com sucesso!'
        css_msg = "sucesso"
    else:
        msg = 'Falha ao excluir! Verifique dependências!'
        css_msg = "erro"

    return render_template('adm/locais/atualizar.html', msg=msg, css_msg=css_msg, locais=[], setores=[], filtro_usado='')