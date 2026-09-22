class Temperature:

    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

temp = Temperature(25)

print("Temperature:", temp.value)
