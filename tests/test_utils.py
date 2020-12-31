import pytest
from pvs.utils import write_report

def test_write_report(mock_erofs_reports):
    with pytest.raises(OSError):
        write_report({'test':1}, 1)
    assert mock_erofs_reports.call_count == 1