"""Starter utilities for the Python CI testing case study."""

from .coordinates import angular_separation_deg, filter_sources_in_cone
from .photometry import detect_transit_dip, normalize_flux

__all__ = [
    "angular_separation_deg",
    "detect_transit_dip",
    "filter_sources_in_cone",
    "normalize_flux",
]

