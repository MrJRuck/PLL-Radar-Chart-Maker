import pytest
import pandas as pd
from project import get_factors, check_exists, get_player


df = pd.read_csv("pll-player-stats.csv")


def test_check_exists():
    assert check_exists("Jeff", "Teat", df)

    with pytest.raises(SystemExit):
        check_exists("Jude", "Ruckart", df)


def test_get_player():
    assert get_player("Jeff", "Teat", df) == "A"


def test_get_factors():
    assert get_factors("A") == ["Points", "Total Goals", "Assists", "Shot Pct", "Turnovers", "Groundballs", "Touches", "Total Passes"]