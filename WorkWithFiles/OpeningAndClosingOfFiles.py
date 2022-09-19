myfile = open("hello.txt", "w")

myfile.close()

try:
    somefile = open("hello.txt", "w")
    try:
        somefile.write("Hello world!")
    except Exception as e:
        print(e)
    finally:
        somefile.close()
except Exception as e:
    print(e)

with open("hello.txt", "w") as filename:
    filename.write("Hello World2!")