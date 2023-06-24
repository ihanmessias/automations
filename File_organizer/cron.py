import os

types = ['png', 'zip']

# -> Directory root
base_path = os.path.expanduser('~')
path = os.path.join(base_path, 'letscode/projects')

cwd = os.chdir(path)

full_list = os.listdir(cwd)

for type_ in types:
    if type_ not in os.listdir():
        os.makedirs(type_)
for file in full_list:
    for type_ in types:
        if '.'+type_ in file:
            old_path = os.path.join(path,file)
            new_path = os.path.join(path,type_,file)
            
            os.replace(old_path, new_path)