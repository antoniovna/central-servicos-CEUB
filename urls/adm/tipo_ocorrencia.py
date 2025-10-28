from flask import Blueprint, render_template, request
from database.tipo_ocorrencia_dao import TipoOcorrenciaDAO

bp_oco = Blueprint('oco', __name__, url_prefix='/admin/ocorrencias/tipos')


@bp_oco.route('/incluir')
def incluir():
    return render_template('adm/ocorrencias/tipos/incluir.html', msg="", css_msg="")


@bp_oco.route('/salvar_incluir', methods=['POST'])
def salvar_incluir():
    dao = TipoOcorrenciaDAO()
    oco = dao.new_object()

    oco.nme_tipo_ocorrencia = request.form['nme_tipo_ocorrencia']
    oco.tpo_tipo_ocorrencia = request.form['tpo_tipo_ocorrencia']
    oco.sts_tipo_ocorrencia = request.form['sts_tipo_ocorrencia']
    oco.txt_modelo_ocorrencia = request.form['txt_modelo_ocorrencia']

    if dao.insert(oco):
        msg = f"Tipo de Ocorrência {oco.nme_tipo_ocorrencia} inserido com sucesso!"
        css_msg = "sucesso"
    else:
        msg = "Erro ao tentar incluir Tipo de Ocorrência!"
        css_msg = "erro"

    return render_template('adm/ocorrencias/tipos/incluir.html', msg=msg, css_msg=css_msg)


@bp_oco.route('/consultar')
def consultar():
    return render_template('adm/ocorrencias/tipos/consultar.html', tipos_ocorrencia=[], filtro_usado='')


@bp_oco.route('/roda_consultar', methods=['POST'])
def roda_consultar():
    nme_tipo_ocorrencia = request.form['nme_tipo_ocorrencia']
    tpo_tipo_ocorrencia = request.form['tpo_tipo_ocorrencia']

    filtros = []
    if nme_tipo_ocorrencia:
        filtros.append(('nme_tipo_ocorrencia', 'ilike', f'%{nme_tipo_ocorrencia}%'))
    if tpo_tipo_ocorrencia:
        filtros.append(('tpo_tipo_ocorrencia', '=', tpo_tipo_ocorrencia))

    filtro_usado = f'Nome: {nme_tipo_ocorrencia or "Não informado"} / Tipo: {tpo_tipo_ocorrencia or "Todos"}'

    dao = TipoOcorrenciaDAO()
    tipos_ocorrencia = dao.read_by_filters(filtros)

    return render_template('adm/ocorrencias/tipos/consultar.html', tipos_ocorrencia=tipos_ocorrencia,
                           filtro_usado=filtro_usado)


@bp_oco.route('/atualizar')
def atualizar():
    return render_template('adm/ocorrencias/tipos/atualizar.html', tipos_ocorrencia=[], filtro_usado='')


@bp_oco.route('/roda_atualizar', methods=['POST'])
def roda_atualizar():
    nme_tipo_ocorrencia = request.form['nme_tipo_ocorrencia']
    tpo_tipo_ocorrencia = request.form['tpo_tipo_ocorrencia']

    filtros = []
    if nme_tipo_ocorrencia:
        filtros.append(('nme_tipo_ocorrencia', 'ilike', f'%{nme_tipo_ocorrencia}%'))
    if tpo_tipo_ocorrencia:
        filtros.append(('tpo_tipo_ocorrencia', '=', tpo_tipo_ocorrencia))

    filtro_usado = f'Nome: {nme_tipo_ocorrencia or "Não informado"} / Tipo: {tpo_tipo_ocorrencia or "Todos"}'

    dao = TipoOcorrenciaDAO()
    tipos_ocorrencia = dao.read_by_filters(filtros)

    return render_template('adm/ocorrencias/tipos/atualizar.html', tipos_ocorrencia=tipos_ocorrencia,
                           filtro_usado=filtro_usado)


@bp_oco.route('/excluir/<int:idt>')
def excluir(idt):
    dao = TipoOcorrenciaDAO()

    if dao.delete(idt):
        msg = 'Tipo de Ocorrência excluído com sucesso!'
        css_msg = "sucesso"
    else:
        msg = 'Falha ao excluir! Verifique dependências!'
        css_msg = "erro"

    return render_template('adm/ocorrencias/tipos/atualizar.html', msg=msg, css_msg=css_msg, tipos_ocorrencia=[], filtro_usado='')


@bp_oco.route('/alterar/<int:idt>')
def alterar(idt):
    dao = TipoOcorrenciaDAO()
    oco = dao.read_by_idt(idt)
    return render_template('adm/ocorrencias/tipos/alterar.html', msg="", css_msg="", oco=oco)


@bp_oco.route('/salvar_alterar', methods=['POST'])
def salvar_alterar():
    dao = TipoOcorrenciaDAO()
    oco = dao.read_by_idt(int(request.form['idt_tipo_ocorrencia']))

    oco.nme_tipo_ocorrencia = request.form['nme_tipo_ocorrencia']
    oco.tpo_tipo_ocorrencia = request.form['tpo_tipo_ocorrencia']
    oco.sts_tipo_ocorrencia = request.form['sts_tipo_ocorrencia']
    oco.txt_modelo_ocorrencia = request.form['txt_modelo_ocorrencia']

    if dao.update(oco):
        msg = 'Tipo de Ocorrência alterado com sucesso!'
        css_msg = "sucesso"
    else:
        msg = 'Falha ao tentar alterar Tipo de Ocorrência!'
        css_msg = "erro"

    return render_template('adm/ocorrencias/tipos/alterar.html', msg=msg, css_msg=css_msg, oco=oco)