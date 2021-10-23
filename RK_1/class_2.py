"""
класс_2
"""
class Book_shop:

    def __init__(self,id_sop,name):
        self.id_shop = id_sop
        self.name = name


    def __repr__(self):
        return "Оркест {} имеет номер {}".format(self.name,self.num_orch)
