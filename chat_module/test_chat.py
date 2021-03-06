'''
    Test for chat modules
'''

import sqlite3
from chat import chat_api as c

def test_add_reading():
    response = c.put({
        'request': 'POST',
        'sender_ID': 1,
        'receiver_ID': 2,
        'conversation_ID': 1,
        'message_type': 1,
        'message': "Nice to meet you!",
        'time': "2022-02-15 00:00:00",
    })
    assert response['success'] == True

def test_get_reading():
    response = c.get({
        'request': 'GET',
        'conversation_ID': 1
    })
    # Deleting test dummy entry
    connection = sqlite3.connect('database/health_care_DB.db')
    cursor = connection.cursor()
    cursor.execute('''DELETE FROM messages WHERE conversation_ID==1 AND message=='Nice to meet you!';''')
    connection.commit()
    connection.close()
    assert response['success'] == True
