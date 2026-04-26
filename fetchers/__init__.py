"""
公司新聞爬蟲
"""

from .base import CompanyFetcher, CompanyDocument

from .agc import AgcFetcher
from .au_optronics import AuOptronicsFetcher
from .corning import CorningFetcher
from .first_solar import FirstSolarFetcher
from .flat_glass import FlatGlassFetcher
from .fuyao import FuyaoFetcher
from .innolux import InnoluxFetcher
from .longi import LongiFetcher
from .nsg import NsgFetcher
from .oi_glass import OiGlassFetcher
from .owens_corning import OwensCorningFetcher
from .saint_gobain import SaintGobainFetcher
from .sibelco import SibelcoFetcher
from .solvay import SolvayFetcher
from .taiwan_glass import TaiwanGlassFetcher
from .tata_chemicals import TataChemicalsFetcher
from .xinyi_glass import XinyiGlassFetcher
from .xinyi_solar import XinyiSolarFetcher

FETCHERS = {
    "agc": AgcFetcher,
    "au_optronics": AuOptronicsFetcher,
    "corning": CorningFetcher,
    "first_solar": FirstSolarFetcher,
    "flat_glass": FlatGlassFetcher,
    "fuyao": FuyaoFetcher,
    "innolux": InnoluxFetcher,
    "longi": LongiFetcher,
    "nsg": NsgFetcher,
    "oi_glass": OiGlassFetcher,
    "owens_corning": OwensCorningFetcher,
    "saint_gobain": SaintGobainFetcher,
    "sibelco": SibelcoFetcher,
    "solvay": SolvayFetcher,
    "taiwan_glass": TaiwanGlassFetcher,
    "tata_chemicals": TataChemicalsFetcher,
    "xinyi_glass": XinyiGlassFetcher,
    "xinyi_solar": XinyiSolarFetcher,
}
