"""Information about this library."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("streamlit-pydantic")
except PackageNotFoundError:
    __version__ = "0.0.0-local"

