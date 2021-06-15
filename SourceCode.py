import os;

####################
def kill():
    os.system('TASKKILL /F /IM LOCKER.exe');
####################
def lock(folderPath):
    try:
        os.system(f'cacls "{folderPath}" /P everyone:n');
    except Exception:
        print('ERROR')
        kill()
####################
def unlock(folderPath):
        os.system(f'cacls "{folderPath}" /P everyone:f');
####################

print('please enter the file/folder path which you want to lock');
path = str(input('>'));
if path != "":
    command = input('Enter the command "l to lock and u to unlock": ');
    if 'l' in command:
        lock(path);
    elif 'u' in command:
        unlock(path);
    else:
        print('Enter a valid command');
        kill();
else:
    kill();