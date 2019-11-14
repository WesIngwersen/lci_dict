# lci_dict: Life cycle inventory dictionary module

Provides conversion functions to create standardized Python dictionaries for storing
life cycle inventory data corresponding to the olca-schema. This is a multi-tiered dictionary format with processes at
as the top-tier and process data and metadata elements on successive tiers.
This module is intended to be a more generic build of these LCI dictionaries created
in [ElectricityLCI](https://github.com/usepa/electricitylci)
From the dictionaries, .zip archives of openLCA schema JSON-LD files can be written.

Language: Python 3.x
Dependencies: pandas, olca-ipc (both available via pip install)

## Install with pip:
>pip install git+https://github.com/WesIngwersen/lci_dict.git







