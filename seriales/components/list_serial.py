from django_unicorn.components import UnicornView
from seriales.models import Computador

class ListSerialView(UnicornView):
    computadores: list[Computador] = None
    query = ""
    resultados = []
    realizados_count = 0
    faltantes_count = 0
    total_count = 0


    def mount(self):
        self.computadores = Computador.objects.all()
        self.actualizar_contadores()
    
    def actualizar_contadores(self):
        """Consulta y actualiza los contadores de computadores según su estado."""
        self.realizados_count = Computador.objects.filter(mantenimiento_realizado=True).count()
        self.faltantes_count = Computador.objects.filter(mantenimiento_realizado=False).count()
        self.total_count = Computador.objects.count()
    
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
