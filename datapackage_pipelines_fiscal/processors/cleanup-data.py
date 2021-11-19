import os
import shutil
import logging

from datapackage_pipelines.wrapper import process

def cleanup_data(dp, parameters, *_):
    abs_path = os.path.abspath('data')
    logging.info(f'Cleaning artifact: {abs_path}')

    try:
        shutil.rmtree(abs_path)
    except FileNotFoundError:
        logging.warning(f'No data to delete: {abs_path}')

    return dp

if __name__ == '__main__':
    process(modify_datapackage=cleanup_data)