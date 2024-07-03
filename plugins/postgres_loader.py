from sqlalchemy import create_engine


def load(data, table_name):
    # Read the data from the text file
    with open('./data/config.txt', 'r') as file:
        lines = file.readlines()

    user = ''
    passwd = ''
    hostname = ''
    database = ''

    # Extract values
    for line in lines:
        if 'user' in line:
            user = line.split('=')[1].strip()
        elif 'passwd' in line:
            passwd = line.split('=')[1].strip()
        elif 'hostname' in line:
            hostname = line.split('=')[1].strip()
        elif 'database' in line:
            database = line.split('=')[1].strip()

    conn_string = f'postgresql://{user}:{passwd}@{hostname}:5432/{database}'

    db = create_engine(conn_string)
    conn = db.connect()

    data.to_sql(table_name, con=conn, if_exists='append',
                index=False)

    print("Successfully loaded to postgres")