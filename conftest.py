import os
import pytest
from pytest_rabbitmq import factories
from pvs.utils import config
import random
import errno

PROJECT_ROOT = os.path.dirname(__file__)

# Override test config before importing any local modules
os.environ["CONFIG"] = os.path.join(PROJECT_ROOT, "test.yaml")

@pytest.fixture()
def mock_meter(mocker):
    """Mock meter provided values"""
    yield(str(random.randint(0,9000)))


@pytest.fixture()
def mock_erofs_reports(mocker):
    """write_progress_stage error read of file"""
    return mocker.patch("pvs.utils.open", side_effect=OSError(errno.EROFS))
