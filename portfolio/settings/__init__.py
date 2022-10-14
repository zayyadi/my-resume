from .base import *
import os


if os.environ.get("ENV_NAME") == "Prod":
    from .prod import *
else:
    from .dev import *
