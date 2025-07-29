"""
This file is part of CLIMADA.

Copyright (C) 2017 ETH Zurich, CLIMADA contributors listed in AUTHORS.

CLIMADA is free software: you can redistribute it and/or modify it under the
terms of the GNU General Public License as published by the Free
Software Foundation, version 3.

CLIMADA is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with CLIMADA. If not, see <https://www.gnu.org/licenses/>.

---

climada init
"""

from pathlib import Path
from shutil import copyfile

from .util.config import CONFIG  # noqa: F401
from .util.constants import *

GSDP_DIR = SYSTEM_DIR.joinpath("GSDP")  # noqa: F405

REPO_DATA = {
    "climada/data/system": [
        ISIMIP_GPWV3_NATID_150AS,  # noqa: F405
        GLB_CENTROIDS_MAT,  # noqa: F405
        ENT_TEMPLATE_XLS,  # noqa: F405
        HAZ_TEMPLATE_XLS,  # noqa: F405
        RIVER_FLOOD_REGIONS_CSV,  # noqa: F405
        NATEARTH_CENTROIDS[150],  # noqa: F405
        NATEARTH_CENTROIDS[360],  # noqa: F405
        SYSTEM_DIR.joinpath("WEALTH2GDP_factors_CRI_2016.csv"),  # noqa: F405
        SYSTEM_DIR.joinpath("GDP_TWN_IMF_WEO_data.csv"),  # noqa: F405
        SYSTEM_DIR.joinpath("FAOSTAT_data_country_codes.csv"),  # noqa: F405
        SYSTEM_DIR.joinpath("rcp_db.xls"),  # noqa: F405
        SYSTEM_DIR.joinpath("tc_impf_cal_v01_TDR1.0.csv"),  # noqa: F405
        SYSTEM_DIR.joinpath("tc_impf_cal_v01_EDR.csv"),  # noqa: F405
        SYSTEM_DIR.joinpath("tc_impf_cal_v01_RMSF.csv"),  # noqa: F405
    ],
    "climada/data/system/GSDP": [
        GSDP_DIR.joinpath(f"{cc}_GSDP.xls")
        for cc in [
            "AUS",
            "BRA",
            "CAN",
            "CHE",
            "CHN",
            "DEU",
            "FRA",
            "IDN",
            "IND",
            "JPN",
            "MEX",
            "TUR",
            "USA",
            "ZAF",
        ]
    ],
    "climada/data/demo": [
        ENT_DEMO_TODAY,  # noqa: F405
        ENT_DEMO_FUTURE,  # noqa: F405
        EXP_DEMO_H5,  # noqa: F405
        HAZ_DEMO_FL,  # noqa: F405
        HAZ_DEMO_MAT,  # noqa: F405
        HAZ_DEMO_H5,  # noqa: F405
        TC_ANDREW_FL,  # noqa: F405
        DEMO_DIR.joinpath("demo_emdat_impact_data_2020.csv"),  # noqa: F405
        # noqa: F405DEMO_DIR.joinpath("nl_rails.gpkg"), # noqa: F405
    ]
    + WS_DEMO_NC,  # noqa: F405
}


def test_installation():
    """Run this function to check whether climada is working properly.
    If the invoked tests pass and an OK is printed out, the installation was successfull.
    """
    from unittest import TestLoader, TextTestRunner

    suite = TestLoader().discover(
        start_dir="climada.engine.test", pattern="test_cost_benefit.py"
    )
    suite.addTest(
        TestLoader().discover(start_dir="climada.engine.test", pattern="test_impact.py")
    )
    TextTestRunner(verbosity=2).run(suite)


def setup_climada_data(reload=False):
    """This function is called when climada is imported.
    It creates a climada directory by default in the home directory.
    Other locations can be configured in the climada.conf file.
    The directory is filled with data files from the repository and is also the default target
    directory for files downloaded from climada.ethz.ch via the data api.

    Parameters
    ----------
    reload : bool, optional
        in case system or demo data have changed in the github repository, the local copies of
        these files can be updated by setting reload to True,
        by default False
    """
    for dirpath in [DEMO_DIR, SYSTEM_DIR, GSDP_DIR]:  # noqa: F405
        dirpath.mkdir(parents=True, exist_ok=True)

    for src_dir, path_list in REPO_DATA.items():
        for path in path_list:
            if not path.exists() or reload:
                src = Path(__file__).parent.parent.joinpath(src_dir, path.name)
                copyfile(src, path)


setup_climada_data()
