from lib.task_manager import TaskManager
import pytest


def test_view_all_tasks_given_no_tasks():
    task_manager = TaskManager()
    assert task_manager.view_all_tasks() == 'There are no uncompleted tasks'

def test_view_all_tasks_given_some_tasks():
    task_manager = TaskManager()
    task_manager.create_task('Walk the dog')
    task_manager.create_task('Walk the cat')
    task_manager.create_task('Walk the fish')
    assert task_manager.view_all_tasks() == [['TODO: Walk the dog'], ['TODO: Walk the cat'], ['TODO: Walk the fish']]


def test_create_task():
    task_manager = TaskManager()
    task_manager.create_task('Walk the dog')
    pass

def test_mark_task_as_completed_given_some_tasks():
    task_manager = TaskManager()
    task_manager.create_task('Walk the dog')
    task_manager.create_task('Walk the cat')
    task_manager.mark_as_complete(0)
    assert task_manager.view_all_tasks() == [['TODO: Walk the cat']]

def test_mark_task_as_completed_given_zero_tasks():
    task_manager = TaskManager()
    with pytest.raises(Exception) as e:
        task_manager.mark_as_complete(2)
    error_message = str(e.value)
    assert error_message == 'That task does not exist'
