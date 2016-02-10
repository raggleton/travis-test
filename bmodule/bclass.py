"""Another class"""


from amodule.aclass import Adder


class Bass(object):

    def __init__(self, wubiness):
        self.wubiness = wubiness

    def wub(self):
        print 'WUB' * self.wubiness

    def note(self):
        a = Adder()
        return a.add(self.wubiness, 100)
