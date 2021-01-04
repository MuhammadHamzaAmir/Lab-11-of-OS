from socket import *
import time

def mainMenu():

    serverIP = input("Enter the IP address: ")
    username = input("Enter the user name: ")
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverIP, 95))
    clientSocket.send(username.encode('utf-8'))
    
    while (True):
        print("**File Management System**")

        print("""
            1.Create file
            2.Delete file
            3.Open file
            4.Close file
            5.Read file
            6.Write in the file
            7.Append in the end of text file
            8.Read from a specific point
            9.Write at the specific point
            10.Truncate
            11.Move within a file
            12.Show memory map
            13.Exit System 
            """)

        choice = input("What would you like to do: ")

        if choice == "1":
            fname = input(
                "Enter the name for the text file (without extension): ")
            send_data = "Create#"+fname
            clientSocket.send(send_data.encode('utf-8'))
            time.sleep(0.5)
            output = clientSocket.recv(204800).decode('utf-8')
            print(output)
        elif choice == "2":
            fname = input(
                "Enter the name for the text file you want to delete(without extension): ")
            send_data = "Delete#"+fname
            clientSocket.send(send_data.encode('utf-8'))
            time.sleep(0.5)
            output = clientSocket.recv(204800).decode('utf-8')
            print(output)
        elif choice == "3":
            fname = input(
                "Enter the name of the file you want to open(without extension): ")
            mode = input("Enter the file mode (r,w,a)")
            ob.Open(fname, mode)
        elif choice == "4":
            fname = input(
                "Enter the name of the file you want to close(without extension): ")
            ob.Close(fname)
        elif choice == "5":
            ob.Read_From_File()
        elif choice == "6":
            text = input("Enter data: ")
            ob.write_to_file(text)
        elif choice == "7":
            text = input("Enter data: ")
            ob.appendFile(text)
        elif choice == "8":
            start = input("Enter the starting point: ")
            size = input("Enter the string you want to read till: ")
            ob.read_from_file(start, size)
        elif choice == "9":
            write_at = input("Enter the point where you want to write: ")
            text = input("Enter Data: ")
            ob.Write_to_File(write_at, text)
        elif choice == "10":
            maxsize = input("Enter the size of the file, you want: ")
            ob.truncate(maxsize)
        elif choice == "11":
            start = input("Enter starting index: ")
            size = input("Enter the size of string: ")
            target = input("Enter where you want to put the string: ")
            ob.Move_within_file(start, size, target)
        elif choice == "12":
            ob.show_memory_map()
        elif choice == "13":
            ob.system_exit()
            break
        elif choice != "":
            print("\n Not Valid Choice Try again")


mainMenu()
