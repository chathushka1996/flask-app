import logging
import logging.handlers


def get_debug_logger(name,file_name):

    _logger = logging.getLogger(name)
    _logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(file_name)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    _logger.addHandler(file_handler)
    return _logger
