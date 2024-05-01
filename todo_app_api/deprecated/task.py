from date import Date 
class Task:
    def __init__(self, id  : int, task_name : str, is_done : bool, tags : list = None, due_date : Date = None):
        self.id = id
        self.task_name : str = task_name
        self.is_done : bool = is_done
        if due_date != None and not isinstance(due_date, Date):
            raise Exception('due_date parameter should have "Date" type, not {}'.format(type(due_date)))
        self.due_date : Date = due_date
        if tags == None:
            self.tags = []
        else:
            for tag in tags:
                if not Task.is_valid_tag(tag):
                    raise Exception(f'Invalid tag {tag}, from tag list')
            self.tags = tags
    
    def __eq__(self, other : object)->bool:
        if not isinstance(other, Task): return False
        if self.task_name != other.task_name: return False
        if self.is_done != other.is_done: return False
        if self.due_date != other.due_date: return False
        if self.tags != other.tags: return False
        return True
    
    # TODO : Add more tag restrictions
    @classmethod
    def is_valid_tag(cls, tag : str):
        return type(tag) == str
    # Returns if a task has a specific tag
    def has_tag(self, tag : str)->bool:
        return tag in self.tags
    
    # Adds a tag to the task. Returns if it was added (True) or if it was already there
    def add_tag(self, tag : str)->bool:
        if not Task.is_valid_tag(tag): raise Exception('Tag must be a string')
        if self.has_tag(tag): return False
        self.tags.append(tag)
        return True
    
    def rm_tag(self, tag : str)->bool:
        if not self.has_tag(tag): return False
        self.tags.remove(tag)
        return True
    
    # Task conversion to SQL tuple
    def get_tuple(self)->tuple:
        return (self.id, self.task_name, self.is_done)

    # Task tags conversion to SQL tuple
    def get_tags_tuple(self)->list:
        tag_tuples = [(self.id, tag) for tag in self.tags]
        return tag_tuples