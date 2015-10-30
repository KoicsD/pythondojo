__author__ = 'KoicsD'


class Digit():

    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


    def __init__(self):
        self.increaser = None
        self.decreaser = None
        self.increaser_order = 0
        self.value = 0
        self.sign = ''

class One(Digit):

    def __init__(self):
        self.increaser = None
        # 1 cannot have any decreaser
        self.increaser_order = 0
        self.value = 1
        self.sign = 'I'

class Five(Digit):

    def __init__(self):
        self.increaser = None
        self.decreaser = None
        self.increaser_order = 0
        self.value = 5
        self.sign = 'V'

class Ten(Digit):

    def __init__(self):
        self.increaser = None
        self.decreaser = None
        self.increaser_order = 0
        self.value = 10
        self.sign = 'X'

class Fifty(Digit):

    def __init__(self):
        self.increaser = None
        self.decreaser = None
        self.increaser_order = 0
        self.value = 50
        self.sign = 'L'

class OneHundred(Digit):

    def __init__(self):
        self.increaser = None
        self.decreaser = None
        self.increaser_order = 0
        self.value = 100
        self.sign = 'C'

class FiveHundred(Digit):

    def __init__(self):
        self.increaser = None
        self.decreaser = None
        self.increaser_order = 0
        self.value = 500
        self.sign = 'D'

class OneThousand(Digit):

    def __init__(self):
        self.increaser = None
        self.decreaser = None
        self.increaser_order = 0
        self.value = 1000
        self.sign = 'M'

values = {'I': One, 'V': Five, 'X': Ten, 'L': Fifty, 'C': OneHundred, 'D': FiveHundred, 'M': OneThousand}

my_obj = values['V']()