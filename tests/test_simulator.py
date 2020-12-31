from pvs.simulator import PVReport, PVSimulator

class TestPVReport(object):
    def test_common(self, mock_meter):
        
        pv_report = PVReport(meter_value=int(mock_meter))
        assert pv_report.meter_value == int(mock_meter)
        assert pv_report.result_value == pv_report.pv_value - int(mock_meter)
