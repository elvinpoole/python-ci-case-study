"""Small coordinate helpers used by the case study."""

from __future__ import annotations

import math
from collections.abc import Iterable, Mapping


def angular_separation_deg(ra1: float, dec1: float, ra2: float, dec2: float) -> float:
    """Return the great-circle separation between two sky positions in degrees."""
    ra1_rad = math.radians(ra1)
    dec1_rad = math.radians(dec1)
    ra2_rad = math.radians(ra2)
    dec2_rad = math.radians(dec2)
    cos_sep = (
        math.sin(dec1_rad) * math.sin(dec2_rad)
        + math.cos(dec1_rad) * math.cos(dec2_rad) * math.cos(ra1_rad - ra2_rad)
    )
    return math.degrees(math.acos(max(-1.0, min(1.0, cos_sep))))


def filter_sources_in_cone(
    sources: Iterable[Mapping[str, float | str]],
    center_ra: float,
    center_dec: float,
    radius_deg: float,
) -> list[Mapping[str, float | str]]:
    """Return source mappings that fall inside an inclusive cone search radius."""
    if radius_deg < 0:
        raise ValueError("radius_deg must be non-negative")
    matches: list[Mapping[str, float | str]] = []
    for source in sources:
        source_ra = float(source["ra"])
        source_dec = float(source["dec"])
        separation = angular_separation_deg(center_ra, center_dec, source_ra, source_dec)
        if separation <= radius_deg:
            matches.append(source)
    return matches
