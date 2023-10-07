from scan_nikto import ScanNikto
import yaml

with open('testdata.yaml', encoding='utf-8') as fy:
    testdata = yaml.safe_load(fy)


def test_scan_injection():
    scan = ScanNikto(testdata['url_base'])
    res = scan.scan_injection()
    assert '0 error(s)' in res
