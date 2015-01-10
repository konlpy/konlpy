import sys
import warnings

from ._hannanum import Hannanum
from ._kkma import Kkma
if sys.version_info[0] < 3:
    warnings.filterwarnings("once")
    warnings.warn("Your system does not support KOMORAN", ImportWarning)
else:
    from ._komoran import Komoran
try:
    from ._mecab import Mecab
except ImportError:
    pass
