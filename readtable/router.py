class ChangeRouter(object):
    def db_for_read(self, model, **hints):
        """Send all read operations on Example app models to `example_db`."""
        if model.__name__ == 'User':
            return 'main'
        if model.__name__ == "UserUserattribute":
            return 'main'
        if model.__name__ == "UserApipermissions":
            return 'main'
        return None
