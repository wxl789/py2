#测试has-a关系，使用组合

class MobilePhone:
    def __init__(self,cpu,screen):
        self.cpu = cpu
        self.screen = screen


class CPU:
    def calculate(self):
        print("算你个12345")
        print("cpu对象：",self)

class Screen:
    def show(self):
        print("显示一个好看的画面，亮瞎你的钛合金大眼")
        print("screen对象：",self)


m = MobilePhone(CPU(),Screen())
m.cpu.calculate()
m.screen.show()