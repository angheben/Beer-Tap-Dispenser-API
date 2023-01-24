from django.db import models
from stdimage.models import StdImageField

class Beer(models.Model):
    """
    This class represent a beer object
    """
    type = [
        ("Pilsen", "Pilsen"),
        ("Lager", "Lager"),
        ("Ipa", "Ipa"),
        ("Stout", "Stout"),
        ("Weiss", "Weiss"),
        ("Apa", "Apa"),
        ("Pale Ale", "Pale Ale"),
    ]

    status = [
        ("Open", "Open"),
        ("Close", "Close"),
    ]

    name = models.CharField(name='name' ,max_length=100)
    brand = models.CharField(name='brand', max_length=100)
    cost_per_liter = models.DecimalField(name='cost_per_liter', decimal_places=2, max_digits=10)
    flow_volume = models.DecimalField(name='flow_volume', decimal_places=2, max_digits=10)
    type = models.CharField(name="type", choices=type, max_length=100)
    image = StdImageField(name='image', upload_to='beer_pictures', variations={"thumb": {"width": 50, "height": 100,
                                                                                         "crop": True}})
    times_used = models.IntegerField(name='times_used', default=0)
    total_cost = models.DecimalField(name='total_cost', decimal_places=2, default=0, max_digits=100)
    status = models.CharField(name='status', choices=status, max_length=10, default=False)
    def __str__(self):
        return self.name