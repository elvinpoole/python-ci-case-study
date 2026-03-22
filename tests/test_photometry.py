import pytest

from ci_case_study.photometry import detect_transit_dip, normalize_flux


def test_normalize_flux_scales_values_by_the_median() -> None:
    assert normalize_flux([10.0, 10.0, 20.0]) == [1.0, 1.0, 2.0]


def test_normalize_flux_rejects_empty_input() -> None:
    with pytest.raises(ValueError, match="must not be empty"):
        normalize_flux([])


def test_normalize_flux_rejects_zero_median() -> None:
    with pytest.raises(ValueError, match="must not be zero"):
        normalize_flux([0.0, 0.0, 0.0])


def test_detect_transit_dip_detects_consecutive_low_points() -> None:
    assert detect_transit_dip([1.0, 1.0, 1.0, 0.95, 0.94, 0.95, 1.0], min_points=3)


def test_detect_transit_dip_returns_false_without_enough_consecutive_points() -> None:
    assert not detect_transit_dip([1.0, 0.96, 1.0, 0.95, 0.96], min_points=3)


def test_detect_transit_dip_rejects_invalid_min_points() -> None:
    with pytest.raises(ValueError, match="at least 1"):
        detect_transit_dip([1.0, 0.95], min_points=0)
