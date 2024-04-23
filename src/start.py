import sys
import os
import importlib
import argparse

def execute_task(task):
    # Define the directory where tasks are located
    current_directory = os.getcwd()
    tasks_directory = current_directory
    task = 'task_' + task;

    # Check if the specified task exists
    task_path = os.path.join(tasks_directory, task + '.py')
    if os.path.exists(task_path):  # Check if task file has a ".py" extension
        # Execute the task
        print(f'Executing {task}...')
        
        # Dynamically import and execute the task module
        try:
            sys.path.append(tasks_directory)
            task_module = importlib.import_module(task)
            task_module.execute()
            print(f'{task} completed.')
        except Exception as e:
            print(f'Error executing {task}: {e}')

if __name__ == "__main__":
    # Create an argument parser
    parser = argparse.ArgumentParser(description='Execute a task.')

    # Add an argument for the task name
    parser.add_argument('task', help='Name of the task to execute')

    # Parse the command line arguments
    args = parser.parse_args()

    # Get the task from the parsed arguments
    task = args.task

    # Call the execute_task function with the specified task
    execute_task(task)
