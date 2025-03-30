from django_unicorn.components import UnicornView
from seriales.models import Computador
from seriales.forms import ComputadorForm

class CreateSerialView(UnicornView):    
    
    serial = None
    form_class = ComputadorForm

    def create(self):
        if not self.is_valid():
            return
        
        Computador.objects.create(
            serial = self.serial
        )
        self.serial = ''

    def mount(self):
        self.seriales = Computador.objects.all()