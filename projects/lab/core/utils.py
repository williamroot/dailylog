import logging
import sys
import importlib
from typing import Optional

import streamlit as st


def _reload_module(page):
    logging.debug(
        """--- Reload of module for live reload to work on deeply imported python modules.
    Cf. https://github.com/streamlit/streamlit/issues/366 ---"""
    )
    logging.debug("2. Module: %s", page)
    logging.debug("3. In sys.modules: %s", page in sys.modules)
    try:
        importlib.import_module(page.__name__)
        importlib.reload(page)
    except ImportError as _:
        logging.debug("4. Writing: %s", page)
        logging.debug("5. In sys.modules: %s", page in sys.modules)


def write_page(page):
    page.write()


@st.cache
def set_logging_format(
    logging_formatter: Optional[str] = "%(asctime)s %(name)s: %(message)s"
) -> bool:
    loggers = [
        name
        for name in logging.root.manager.loggerDict
        if name.startswith("streamlit")
    ]
    formatter = logging.Formatter(logging_formatter)
    for name in loggers:
        logger = logging.getLogger(name)
        for handler in logger.handlers:
            handler.setFormatter(formatter)
    return True
