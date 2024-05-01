import psycopg
import os

user = os.environ['POSTGRES_USER']
password = os.environ['POSTGRES_PASSWORD']
database_name = os.environ['POSTGRES_DB']
database_url = os.environ['DATABASE_URL']
database_port = os.environ['DATABASE_PORT']

def connect_to_psql():
    with psycopg.connect('host={} port={} dbname={} user={} password={}'.format(database_url, database_port, database_name, user, password)) as conn:
        with conn.cursor() as cur:
            return cur

def select_tasks(task_id : int = None) -> list:
    with psycopg.connect('host={} port={} dbname={} user={} password={}'.format(database_url, database_port, database_name, user, password)) as conn:
        with conn.cursor() as cur:
            if task_id == None:
                cur.execute('''SELECT tasks.task_id, tasks.task_name, tasks.is_done, tags.tag_name
                            FROM tasks LEFT JOIN tags
                            ON tasks.task_id = tags.task_id''')
            else:
                cur.execute('''SELECT tasks.task_id, tasks.task_name, tasks.is_done, tags.tag_name
                            FROM tasks LEFT JOIN tags
                            ON tasks.task_id = tags.task_id
                            WHERE tasks.task_id = %s''',
                            (task_id, ))
            
            query_response = cur.fetchall()            
    
    return query_response

def update(table, id : int, id_name : str, attribute : str, value : str) -> list:
    with psycopg.connect(f'host={database_url} port={database_port} dbname={database_name} user={user} password={password}') as conn:
        with conn.cursor() as cur:
            cur.execute('UPDATE %s SET %s = %s WHERE %s = %s', (table, attribute, value, id_name, id))
            query_respose = cur.fetchall()
    return query_respose

# Transforma query lists that uses union into a dict that stores the tags
def query_to_dict(query : list)->dict:
    query_dict = {}         # Indexes by id
    # Tuple format (task_id, task_name, is_done, tag)
    for task_tuple in query:
        task_id, task_name, is_done, task_tag = task_tuple
        if task_id not in query_dict.keys():      # Case the task from tuple has not been added to dict
            query_dict[task_id] = (task_id, task_name, is_done, [])
        
        if task_tag != None:
            query_dict[task_id][-1].append(task_tag)        # [-1]  is the tags list
    return query_dict
            




def create_database(database_name):
    pass
