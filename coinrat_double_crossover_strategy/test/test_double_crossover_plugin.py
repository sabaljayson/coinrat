import pytest
from flexmock import flexmock

from coinrat_double_crossover_strategy import strategy_plugin
from coinrat_double_crossover_strategy.strategy import DoubleCrossoverStrategy


def test_plugin():
    assert 'coinrat_double_crossover_strategy' == strategy_plugin.get_name()
    assert ['double_crossover'] == strategy_plugin.get_available_strategies()

    strategy_run_mock = flexmock(strategy_configuration={})

    assert isinstance(
        strategy_plugin.get_strategy(
            'double_crossover',
            flexmock(),
            flexmock(),
            flexmock(),
            strategy_run_mock
        ),
        DoubleCrossoverStrategy
    )
    with pytest.raises(ValueError):
        strategy_plugin.get_strategy('gandalf', flexmock(), flexmock(), flexmock(), strategy_run_mock)
