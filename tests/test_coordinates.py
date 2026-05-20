import pytest

from ci_case_study.coordinates import angular_separation_deg, filter_sources_in_cone


def test_angular_separation_is_zero_for_identical_positions() -> None:
    assert angular_separation_deg(150.0, 2.0, 150.0, 2.0) == 0.0


def test_angular_separation_matches_one_degree_on_equator() -> None:
    separation = angular_separation_deg(10.0, 0.0, 11.0, 0.0)
    assert separation == pytest.approx(1.0)

def test_filter_sources_at_boundary() -> None:
    source = {"ra":150., "dec":2.0}
    matches = filter_sources_in_cone([source], 151., 2.0, 1.0)
    assert len(matches) == 1
    assert matches[0] == source