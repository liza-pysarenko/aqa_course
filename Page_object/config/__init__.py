import os
from Page_object.config.config import BrowserConfig, APIConfig

path_to_dir = os.path.dirname(__file__)
path_to_config = os.path.join(path_to_dir, 'config.env')

file = os.getenv('ENV_FILE', path_to_config)

browser = BrowserConfig(_env_file=file)
api = APIConfig(_env_file=file)
