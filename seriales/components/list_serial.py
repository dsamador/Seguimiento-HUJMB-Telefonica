from django_unicorn.components import UnicornView
from seriales.models import Computador

class ListSerialView(UnicornView):
    computadores: list[Computador] = None
    query = ""
    resultados = []

    def mount(self):
        self.computadores = Computador.objects.all()
    
    def realizados(self):
        self.computadores = Computador.objects.filter(mantenimiento_realizado=True)
    
    def faltantes(self):
        self.computadores = Computador.objects.filter(mantenimiento_realizado=False)
    
    def todos(self):
        self.computadores = Computador.objects.all()

    def buscar(self):
        if self.query:
            letras = list(self.query)# Separa las letras
            self.computadores = Computador.objects.filter(
                serial__icontains=self.query  # Filtra si contiene la cadena
            )
            
            # Filtra los seriales que contengan todas las letras en cualquier orden
            self.computadores = [
                c for c in self.computadores if all(letra in c.serial for letra in letras)
            ]
        else:
            self.computadores = Computador.objects.all()
