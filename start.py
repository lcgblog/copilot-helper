import sys
import os
import importlib

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
    # Get the task from command line arguments
    if len(sys.argv) < 2:
        print("Please provide a task name as a command line argument.")
        sys.exit(1)
    task = sys.argv[1]

    # Call the execute_task function with the specified task
    execute_task(task)
