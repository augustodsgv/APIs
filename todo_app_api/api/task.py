import pydantic
import datetime
class Task(pydantic.BaseModel):
    task_id : int
    task_name : str
    is_done : bool
    tags : list
    # due_date : datetime.datetime