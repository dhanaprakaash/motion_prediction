class Robot():

    def __init__(self,name):
        self.name = name
        self.initial_loc = None
        self.destination_loc = None
        self.planned_path = []
        self.number_of_obstacles = 0
        self.number_of_recomp = 0
        self.mission_time = None
        self.battery_status = None
        self.distance_travelled =None


    def set_init_loc(self, pose):
        self.initial_loc = pose

    def get_init_loc (self):
        return self.initial_loc

    def set_dest_loc(self, pose):
        self.destination_loc = pose
    
    def get_dest_loc(self):
        return self.destination_loc
    
    def set_planned_path(self, path):
        self.planned_path = path
    
    def get_path_robot(self):
        return self.planned_path
    def print_details(self):
        print("Name",self.name)
        print("Initial Loc :", self.initial_loc)
        print("Destination LOc", self.destination_loc)
        print("Planned Path", self.planned_path)
    
