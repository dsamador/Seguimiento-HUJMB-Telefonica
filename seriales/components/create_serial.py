from django_unicorn.components import UnicornView
from seriales.models import Computador

class CreateSerialView(UnicornView):
    state: str = "Add"
    seriales: list[Computador]

    def mount(self):
        self.seriales = Computador.objects.all()