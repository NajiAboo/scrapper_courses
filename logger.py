import logging
logging.basicConfig(handlers=[logging.FileHandler(filename="logger.log", encoding='utf-8', mode='a+')],format="%(asctime)s %(name)s:%(levelname)s:%(message)s",  datefmt="%F %A %T",  level=logging.INFO)
