from flask_restful import Resource, request
from bms.models import Battery
from bms import db
import csv
import os
import time


class MyApi(Resource):
    def get(self, token, task):
        battery = Battery.query.filter_by(token=token).first()
        if battery:
            if task == 'meta':
                json_battery = {'id': str(battery.id),
                                'name': str(battery.name),
                                'message': str(battery.token),
                                'last_health': str(battery.last_health),
                                'last_soc': str(battery.last_soc),
                                'last_voltage': str(battery.last_voltage),
                                'last_temp': str(battery.last_temp)
                                }
                return json_battery
            elif task == 'last':
                if os.path.exists('csv/'+token+'.csv'):
                    last_time = battery.last_time
                    if last_time:
                        return {'message': last_time}
                return {'message': '0'}
            return {'message': 'no-task'}
        return {'message': 'invalid-token'}

    def put(self, token, task):
        battery = Battery.query.filter_by(token=token).first()
        if battery:
            if task == 'write':
                f = open('csv/'+token+'.csv', 'a', newline='')
                dataset = csv.writer(f, delimiter=',')
                dataset.writerow([request.form['time'],
                                  request.form['voltage'],
                                  request.form['current'],
                                  request.form['temp'],
                                  request.form['cycles'],
                                  request.form['index']
                                  ])
                f.close()
                battery.last_temp = request.form['temp']
                battery.last_voltage = request.form['voltage']
                battery.last_time = request.form['index']
                db.session.commit()
                return {'message': 'ok'}
            return {'message': 'no-task'}
        return {'message': 'invalid-token'}
