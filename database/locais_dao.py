# Classe DAO para a entidade "tb_servico"
from database.model_dao import DAO


class LocaisDAO(DAO):
    def __init__(self):
        super().__init__("tb_local", "idt_local")
