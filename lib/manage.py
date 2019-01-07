from Jake.lib.models import Message
import Jake.lib.config as config


obj = Message()


def migrate():
    if config.columns:
        print(obj.alter_table())
    else:
        print(obj.create_all())

migrate()