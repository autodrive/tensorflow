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
    text = ''.join(workspace_lines_list).strip()

    result = get_workspace_entries(text)

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


def get_workspace_entries(text):
    """
    convert workspace text into list of entries
    entry example : ['new_http_archive', {
          'name': "gmock_archive",
          'url': "https://googlemock.googlecode.com/files/gmock-1.7.0.zip",
          'sha256': "26fcbb5925b74ad5fc8c26b0495dfc96353f4d553492eb97e85a8a6d2f43095b",
          'build_file': "google/protobuf/gmock.BUILD",
    }]

    :param text:
    :return result: list of entries
    """

    result = []
    state = 'before'
    for c in text:
        if 'before' == state:
            if c.strip():
                state = 'entry_found'
                entry_name = c
        elif 'entry_found' == state:
            if c.strip():
                if '(' != c:
                    entry_name += c
                else:
                    entry = [entry_name,{}]
                    state = 'dictionary_key'
                    key_name = ''
        elif 'dictionary_key' == state:
            if c.strip():
                if '=' == c:
                    key_name = key_name.strip()
                    state = 'dictionary_value'
                    value = ''
                elif ')' == c:
                    result.append(entry)
                    entry = []
                    state = 'before'
                else:
                    key_name += c

        elif 'dictionary_value' == state:
            if c.strip():
                if ')' == c:
                    result.append(entry)
                    entry = []
                    state = 'before'
                elif ',' != c:
                    value += c
                else:
                    entry[1][key_name] = value
                    state = 'dictionary_key'
                    key_name = ''

    return result


if '__main__' == __name__:
    main()
