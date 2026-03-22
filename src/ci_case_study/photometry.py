"""Small photometry helpers used by the case study."""

from __future__ import annotations

from collections.abc import Iterable
from statistics import median


def normalize_flux(fluxes: Iterable[float]) -> list[float]:
    """Normalize a series of flux values by its median."""
    flux_list = [float(value) for value in fluxes]
    if not flux_list:
        raise ValueError("fluxes must not be empty")
    baseline = median(flux_list)
    if baseline == 0:
        raise ValueError("flux median must not be zero")
    return [value / baseline for value in flux_list]


def detect_transit_dip(
    fluxes: Iterable[float],
    threshold: float = 0.98,
    min_points: int = 3,
) -> bool:
    """Return True when a transit-like dip appears for consecutive points."""
    if min_points < 1:
        raise ValueError("min_points must be at least 1")
    consecutive_points = 0
    for value in normalize_flux(fluxes):
        if value <= threshold:
            consecutive_points += 1
            if consecutive_points >= min_points:
                return True
        else:
            consecutive_points = 0
    return False

