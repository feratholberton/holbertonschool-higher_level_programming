#!/usr/bin/env python3
''' Define The Mystical Dragon Mixins '''


class SwimMixin:
    def swim(self):
        print("The creature swims!")

class FlyMixin:
    def fly(self):
        print("The creature flies!")



class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")
