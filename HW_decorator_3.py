from HW_decorator_2 import logger


def __init__(self, nested_list):
        self.nested_list = iter(nested_list)
        self.current_list = iter([])

def __iter__(self):
    return self

def __next__(self):
    while True: 
        try:
            return next(self.current_list)
        except StopIteration:
            self.current_list = iter(next(self.nested_list))


@logger(path='flat_iterator.log')
def fg(nested_list):
    return tuple(__iter__(nested_list))


list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

if __name__ == '__main__':
    fg(list_of_lists_1)