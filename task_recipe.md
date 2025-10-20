# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python

class TaskManager:

    def __int__(self):
        # Parameters:
        #   none
        # Side effects:
        #   Creates an empty list to store tasks
        pass

    def create_task(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   nothing
        # Side effects:
        #   saves the task as a list to the list initialised in init function
        pass

    def view_all_tasks(self):
        # Parameters:
        #   None
        # Returns:
        #   A list of all uncompleted tasks
        # Side effects: 
        #   If all called when there are no tasks, return message 'There are no uncompleted tasks'

    def mark_as_complete(self, task_id):
        # Parameters:
        #   task_id: an integer that represents the index of the task in the list
        # Returns:
        #   nothing
        # Side effects:
        #   Updates the task list by removing specified task
        #   Throws exception if task_id does not exist
        pass


```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python


"""
Given a task
create_task adds the task to the list
"""

task_manager = TaskManager()
task_manager.create_task('Walk the dog')
task_manager.view_all_tasks() => [['TODO: Walk the dog']]

"""
When trying to view all tasks when there are none
A message saying 'There are no uncompleted tasks' is returned
"""
task_manager = TaskManager()
task_manager.view_all_tasks() => 'There are no uncompleted tasks'

"""
When there are uncompleted tasks in the list
Given the index of the task
The mark_as_complete function should remove the specified task from the list
"""

task_manager = TaskManager()
task_manager.create_task('Walk the dog')
task_manager.mark_as_complete(0)
task_manager.view_all_tasks() => 'There are no uncompleted tasks'

"""
Given an index of a task that doesnt exist
It should throw an exception and return a message 'That task does not exist'
"""
task_manager = TaskManager()
task_manager.mark_as_complete(0) => 'That task does not exist'

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

<!-- wowowowo -->
