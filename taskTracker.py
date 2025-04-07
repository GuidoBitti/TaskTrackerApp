# import argparse
import argparse
import json
import os
import datetime
from tabulate import tabulate

FILE_NAME='tasks.json'

#function to show the info of a task
def print_info(data):
    header = ['ID','Description','Status','Date of creation','Date of last update']
    body=[[task['id'],task['description'],task['status'],task['created-at'],task['updated-at']] for task in data]
    print(tabulate(body,headers=header,tablefmt="grid"))
    
def is_id(id,data):
    left=0
    right=len(data)-1
    while left<=right:
        mid=(left+right)//2
        mid_id=data[mid]["id"]
        if mid_id==id:
            return mid
        elif mid_id<id:
            left=mid+1
        else:
            right = mid-1
    return -1
    
    
#function to get the tasks(defaut all)
def get_tasks_by_type(type=None):
    #checks if the file exists
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as f:
            data = json.load(f)
    else:
        with open(FILE_NAME, 'w') as f:
            data = []
            json.dump(data, f, indent=4)
    
    if(type):
        data=[t for t in data if t["status"].lower()==type]
        
    return data

#function to update the json file
def update_tasks(data):
    with open(FILE_NAME, 'w') as f:
            json.dump(data, f, indent=4)

#function to add a new task
def add_new_task(description):
    #gets the time of creation
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    new_data={'description':description, 'status':'To-do', 'created-at':date, 'updated-at':date}
    
    data=get_tasks_by_type()
    
    #writes the new task in the json
    new_data['id']=int(data[-1]['id'])+1 if len(data)>0 else 1
    data.append(new_data)
    
    #updates the json
    update_tasks(data)
    print('Data added: ')
    print_info([new_data])
            
#function to update the infomation of the id given
def update_task_by_id(id,new_description=None,new_status=None):
    data=get_tasks_by_type()
    pos=is_id(id,data)
    if pos>=0:
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data[pos]["updated-at"]=date
        if new_description:
            data[pos]["description"]=new_description
        if new_status:
            data[pos]["status"]=new_status
        update_tasks(data)
        print('Data updated: ')
        print_info([data[pos]])
        
    else:
        print(f'ID {id} not found.\n')
        
#function to delete the task of the id given
def delete_task_by_id(id):
    data=get_tasks_by_type()
    pos=is_id(id,data)
    if pos>=0:
        print('Check the task:')
        print_info([data[pos]])
        option=''
        while option!='Y' and option!='N':
            option=input('Are you sure to delete?(Y/N):')
        
        if option=='Y':
            data.pop(pos)
            update_tasks(data)
            print('Deleted succesfully.\n')
        else:
            print('Delete canceled.\n')
        
        
    else:
        print(f'ID {id} not found.\n')

#function to print all the tasks given a parameter(dafult all):
def list_tasks(type=None):
    data=get_tasks_by_type(type)
    print_info(data)

def main():    
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="option", required=True, help="Subcomandos disponibles")
    
    #option add:
    parser_add = subparsers.add_parser('add', help='Add a new task')
    parser_add.add_argument('description', help='Description of the task')
    
    #option update:
    parser_update = subparsers.add_parser('update', help='Update a new task')
    parser_update.add_argument('id', type=int, help='ID of the task to update')
    parser_update.add_argument('description', help='New description of the task')

    #option delete:
    parser_delete = subparsers.add_parser('delete', help='Delete a task')
    parser_delete.add_argument('id', type=int, help='ID of the task to delete')
    
    #option progress:
    parser_progress = subparsers.add_parser('mark-in-progress', help='change the status of a task to in-progress')
    parser_progress.add_argument('id', type=int, help='ID of the task to change the status')
    
    #option done:
    parser_done = subparsers.add_parser('mark-done', help='change the status of a task to done')
    parser_done.add_argument('id', type=int, help='ID of the task to change the status')
    
    #option done:
    parser_list = subparsers.add_parser('list', help='change the status of a task to done')
    parser_list.add_argument('filter', type=str, choices=['to-do','in-progress','done',None], default=None, nargs='?', help='Filter for the list(to-do/in-progress/done)')
    
    args = parser.parse_args()
    if args.option == "add":
        add_new_task(args.description)
    elif args.option == "update":
        update_task_by_id(args.id,new_description=args.description)
    elif args.option == "delete":
        delete_task_by_id(args.id)
    elif args.option == "mark-in-progress":
        update_task_by_id(args.id,new_status='In-progress')
    elif args.option == "mark-done":
        update_task_by_id(args.id,new_status='Done')
    elif args.option == 'list':
        list_tasks(args.filter)
    
if __name__ == "__main__":
    main()