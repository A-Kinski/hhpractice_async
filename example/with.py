from contextlib import contextmanager

@contextmanager
def file_open(path):
    try:
        file_object = open(path, 'w')
        yield file_object
    except OSError:
        print("Error!")
    finally:
        print('Closing file')
        file_object.close()
