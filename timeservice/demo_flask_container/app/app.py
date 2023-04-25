from datetime import datetime, timedelta
from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


class UTCTime(Resource):

    def get(self, us_time):
        # Default to 200 OK
        # note: us_time variable is assumed based on US timezone(constant)
        working_hours = 9 # total number of hours in working time.
        hours_to_work = 15 # hours difference between US and Israel.  Based on US 8am working time.
        try:
            ts = int(us_time)
            # assuming that the us_time variable is based on US time. time difference between israel
            # and US is +7, hence +7(hours)
            ts_israel = datetime.fromtimestamp(ts) + timedelta(hours=7)

            # get the date today in Israel and add the starting hours in Israel based on US time zone.  (+15 or 3pm).
            israel_time_start_dt= datetime.combine(ts_israel.date(), ts_israel.min.time() ) + timedelta(hours=int(hours_to_work))
            # add 9 hours of working time
            israel_time_end_dt = israel_time_start_dt + timedelta(hours=int(working_hours))

            return { 'israel_start_time': israel_time_start_dt.strftime('%Y-%m-%d %H:%M:%S'),
                     'israel_end_time': israel_time_end_dt.strftime('%Y-%m-%d %H:%M:%S')}

        except Exception as e:
            print("error on integer time format " + str(e))
            return {'us_start_time': 'error'}

class Index(Resource):

    def get(self):
        return {"index":"index"}


#endpoints
api.add_resource(Index,'/')
api.add_resource(UTCTime, '/getisraeltime/<string:us_time>')


if __name__ == '__main__':
    app.run(debug=True)