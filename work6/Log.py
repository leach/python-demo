
import logging


















logging.basicConfig(filename="example.log", level=logging.DEBUG,
                    format="%(asctime)s %(message)s %(lineno)s",
                    datefmt="%m/%d/%Y %I:%M:%S %p")
logging.debug("bug")
# logger = logging.getLogger(__name__)