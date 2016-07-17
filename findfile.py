import os


def search_file(search, directory):
    file_list = []
    for i in os.walk(directory):
        for j in i[2]:
            if search in j:
                file_list.append(j)
                continue
            f = open(i[0] + '/' + j)
            data = f.read()
            if search in data:
                file_list.append(j)
    return file_list


search = raw_input('Please enter the key word you are searching for.\n')
directory = raw_input('Please enter the directory in which you would like to search.\n')
print search_file(search, directory)
