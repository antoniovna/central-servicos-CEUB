from database.tipo_ocorrencia_dao import TipoOcorrenciaDAO

def incluir():
    nome = input('Tipo Ocorrencia: ')
    texto = input('Texto Ocorrencia: ')
    dao = TipoOcorrenciaDAO()
    to = dao.new_object()
    to.nme_tipo_ocorrencia = nome
    to.txt_modelo_ocorrencia = texto
    to.tpo_tipo_ocorrencia = 'E'
    to.sts_tipo_ocorrencia = 'A'
    dao.insert(to)
    print(f'Inserido ocorrência número {to.idt_tipo_ocorrencia}')

def listar():
    dao = TipoOcorrenciaDAO()
    lista = dao.read_all()
    for to in lista:
        print(to.idt_tipo_ocorrencia, ' - ', to.nme_tipo_ocorrencia, ' - ',
              to.txt_modelo_ocorrencia)

if __name__ == '__main__':
    while True:
        opc = int(input('''
           1 - Incluir
           2 - Listar
           3 - Sair
           Escolha a Opção? 
        '''))
        if opc == 1:
            incluir()
        elif opc == 2:
            listar()
        else:
            break
