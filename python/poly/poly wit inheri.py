#polmorphism with inheritance
class bird:
    def intro(host):
        print("these are different birds")
    def flight(host):
        print("most of the birds can fly and some cannot fly")
class parrot(bird):
    def flight(host):
        print("parrots can fly")
class penguin(bird):
    def flight(self):
        print("penguins do not fly")
obj_bi=bird()
obj_pa=parrot()
obj_pen=penguin()

obj_bi.intro()
obj_bi.flight()

obj_pa.intro()
obj_pa.flight()

obj_pen.intro()
obj_pen.flight()
