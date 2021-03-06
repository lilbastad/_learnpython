# -*- coding: utf-8 -*-
"""
sqlite_tutorial_06.py

This is code from online "SQLite Python tutorial": http://zetcode.com/db/sqlitepythontutorial/

@author Tset Noitamotua (tset.no@gmail.com)
@version 2017-05-05
"""

import sqlite3 as lite
import sys



# Connection to SQLite3 DB in memory
conm = lite.connect(':memory:')


def main():

    with conm:
        cur = conm.cursor()
        cur.execute("CREATE TABLE Friends(Id INTEGER PRIMARY KEY, Name TEXT);")
        cur.execute("INSERT INTO Friends(Name) VALUES ('Tom');")
        cur.execute("INSERT INTO Friends(Name) VALUES ('Rebecca');")
        cur.execute("INSERT INTO Friends(Name) VALUES ('Jim');")
        cur.execute("INSERT INTO Friends(Name) VALUES ('Robert');")

        last_id = cur.lastrowid
        print("The last id of the inserted row is %d" % last_id)


if __name__ == '__main__':
    main()
