from irods_capability_automated_ingest.core import Core
from irods_capability_automated_ingest.utils import Operation

import datetime
def timestamp(): return str(datetime.datetime.now())

class event_handler(Core):

    @staticmethod
    def operation(session, meta, **options):
        return Operation.NO_OP

    @staticmethod
    def setup_job(*x,**kw):
        with open("/tmp/a", "a") as f:
            f.write("SETUP_job {}------\n".format(timestamp()))
            #f.write("\t:arg={}\n\t:kw={}\n------\n".format(x,kw))

    @staticmethod
    def teardown_job(*x,**kw):
        with open("/tmp/a", "a") as f:
            f.write("TEARDOWN_job {}------\n".format(timestamp()))
            #f.write("\t:arg={}\n\t:kw={}\n------\n".format(x,kw))

    @staticmethod
    def pre_job(hdlr_mod, logger, meta):
        with open("/tmp/a", "a") as f:
            f.write("pre_job {}------\n".format(timestamp()))
            #f.write("\t{!r}\n------\n".format(meta))

    @staticmethod
    def post_job(hdlr_mod, logger, meta):
        with open("/tmp/a", "a") as f:
            f.write("post_job {}------\n".format(timestamp()))
            #f.write("\t{!r}\n------\n".format(meta))

