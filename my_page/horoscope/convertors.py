from django.urls import converters

class FourDigitConverter:
    regex = "[0-9]{4}"

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return '04%d' % value


class MyFloatConverter:
    regex = "[0-9]+\.[0-9]+"

    def to_python(self, value):
        return float(value)

    def to_url(self, value):
        return str(value)