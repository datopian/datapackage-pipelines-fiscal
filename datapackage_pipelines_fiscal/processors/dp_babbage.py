import os
import shutil
import logging
import json
from os.path import dirname, basename
from datapackage_pipelines.wrapper import process

def copy_babbage(dp, parameters, *_):
    
    abs_path = os.path.abspath("normalized")
    logging.info(f'Obtaining Babbage model from: {abs_path}')

    dpkg_path  = f'{abs_path}/final/datapackage.json'
    dpkg = json.load(open(dpkg_path,"r"))['babbageModel']

    org_path = dirname(dirname(os.getcwd()))
    model_name = basename(os.getcwd())

    model_path = f'{org_path}/models/{model_name}.json'

    with open(model_path, "w") as outfile:
        json.dump(dpkg, outfile)

    return dp

if __name__ == '__main__':
    process(modify_datapackage=copy_babbage)