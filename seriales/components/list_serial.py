from django_unicorn.components import UnicornView
from seriales.models import Computador

class ListSerialView(UnicornView):
    computadores: list[Computador] = None

    def mount(self):
        self.computadores = Computador.objects.all()
