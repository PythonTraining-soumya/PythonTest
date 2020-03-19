import logging


def test_loggingDemo():

    logger = logging.getLogger(__name__)  # will capture the file name at the run time(give 2 underscore infront and
# back of name and give as argument)

    fileHandler = logging.FileHandler('logfile.log')
# if you want to give which format you want to log your output use the code below
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)   # this method will take file handler object as argument
    logger.setLevel(logging.DEBUG)
    logger.debug("Debug statement is executed")
    logger.info("All information we  given is generated")
    logger.warning("Warning message is printed")
    logger.error("error msg is logged")
    logger.critical("Attention needed immediately as it is a critical issue")
