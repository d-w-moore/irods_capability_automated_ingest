from core import Core

class event_handler(Core):
    
    @staticmethod
    def post_data_obj_create(hdlr_mod, session, target, path, **options):
        print("create", target)

    @staticmethod
    def post_data_obj_modify(hdlr_mod, session, target, path, **options):
        print("modify", target)

    @staticmethod
    def post_coll_create(hdlr_mod, session, target, path, **options):
        print("create coll ", target)

    @staticmethod
    def to_resource_hier(session, target, path, **options):
        return "demoResc"

    @staticmethod
    def as_user(target, path, **options):
        return "tempZone", "rods"



