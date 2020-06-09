# flake8: noqa
from sprezzatura.settings_shared import *
from ccnmtlsettings.compose import common

locals().update(
    common(
        project=project,
        base=base,
        STATIC_ROOT=STATIC_ROOT,
        INSTALLED_APPS=INSTALLED_APPS,
    ))

try:
    from sprezzatura.local_settings import *
except ImportError:
    pass
