# -*- coding: utf-8 -*-
import os
from datetime import datetime, timedelta


class Utilities:

    @staticmethod
    def remove_doc(path_dir: str, file: str = '') -> bool:
        try:
            if (file != ''):
                os.remove(path_dir)
                return True
            else:
                list_dir = os.listdir(path_dir)
                for file in list_dir:
                    os.remove(os.path.join(path_dir, file))
                return True
        except Exception:
            return False

    @staticmethod
    def get_current_day() -> datetime:
        return datetime.now()

    @staticmethod
    def get_previous_day(previous_days) -> datetime:
        return Utilities.get_current_day() - timedelta(days=previous_days)
