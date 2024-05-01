import fastapi
import sql_querys
import task

todo_api = fastapi.FastAPI()

@todo_api.get("/")
async def root(task_id : str = None):
    query : list = sql_querys.select_tasks(task_id)
    print(query)
    task_dict : dict = sql_querys.query_to_dict(query)
    task_list = []
    for task_tuple in task_dict.values():
        print(task_tuple)
        task_id, task_name, is_done, tags = task_tuple
        new_task = task.Task(task_id=task_id, task_name=task_name, is_done=is_done, tags=tags)

        task_list.append(new_task)
    
    return task_list

@todo_api.post("/")
async def add_task(new_task : task.Task):
    return new_task.model_dump_json()
