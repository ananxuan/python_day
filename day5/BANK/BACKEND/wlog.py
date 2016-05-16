import logging
import sys
import os
sys.path.append("..")

def wlog(card_id,message):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DB_CARD_ACCOUNT_FILE = r"%s\DB\card_account"%BASE_DIR
    LOGGING_BASE = r"%s\LOG"%BASE_DIR
    DB_XIAOFEI_DIR = r"%s\DB\xiaofei"%BASE_DIR

    logging_file = "%s\%s"%(LOGGING_BASE,card_id)
    logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(message)s',
                    filename=logging_file,
                    filemode='a')
    logging.info(message)
    return True
