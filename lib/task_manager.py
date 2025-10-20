class TaskManager():
    
    def __init__(self):
        self.task_list = []

    def create_task(self, task):
        task = [f'TODO: {task}']
        self.task_list.append(task)

    def view_all_tasks(self):
        if len(self.task_list) > 0:
            return self.task_list
        else:
            return 'There are no uncompleted tasks'
        
    def mark_as_complete(self, task_id):
        if isinstance(task_id, int):
            try:
                self.task_list.pop(task_id)
            except IndexError:
                raise Exception('That task does not exist')
        return 'Task ID must be an integer representing the index of the task'