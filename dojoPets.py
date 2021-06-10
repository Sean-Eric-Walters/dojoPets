from ninja import Ninja
from pet import Pet


Momochi = Pet('Momochi', 'crow','poetry', 100, 100)
Fujibayashi = Ninja('Fujibayashi', 'Nagato', Momochi, 'pine nuts', 'raw meat')


Fujibayashi.walk().feed().bathe()
