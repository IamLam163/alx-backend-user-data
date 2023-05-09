#!/usr/bin/env python3
"""MAIn FIle"""
from user import User

print(User.__tablename__)

for column in User.__table__.columns:
    print("{}: {}".format(column, column.type))
