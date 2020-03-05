'''
  The purpose of this code is to adjust all paths in the training dataset.
  Only necessary if initial training phase was done on windows.

  The code replaces any windows-like backslashes to linux forwards slashes in
  * config.yaml
  * all .csv labeling files
  * all .h5 labeling files
'''

#import numpy as np
import os, sys
import yaml
#import h5py
import pandas as pd

projectPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(projectPath)

from lib.qt_wrapper import gui_fname
from lib.os_lib import getfiles_walk


pwd_config_file = gui_fname("Select config file...", "./", "Config Files (*.yaml)")
pwd_project = os.path.dirname(pwd_config_file)

pwd_project     = os.path.abspath(pwd_project)
pwd_config_file = os.path.abspath(pwd_config_file)

print("Absolute path to config file is: ", pwd_config_file)

##################################
#  Editing config.yaml file
##################################
print('Editing config.yaml file')
with open(pwd_config_file, "r") as fconf:
  data_conf = yaml.load(fconf)

# Fix project path
project_path_old = data_conf['project_path']
data_conf['project_path'] = pwd_project

# Fix all paths to videos
video_sets_old = data_conf.pop('video_sets')
data_conf['video_sets'] = {}
for k,v in video_sets_old.items():
  k_new = k.replace('\\','/')
  idxVideos = k_new.find("videos/")
  k_new = os.path.join(data_conf['project_path'], k_new[idxVideos:])
  #k_new = k.replace(project_path_old, data_conf['project_path']).replace('\\','/')
  data_conf['video_sets'][k_new] = v

# Save changes
with open(pwd_config_file, 'w') as fconf_new:
  yaml.dump(data_conf, fconf_new, default_flow_style=False)

##################################
#  Editing csv paths
##################################
print('Editing paths in .csv marking files')
pwd_labeled = os.path.join(pwd_project, 'labeled-data')
filewalk_csv = getfiles_walk(pwd_labeled, ['.csv'])
filepaths_csv = [os.path.join(path, name) for path, name in filewalk_csv]

for csv_fname in filepaths_csv:
    print("Fixing file", csv_fname)

    with open(csv_fname, 'r') as csvfile:
        data_csv = csvfile.readlines()

    data_csv = [line.strip().split(',') for line in data_csv]
    data_csv = [[line[0].replace('\\', '/')] + line[1:] for line in data_csv]

    with open(csv_fname, 'w') as csvfile:
        for line in data_csv:
            csvfile.write(",".join(line) + '\n')

##################################
#  Marking h5 paths
##################################
print('Editing paths in .h5 marking files')
filewalk_h5 = getfiles_walk(pwd_labeled, ['.h5', "CollectedData"])
filepaths_h5 = [os.path.join(path, name) for path, name in filewalk_h5]

for h5_fname in filepaths_h5:
    print("Fixing file", h5_fname)

    h5_df = pd.read_hdf(h5_fname, 'df_with_missing')

    # Rename all indices
    h5_df.index = pd.Index([idx.replace('\\', '/') for idx in h5_df.index])

    print(h5_df.index)


    #print(h5_df.keys())
    #for key in h5_df.keys():
        #for keyname in list(h5_df[key].keys()):
            #newkeyname = keyname.replace('\\', '/')

            ## Add transformed keys
            #h5_df[key][newkeyname] = h5_df[key][keyname]

            ## Delete old keys
            #del h5_df[key][keyname]

    #for key in h5_df.keys():
        #print(h5_df[key])

    # Save edited dataframe back
    h5_df.to_hdf(h5_fname, 'df_with_missing', format='table', mode='w')



        #print(h5_df[key].keys())
        #for key2 in h5_df[key].keys():
            #print(key2)
    #print(h5_df.values())

    #h5_df.to_hdf(h5_fname, 'df_with_missing', format='table', mode='w')

    #h5f = h5py.File(h5_fname, 'r+')
    #sub = h5f['df_with_missing']
    #table = sub['table'][...]
    ##del h5f['df_with_missing/table']

    #for i in range(len(table)):
        #table[i][0] = table[i][0].decode('UTF-8').replace('\\', '/').encode()
        #print(table[i][0])

    #sub['table'][...] = table
    #h5f.close()

        
