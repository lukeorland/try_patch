#from time import sleep


class ClassA(object):

    def slow_method(self):
        #sleep(3)
        return 'slow_result'


def get_result():
    return ClassA().slow_method()
