class GetSetTer(object):
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        print("getter of x called")
        return self._x

    @x.setter
    def x(self, value):
        print("setter of x called")
        self._x = value

    @x.deleter
    def x(self):
        print("deleter of x called")
        del self._x

def to_int(num_str, default_num=0):
    try:
        return int(num_str)
    except:
        return default_num


def to_float(num_str, default_num=0):
    try:
        return float(num_str)
    except:
        return default_num