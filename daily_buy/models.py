from django.db import models

class DailyBuy(models.Model):

    created_on                      = models.DateTimeField(auto_now_add=True)
    name                            = models.CharField(max_length=30)
    varieties                       = (
                                        ('FOOD', 'Food'),
                                        ('SNACKS', 'Snacks'),
                                        ('FOOD STUFF', 'Food stuff'),
                                        ('GROCRIES', 'Grocries'),
                                        ('DRUGS', 'Drugs'),
                                        ('COSMETICS', 'Cosmetics'),
                                        ('OTHERS', 'Others'),
                                    )
    what_to_buy                     = models.CharField(max_length=20, choices=varieties)
    description                     = models.TextField(max_length=500)
    places                          = (
                                        ('CAPTAIN COOK', 'Captain Cook'),
                                        ('COUNTRY KITCHEN', 'Country Kitchen'),
                                        ('ONGBONA', 'Ongbona'),
                                        ('IYA RUKA', 'Iya Ruka'),
                                        ('MAYFAIR MARKET', 'Mayfair market'),
                                        ('SABO MARKET', 'Sabo market'),
                                        ('NEW MARKET', 'New market'),
                                        ('ACE MALL', 'Ace mall'),
                                        ('G2G', 'G2G'),
                                        ('PHAIM PHARMACY', 'Phaim pharmacy')
                                    )
    where_to_buy                    = models.CharField(max_length=20, choices=places)
    delivery_address                = models.CharField(max_length=100)
    phone_number                    = models.CharField(max_length=14)
    

    def __str__(self):
        return self.name
        