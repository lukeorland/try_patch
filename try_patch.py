from time import sleep


class SlowClass(object):

    def slow_method(self):
        sleep(3)
        return 'slow_result'


def get_result():
    return SlowClass().slow_method()
