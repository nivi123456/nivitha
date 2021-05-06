#polmorphism with class methods
class india:
    def language(host):
        print("hindi")
    def capital(host):
        print("delhi")
class england:
    def language(host):
        print("english")
    def capital(host):
        print("london")
obj_ind=india()
obj_eng=england()
for country in (obj_ind,obj_eng):
    country.language()
    country.capital()
