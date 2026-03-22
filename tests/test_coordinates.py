import pytest

from ci_case_study.coordinates import angular_separation_deg


def test_angular_separation_is_zero_for_identical_positions() -> None:
    assert angular_separation_deg(150.0, 2.0, 150.0, 2.0) == 0.0


def test_angular_separation_matches_one_degree_on_equator() -> None:
    separation = angular_separation_deg(10.0, 0.0, 11.0, 0.0)
    assert separation == pytest.approx(1.0)
