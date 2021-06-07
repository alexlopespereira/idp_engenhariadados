import json

from etlelk.etlbase import EtlBase
import datetime
import sqlite3


class EtlPst(EtlBase):

    def __init__(self, config, job_description, limit=100000):
        super().__init__(config, job_description, limit=limit)

    def connect(self):
        try:
            self.connection = sqlite3.connect('test.sqlite3')
            self.connection.row_factory = lambda c, r: dict(zip([col[0] for col in c.description], r))
        except Exception as e:
            print(e)


    def parse_result(self, results):
        for r in results:
            r['date'] = r['date'].split('.')[0]
        return results

    def load_results(self):
        cursor = self.connection.cursor()
        currquery = self.query + f" limit {self.limit} offset {self.offset}"
        ans = None
        try:
            cursor.execute(currquery)
            ans = cursor.fetchall()
        except Exception as e:
            print("Could not select from database: " + e.__str__())
            pass

        if not ans:
            return None
        else:
            ans = self.parse_result(ans)
        return ans

    def create_query(self, from_date=None, date_field=None):
        if from_date:
            from_date_obj = datetime.datetime.strptime(from_date, '%Y-%m-%d %H:%M:%S')
            from_date_offset = from_date_obj - datetime.timedelta(days=2)

            self.query = "SELECT * " \
                         "FROM message m " \
                         f"WHERE m.date >= '{from_date_offset}' " \
                         "ORDER BY m.date ASC "
        else:
            self.query = "SELECT * " \
                         "FROM message m " \
                         "WHERE m.date IS NOT null " \
                         "ORDER BY m.date ASC "
