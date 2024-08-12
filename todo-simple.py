"""An incredibly basic CLI todo list. Add, remove, and view items. Items are not saved to storage.
   This is a simple program that will be expanded on for a larger project."""

from sys import argv
commands =["add", "remove","view","help","quit"]
tasks=[]

done = False

while not done:
    print("What would you like to do?")
    com=input("")
    if com == "add":
        task=input("What task do you want to add?")
        tasks.append(task)
        print("Task added")
    elif com=="remove":
        task=input("What task would you like to remove?")
        for thing in tasks:
            print(thing)
        if task not in tasks:
            print("Task not in list or it's misspelt.")
        else:
            tasks.remove(task)
            print("Task removed")
    elif com=="view":
        print("Current tasks:")
        for thing in tasks:
            print(thing)
    elif com== "help":
        print("Commands available:")
        for command in commands:
            print(command)
    elif com== "quit":
        done = True
    else:
        print("I don't recognize that command.")