class Human():
    def __init__(self,name):
        self.name = name
        self.init_loc =None
        self.dst_loc =None
        self.predicted_path = None

    
    def set_init_loc(self, pose):
        self.init_loc = pose
    
    def get_init_loc(self):
        return self.init_loc
    
    def set_dst_loc(self, pose):
        self.dst_loc = pose

    def get_dst_loc(self):
        return self.dst_loc

    def set_path(self, path):
        self.predicted_path = path

    def get_path_human(self):
        return self.predicted_path


    def print_details(self):
        print("Name",self.name)
        print("Initial Loc :", self.init_loc)
        print("Destination LOc", self.dst_loc)
        print("Predicted Path", self.predicted_path)
