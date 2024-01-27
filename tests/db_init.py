import sqlite3

conn = sqlite3.connect('smart_home.db')
print(f"SQLite database file #################### created successfully.")
c = conn.cursor()

with conn:
    c.execute("""CREATE TABLE devices (
                DeviceId text,
                DeviceType text,
                DeviceName text,
                DeviceGroup text,
                DeviceLocation text,
                DeviceTopicSub text,
                DeviceTopicPub text
        )""")

