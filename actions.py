from helperfuncs import *
from config import *

# This class will contain all actions which the user controls.
class Actions:
        
    # The initial 'speed' of the running of the program, will basically change the number of frames running per second.
    speed = 10
    draw_speeds = False

    # User wants to speed up the program ( more fps for some reason )
    def speed_up(self, part_list):
        self.speed += 1
        return part_list
    # User wants to slow down the program
    def slow_down(self, part_list):
        self.speed -= 1
        return part_list
    # User wants to turn off/on the 'draw speeds' feature on the particles in the system
    def toggle_draw_speed(self, part_list):
        self.draw_speeds = not self.draw_speeds
        return part_list
    # Another stupid, very useless feature. 
    def messup(self, part_list):
        if part_list:
            all_speed = part_list[-1].speed
            for particle in part_list[:-1]:
                particle.speed.change_angle(all_speed.angle)
        return part_list
    # Clear out all the particles in the canvas thing.
    def clear_part(self, part_list):
        part_list.clear()
        part_list = initiallize_particles(NUM_OF_PARTICLES)
        return part_list
    # This function will get the input from the user, and call the corresponding function.
    def act(self, key, part_list):
        # Each key is mapped to a different function. For each function the parameter is only the list of the particles.
        key_mappings = {'X':self.speed_up, 'Z':self.slow_down, 'D':self.toggle_draw_speed, 'U':self.messup, 'H':self.clear_part}
        if key in key_mappings:
            return key_mappings[key](part_list)
        return part_list

