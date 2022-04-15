import sys
import datetime


usage = "Usage :-\n$ ./todo add \"todo item\"  # Add a new todo\n$ ./todo ls               # Show remaining todos\n$ ./todo del NUMBER       # Delete a todo\n$ ./todo done NUMBER      # Complete a todo\n$ ./todo help             # Show usage\n$ ./todo report           # Statistics"

# USING IF ELSE LADDER AS A MENU 
# FIRST, HELP FUNCTION
if len(sys.argv)==1 or sys.argv[1]=="help":
    sys.stdout.buffer.write(usage.encode('utf-8'))

# SECOND, ADD FUNCTION
elif sys.argv[1]=="add":
    if len(sys.argv) <3:
        print("Error: Missing todo string. Nothing added!") 
    else:
        f=open("todo.txt","a")
        for i in range(2,len(sys.argv)):
            task= sys.argv[i]
            sys.stdout.buffer.write('Added todo: "{}"\n'.format(str(task)).encode('utf-8'))
            f.write(task+"\n")
        f.close()
            
# THIRD, LIST DISPLAY FUNCTION 
elif sys.argv[1]=="ls":
    with open("todo.txt","at+") as f:
        f.seek(0)
        line_list = list(f.readlines())
    if len(line_list) == 0:
        print("There are no pending todos!")
    else:       
        idx = len(line_list)
        for line in line_list[::-1]:
            x=line.rstrip()
            sys.stdout.buffer.write('[{}] {}\n'.format(idx,x).encode('utf-8'))
            idx-=1
        
# FOURTH, DELETE FUNCTION
elif sys.argv[1]=="del":
    l=sys.argv[2:]
    if len(l)>0:
        f= open("todo.txt","r")
        fl = len(list(f))
        f.close()
        for i in range(2,len(l)+2):
            num = int(sys.argv[i])
            if num <= fl and num !=0:
                n=num-1
                with open('todo.txt', 'r') as f:
                    lines= f.readlines()
                with open("todo.txt","w") as f:
                    f.writelines(lines[:n] + lines[n+1:])
                print("Deleted todo #{}".format(num))
            else:
                print("Error: todo #{} does not exist. Nothing deleted.".format(num))
    else:
        print("Error: Missing NUMBER for deleting todo.") 

# FIFTH, DONE FUNCTION
elif sys.argv[1]=="done":
    l=sys.argv[2:]
    if len(l) > 0:
        num = int(sys.argv[2])
        if num == 0:
            sys.stdout.buffer.write("Error: todo #0 does not exist.".encode('utf-8'))
        else: 
            n=num-1
            with open('todo.txt', 'r') as f:
                lines= f.readlines()
            with open("todo.txt","w") as f:
                f.writelines(lines[:n] + lines[n+1:])
            with open("done.txt","a") as d:
                x= datetime.date.today()
                line = str(x) +" "+ "".join(lines[n]) 
                d.write(line)
            sys.stdout.buffer.write("Marked todo #{} as done.".format(num).encode('utf-8'))
    else:
        sys.stdout.buffer.write("Error: Missing NUMBER for marking todo as done.".encode('utf-8'))
# FINALLY, REPORT FUNCTION
elif sys.argv[1]=="report":
    with open("todo.txt","r") as f:
        n1=len(list(f))
    with open("done.txt","r") as d:
        n2=len(list(d))
    x=datetime.date.today()
    sys.stdout.buffer.write("{} Pending : {} Completed : {}".format(x,n1,n2).encode('utf-8'))
else:
    sys.stdout.buffer.write(usage.encode('utf-8'))