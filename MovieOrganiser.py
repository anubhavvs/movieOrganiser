import os
import shutil

print('This script will sort your huge Movie Library according to the Year of Release.\n')
print('Just make sure your Movie title has the Year of Release in Parenthesis().\n')
dir = input('Enter the directory where your movies are:\n\n')
print('\nMovie will be organized in the same directory!')

year = []
count = 0

for file_name in os.listdir(dir):
    file_name_list = file_name.split()
    for file_name_word in file_name_list:
        if "(" and ")" in file_name_word:
            year.append(file_name_word[1:5])
            count += 1

set_year = list(set(year))
set_year.sort()
print('\nFolders that will be created:')
print(set_year)

for year in set_year:
    os.mkdir(dir + '\\' + year)

print('\nFolder creation successful!\n')
flag1 = int(input('Enter 1 if folder creation was successful and you want to proceed to moving the files!\n\n'))

flag2 = 0
if flag1 == 1:
    for folders in os.listdir(dir):
        path_ini = dir + '\\' + folders
        for year in set_year:
            if year in path_ini:
                path_fin = dir + '\\' + year
                shutil.move(path_ini, path_fin)
                flag2 = 1

if flag1 == 1 and flag2 == 1:
    print('\nA total of '+str(count)+' movie has been organized successfully!')
else:
    raise FileNotFoundError

