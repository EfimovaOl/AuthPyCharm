import logging
import subprocess


class ScanNikto:

    def __init__(self, url_base):
        self.url_base = url_base

    def scan_tuning(self, type_tuning):
        try:
            logging.debug(f'sent safety scan "Nikto": Tuning {type_tuning}...')
            cmd = f'nikto -h {self.url_base}/ -ssl -Tuning {type_tuning}'
            res = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
            if not res.stdout or res.returncode != 0:
                logging.error('error safety')
                return None
        except:
            logging.exception(f'exception safety scan "Nikto": Tuning {type_tuning}')

        return res.stdout

    def scan_injection(self):
        return self.scan_tuning(4)