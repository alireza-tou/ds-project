class Path:

    dir_stack = []

    def __init__(self):
        print("App started")
        main_dir = {'/': {}}
        self.dir_stack.insert( len(self.dir_stack), main_dir)

    def mkdir(self, folder_Name):
        current_Level = self.dir_stack[len(self.dir_stack) - 1]
        newDir = {folder_Name: {}}
        current_Map = current_Level[(list(current_Level.keys())[0])]
       
        if folder_Name in current_Map:
            warning = folder_Name +  ' already exists in directory'
            print(warning)
        else:
            current_Map.update(newDir)

    def rmdir(self, folder_Name):
        current_Level = self.dir_stack[len(self.dir_stack) - 1]
        #make global var current_Map
        current_Map = current_Level[(list(current_Level.keys())[0])]  
        if folder_Name in current_Map:
            del current_Map[folder_Name]
        else:
            print('folder doesnt exist')


    def getCurrentMap(self):
        global current_Level
        current_Level = self.dir_stack[len(self.dir_stack) - 1]

   
    def cd(self, folder):
        if(folder == '../'):
            self.dir_stack.pop()

        current_Level = self.dir_stack[len(self.dir_stack) - 1]
        current_Map = current_Level[(list(current_Level.keys())[0])]
        print('lev', current_Map)
        if folder in current_Map:
            print('here')
            self.dir_stack.insert(len(self.dir_stack), current_Map)
        else:
            print ("no existing folder")

    def pwd(self):
        path = ''
        print(self.dir_stack)
        for x in self.dir_stack:
            path += (list(x.keys())[0]) + '/'
        print(path)

    def ls(self):
        current_Level = self.dir_stack[len(self.dir_stack) - 1]
        current_Map = current_Level[(list(current_Level.keys())[0])]
        print(current_Map)





# driver code


fs = Path()
fs.mkdir('usr')
fs.mkdir('new')
fs.mkdir('files')
fs.ls()
fs.cd('usr')
fs.mkdir('local')
fs.cd('new')
fs.pwd()
fs.cd('../')
fs.ls()
# fs.mkdir('local')
# fs.cd('local')
fs.pwd()