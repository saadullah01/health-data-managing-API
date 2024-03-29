'''
 This file contains functions for all the devices interface
 and add user entered data to the database in proper format.
'''
import sqlite3

class device_api():
    def get(inp):
        connection = sqlite3.connect('database/health_care_DB.db')
        user_ID = None
        response = {
            'success': False,
            'message': list()
        }
        # user_ID
        try:
            user_ID = int(inp['user_ID'])
        except:
            response['message'] = "Error! Invalid user_ID format"
            return response
        
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM measurements WHERE user_ID==?;''', (user_ID,))
        readings = cursor.fetchall()
        connection.commit()
        connection.close()

        response['success'] = True
        for r in readings:
            response['message'].append({
                'user_ID': r[0],
                'device_ID': r[1],
                'reading': r[2],
                'time': r[3]
            })
        return response

    def put(inp):
        connection = sqlite3.connect('database/health_care_DB.db')
        user_ID, device_type, reading, time = None, None, None, None
        response = {
            'success': False,
            'message': None
        }
        # user_ID
        try:
            user_ID = int(inp['user_ID'])
        except:
            response['message'] = "Error! Invalid user_ID format"
            return response
        # device_ID
        try:
            device_type = int(inp['device_ID'])
        except:
            response['message'] = "Error! Invalid device_ID format"
            return response
        # value
        try:
            reading = float(inp['reading'])
        except:
            response['message'] = "Error! Invalid reading format"
            return response
        # time
        try:
            time = str(inp['time'])
        except:
            response['message'] = "Error! Invalid time format"
            return response

        cursor = connection.cursor()
        cursor.execute('''INSERT INTO measurements(user_ID,device_ID,reading,time) VALUES(?,?,?,?);''', (user_ID, device_type, reading, time))
        connection.commit()
        connection.close()

        response['success'] = True
        response['message'] = "Successfull!"
        return response

    def delete(inp):
        pass
