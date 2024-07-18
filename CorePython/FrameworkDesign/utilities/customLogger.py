import logging
import os

log_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Logs', 'automation.log'))


class LogGeneration:
    @staticmethod
    def get_info_log():
        logger = logging.getLogger()
        fhandler = logging.FileHandler(filename=log_file_path, mode='w')
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        fhandler.setFormatter(formatter)
        logger.setLevel(logging.INFO)
        logger.addHandler(fhandler)
        return logger