from copy import deepcopy

import pytest

from src.app import activities


@pytest.fixture(autouse=True)
def isolate_activity_data():
    original_activities = deepcopy(activities)
    yield
    activities.clear()
    activities.update(original_activities)