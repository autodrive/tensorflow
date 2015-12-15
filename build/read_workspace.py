import os

current_dir = os.path.abspath(os.curdir)
tensorflow_root = os.path.abspath(os.pardir)


def main():
    os.chdir(tensorflow_root)

    os.chdir(current_dir)


if '__main__' == __name__:
    main()
