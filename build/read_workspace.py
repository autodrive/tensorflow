import os

current_dir = os.path.abspath(os.curdir)
tensorflow_root = os.path.abspath(os.pardir)


def main():
    os.chdir(tensorflow_root)

    workspace_filename = 'WORKSPACE'
    workspace_file = open(workspace_file, 'r')
    workspace_txt = workspace_file.read()

    os.chdir(current_dir)


if '__main__' == __name__:
    main()
