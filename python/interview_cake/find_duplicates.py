# Import the os module, for the os.walk function
import os

# Set the directory you want to start from
# rootDir = '../'
# for dirName, subdirList, files in os.walk(rootDir):
    # print('Found directory: %s' % dirName)
#     for fname in files:
#         print('\t%s' % fname)

# Credit: https://www.pythoncentral.io/how-to-traverse-a-directory-tree-in-python-guide-to-os-walk/

# Testcase:
# [   ('./haha_wedgie.txt', './joshua.txt'),
#     ('./yo_mo.txt', './moses.txt')  ]

# looping through the file system
    # check if current file in dictionary (key: contents, value: file name)
        # add to the dictionary as a key if not and value ['file_name', '']
    # otherwise add file name to value [...,['file_name']]
# create a result list
# check every dictionary key value pair with two file names
    # check metadate on the files and the file created or edited most recently 
        # will be the first item in the tuple
        # the other file will be second
    # add tuple to the result
# return the result

def find_file_duplicates():
    seen = dict()
    # Set the directory you want to start from
    rootDir = './'
    # looping through the file system
    for dirpath, subdirList, filenames in os.walk(rootDir):
        curr_file_contents = ''
        print('Found directory: %s' % dirpath)
        # Code inspiration: https://stackoverflow.com/questions/56528788/how-to-read-text-file-into-one-single-string
        for fname in filenames:
            fname_path = os.path.join(dirpath, fname)
            print('\tFILE:', fname_path)
            with open(fname, 'r') as f:
                # this way of reading the file gives a list of lines
                data_text = f.readlines()
                # create a text out of the file
                curr_file_contents = (' '.join(data_text))
            # check if current file in dictionary (key: contents, value: file name)
            if curr_file_contents in seen:
                seen[curr_file_contents].append(fname_path)
            else: # add new file
                seen[curr_file_contents] = [fname_path]
    # create a result list
    result_list = []
    # check every dictionary key value pair with two file names
    for k, v in seen.items():
        if len(v) == 2:
            # check metadate on the files and the file created (st_ctime) or edited most recently (st_mtime)
            file_1_stat_info = os.stat(v[0])
            file_2_stat_info = os.stat(v[1])
            # the duplicate is the first file
            if file_1_stat_info.st_mtime > file_2_stat_info.st_mtime:
                result_list.append((v[0], v[1]))
            else: # the duplicate is the first file
                result_list.append((v[1], v[0]))
    # return the result
    return result_list
        
    

if __name__ == '__main__':
    print(find_file_duplicates())
