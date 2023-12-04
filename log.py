def log(file,content):
    file = open(file=file, mode="a+")
    file.write(f'{content}\n')
    file.close()