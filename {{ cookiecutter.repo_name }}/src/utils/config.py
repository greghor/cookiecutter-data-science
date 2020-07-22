##
import os
##

##PATHS
if os.name == "posix":
    PROJECT_DIR = (
        "/" + os.path.join(*str(os.path.realpath(__file__)).split("/")[:-3]) + "/"
    )
else:  # assume windows
    PROJECT_DIR = "./../../"


SRC_DIR = PROJECT_DIR + "src/"
CODE_ASSETS_DIR = SRC_DIR + "assets/"

DATA_DIR = PROJECT_DIR + "data/"
RAW_DATA_DIR = DATA_DIR + f"raw/"

PROCESSED_DATA_DIR = DATA_DIR + f"processed/"
SAMPLE_DATA_DIR = DATA_DIR + f"sample/"
INTERIM_DIR = DATA_DIR + f"interim/"
ASSETS_DATA_DIR = DATA_DIR + f"assets/"

OUTPUT_DIR = PROJECT_DIR + f"output/"

MODEL_DIR = PROJECT_DIR + f"model/python/"
FIG_DIR = PROJECT_DIR + f"output/results/visuals/figures/"
PRED_DIR = PROJECT_DIR + f"output/results/predict/"
PREDICT_DIR = PROJECT_DIR + f"output/results/predict/"
##

