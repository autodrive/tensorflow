import os
import re

current_dir = os.path.abspath(os.curdir)
tensorflow_root = os.path.abspath(os.pardir)


def main():
    os.chdir(tensorflow_root)

    workspace_filename = 'WORKSPACE'
    workspace_file = open(workspace_filename, 'r')
    workspace_lines_list = workspace_file.readlines()

    remove_comments(workspace_lines_list)

    os.chdir(current_dir)


def remove_comments(workspace_lines_list, b_verbose=False):
    """
    remove comments from the workspace lines

    :param workspace_lines_list:
    :return:
    """
    if b_verbose: print('len(workspace_lines_list) = %d' % len(workspace_lines_list))

    count_pop = 0
    count_cut = 0
    for i in xrange(len(workspace_lines_list) - 1, -1, -1):
        line = workspace_lines_list[i]
        if line:
            if '#' == line[0]:
                workspace_lines_list.pop(i)
                count_pop += 1
            elif '#' in line:
                j = line.find('#')
                workspace_lines_list[i] = line[:j]
                count_cut += 1

    if b_verbose:
        print('len(workspace_lines_list) = %d' % len(workspace_lines_list))
        print('count pop = %d' % count_pop)
        print('count cut = %d' % count_cut)


if '__main__' == __name__:
    main()
