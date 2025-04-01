from django_unicorn.components import UnicornView
from seriales.models import Computador

class ListSerialView(UnicornView):
    computadores: list[Computador] = None

    def mount(self):
        self.computadores = Computador.objects.all()
    
    def realizados(self):
        self.computadores = Computador.objects.filter(mantenimiento_realizado=True)
    
    def faltantes(self):
        self.computadores = Computador.objects.filter(mantenimiento_realizado=False)
    
    def todos(self):
        self.computadores = Computador.objects.all()
