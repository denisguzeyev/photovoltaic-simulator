import os
import yaml

class BaseConfig(object):
    REPORT_FOLDER = 'report'
    HOST = 'localhost'
    PORT = 5672


class Config(BaseConfig):
     """BasecConfig child where project params can be redefined
    """
     def __init__(self):
        """Init params"""
        locations = ["pvs.yaml"]
        if "CONFIG" in os.environ:
            locations = [os.environ["CONFIG"]]

        for path in locations:
            if not os.path.exists(path):
                continue
            config = yaml.load(open(path), Loader=yaml.FullLoader)

            # Support file alembic config
            config["config_file_name"] = path
            config["version"] = 1

            self.__dict__.update(config)
