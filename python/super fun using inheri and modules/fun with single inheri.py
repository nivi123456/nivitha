#super function using single inheritance
class computer():
    def __init__(host,system,ram,storage):
        host.system=system
        host.ram=ram
        host.storage=storage
class mobile(computer):
    def __init__(host,system,ram,storage,model):
        super().__init__(system,ram,storage)
        host.model=model
obj_mo=mobile("apple",2,64,"xxx")
print("mobile is:",obj_mo.system)
print("ram memory is:",obj_mo.ram)
print("storage is:",obj_mo.storage)
print("model is:",obj_mo.model)
