from time import sleep


class ClassA(object):

    def slow_method(self):
        sleep(3)
        return 'slow_method'

    def result(self):
        return self.slow_method()


def get_result():
    return ClassA().result()
