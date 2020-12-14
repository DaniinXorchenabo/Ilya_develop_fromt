# -*- coding: utf-8 -*-

"""код, который собирает все зависимости, нужные для БД
Именно он применяется для импорта"""
from datetime import date
from datetime import datetime
from datetime import time
from pony.orm import *

from app.settings.config import *
from app.db.models import *
from app.db.db_addition.Group_addition import *
from app.db.db_addition.user_addition import *
from app.db.tests.create_test_db import *
from app.db.db_control_func import *

if __name__ == '__main__':
    from os import chdir

    chdir(HOME_DIR)
    is_DB_created()
    show_all()

    # with db_session:
    #     print(User[105].is_verificated)
    #     print(Group['20ВП1'].get_teachers_data)