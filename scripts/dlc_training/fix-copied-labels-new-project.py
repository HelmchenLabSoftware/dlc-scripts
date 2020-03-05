import yaml

# Append base directory
projectPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(projectPath)

from lib.qt_wrapper import gui_fname, gui_fnames, gui_fpath
from lib.os_lib import getfiles_walk

# Get config file
pwd_config_file = gui_fname("Open config file", "./", "YAML (*.yaml)")

# Get all marked CSV files from labeled data, get containing folders
# Create dummy video file names with same names as the folders
pwd_data = os.path.join(os.path.dirname(pwd_config_file), "labeled-data")
paths_csv = [os.path.join(path, name) for path, name in getfiles_walk(pwd_data, [".csv"])]
video_names = [os.path.basename(os.path.dirname(path)) + ".avi" for path in paths_csv]
video_names = sorted(list(set(video_names)))

# Store resulting video files in the config file
with open(pwd_config_file, "r") as fconf:
    data_conf = yaml.load(fconf)

video_sets_old = data_conf.pop('video_sets')
data_conf['video_sets'] = {vidname : {'crop' : [0, 1000, 0, 734]} for vidname in video_names}

with open(pwd_config_file, 'w') as fconf_new:
    yaml.dump(data_conf, fconf_new, default_flow_style=False)