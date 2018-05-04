try:
    my_file_handle=open("C:\\Users\\dhana.mani\\Documents\\Python\\SimpleClass.py")
    for line in my_file_handle:
        print(line)
except IOError:
    print("File not found or path is incorrect")
finally:
    my_file_handle.close()
    print("exit")