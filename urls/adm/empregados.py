from flask import Blueprint, render_template, request
from database.empregados_dao import EmpregadoDAO
from database.locais_dao import  LocaisDAO
bp_emp = Blueprint('emp', __name__, url_prefix='/admin/empregados')


@bp_emp.route('/incluir')  # /admin/empregados/incluir
def incluir():
    dao_local = LocaisDAO()
    lst_locais = dao_local.read_by_filters([('sts_local', '=', 'A')])
    print("Lista de locias",lst_locais)
    return render_template('adm/empregados/incluir.html', msg="", css_msg="", lst_locais=lst_locais)


@bp_emp.route('/salvar_incluir', methods=['POST'])  # /admin/empregados/salvar_incluir
def salvar_incluir():
    dao = EmpregadoDAO()
    emp = dao.new_object()

    emp.eml_empregado = request.form['eml_empregado']
    emp.mat_empregado = request.form['mat_empregado']
    emp.nme_empregado = request.form['nme_empregado']
    emp.sts_empregado = request.form['sts_empregado']
    emp.tel_empregado = request.form['tel_empregado']
    emp.rml_empregado = request.form['rml_empregado']
    emp.pwd_empregado = request.form['pwd_empregado']
    emp.cod_local = request.form['cod_local']

    if dao.insert(emp):
        msg = f"Empregado {emp.nme_empregado} inserido com sucesso!"
        css_msg = "sucesso"
    else:
        msg = "Erro ao tentar incluir empregado!"
        css_msg = "erro"

    dao_local = LocaisDAO()
    lst_locais = dao_local.read_by_filters([('sts_local', '=', 'A')])

    return render_template('adm/empregados/incluir.html', msg=msg, css_msg=css_msg, lst_locais=lst_locais)


@bp_emp.route('/consultar')  # /admin/empregados/consultar
def consultar():
    dao_local = EmpregadoDAO()
    locais = dao_local.read_by_filters([('sts_local', '=', 'A')])
    return render_template('adm/empregados/consultar.html', empregados=[], locais=locais, filtro_usado='')


@bp_emp.route('/roda_consultar', methods=['POST'])  # /admin/empregados/rodar_consultar
def roda_consultar():
    nme_empregado = request.form['nme_empregado']
    cod_local = request.form['cod_local']

    filtros = []
    if nme_empregado:
        filtros.append(('nme_empregado', 'ilike', f'%{nme_empregado}%'))
    if cod_local:
        filtros.append(('cod_local', '=', int(cod_local)))

    filtro_usado = f'Nome: {nme_empregado or "Não informado"} / Local: {cod_local or "Todos"}'

    dao = EmpregadoDAO()
    empregados = dao.read_by_filters(filtros)

    dao_local = EmpregadoDAO()
    locais = dao_local.read_by_filters([('sts_local', '=', 'A')])

    return render_template('adm/empregados/consultar.html', empregados=empregados, locais=locais,
                           filtro_usado=filtro_usado)


@bp_emp.route('/atualizar')  # /admin/empregados/atualizar
def atualizar():
    dao_local = EmpregadoDAO()
    locais = dao_local.read_by_filters([('sts_local', '=', 'A')])
    return render_template('adm/empregados/atualizar.html', empregados=[], locais=locais, filtro_usado='')


@bp_emp.route('/roda_atualizar', methods=['POST'])  # /admin/empregados/rodar_atualizar
def roda_atualizar():
    nme_empregado = request.form['nme_empregado']
    cod_local = request.form['cod_local']

    filtros = []
    if nme_empregado:
        filtros.append(('nme_empregado', 'ilike', f'%{nme_empregado}%'))
    if cod_local:
        filtros.append(('cod_local', '=', int(cod_local)))

    filtro_usado = f'Nome: {nme_empregado or "Não informado"} / Local: {cod_local or "Todos"}'

    dao = EmpregadoDAO()
    empregados = dao.read_by_filters(filtros)

    dao_local = EmpregadoDAO()
    locais = dao_local.read_by_filters([('sts_local', '=', 'A')])

    return render_template('adm/empregados/atualizar.html', empregados=empregados, locais=locais,
                           filtro_usado=filtro_usado)


@bp_emp.route('/excluir/<int:idt>')
def excluir(idt):
    dao = EmpregadoDAO()

    if dao.delete(idt):
        msg = 'Empregado excluído com sucesso!'
        css_msg = "sucesso"
    else:
        msg = 'Falha ao excluir! Verifique dependências!'
        css_msg = "erro"

    return render_template('adm/empregados/atualizar.html', msg=msg, css_msg=css_msg, locais=[], filtro_usado='')
