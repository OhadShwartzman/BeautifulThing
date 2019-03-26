from particle import *
from actions import *
import pygame

def main():
    '''
        This is the main function of the program, it will manage it and call most of the functions. This program is pretty
        useless. I must say. It's a kind-of not-so accurate simulator of physics with python and pygame, or what I like to call
        ' The - I had nothing to do over the summer so I did a thing.'
        input:
            none
        output:
            none
    '''
    pygame.init()
    display = pygame.display.set_mode(SIZE)
    clock  = pygame.time.Clock()
    part_list = initiallize_particles(NUM_OF_PARTICLES)
    back_color = (0, 0, 0)
    frame_id = 0
    count_lost = 0
    pygame.font.init()
    new_begin_loc = None
    # Define the font which the text on the screen will be written with.
    font = pygame.font.SysFont('Comic Sans MS', 40)
    col_count = 0
    ac = Actions()
    while 1:
        speed = ac.speed
        draw_speeds = ac.draw_speeds
        
        clock.tick(speed * 6)
        display.fill(back_color)
        # This list will contain all of the information that we wish to present to the user. 
        text_list =["Particles: " + str(len(part_list)), 
                    "FPS: " + str(speed * 6),
                    "Total Energy: " + str(find_total_energy(part_list)), 
                    "Particles Lost: " + str(count_lost),
                    "Draw Speeds: " + str(draw_speeds),
                    "Number Of Collisions: " + str(col_count)] 
        # Write down all of the information on the canvas.
        for i, label in enumerate(text_list):
            textsurface = font.render(label, False, (255, 255, 255))
            display.blit(textsurface, (0,25 * i))

        # finally, draw down each particle in the system.
        for particle in part_list:
            pygame.draw.circle(display, particle.color, particle.loc.get_values(), particle.size)

            if draw_speeds:
                start_loc = particle.loc
                end_loc = Location(start_loc.locationX + particle.speed.x * GRAPHICAL_SPEED_MULTIPLIER, start_loc.locationY + particle.speed.y * GRAPHICAL_SPEED_MULTIPLIER)
                pygame.draw.line(display, get_opposite_color(particle.color), start_loc.get_values(), end_loc.get_values())

        pygame.display.flip()

        # This loop will handle movement of each particle in the canvas. it will count on the speed of the 
        # particle, and change the speed of it ( cause of gravity )
        for particle in part_list:
            particle.loc.locationX += int(particle.speed.x)
            particle.loc.locationY += int(particle.speed.y)
            # Because this isn't a PERFECT SYSTEM, we sometimes need to reduce the acceleration.
            if particle.speed.y < 15:
               particle.speed.change_y(particle.speed.y + CONSTANT_ACCELERATION / (speed * 6))

        # This loop will handle deflection of each particle in the canvas. It will check if the particle is coliding with the
        # Borders of it or with other particles.
        for i, particle in enumerate(part_list):
            # If the particle is not coliding with the borders of the canvas, try to colide it with other particles.
            if not particle.bounce_off_static(WIDTH, HEIGHT):
                collider = None
                # This loop will check for each other particle in the system, if it is coliding with this particle.
                for obj in part_list[i+1:]:
                    if particle.check_obj_collision(obj):
                        collider = obj
                        break
                # If there is a colider with the particle, handle the change in speed and movement.
                if collider:
                    col_count += 1
                    particle.deflection(collider)

        # This loop is our error - fixing thing. it will check if any particles were lost - if any particles somehow came
        # Out of the border of the canvas, and put them back in it.
        for particle in part_list:
            if not WIDTH > particle.loc.locationX > 0 or not HEIGHT > particle.loc.locationY > 0:
                particle.loc.locationX = random.randint(0, WIDTH)  
                particle.loc.locationY = random.randint(0, HEIGHT)
                count_lost += 1

        event_list = pygame.event.get()
        # This loop will run over the events which the user activated in the system, say, the user pressed a button
        # or released a button, or the user pressed the button to quit the program, this will all be handles in this 
        # section.
        for event in event_list:
            # If the user pressed the button to quit the program, close it.
            if event.type == pygame.QUIT:
                quit()
            # If the user pressed a button in his mouse, check if it's mouse1, if it is make a new start point which
            # will be used when the user releases his mouse. if it's mouse2, spawn particles randomly in a radius.
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # event_dict contains details about the events of the user input, in this case we use it to check which
                # button was pressed down by the user.
                event_dict = event.__dict__
                if event_dict['button'] == 1:
                    # Initiallize a new start point of spawning a new particle, this will be used when we release the button, 
                    # The starting speed vector of the new particle will be in the direction and the size of movement between
                    # the first point and the second point.
                    pos = event_dict['pos']
                    new_begin_loc = Location(pos[0], pos[1])
                else:
                    # Generate particles randomly in a constant radius. this is a VERY stupid feature.
                    part_list += generate_in_radius(event_dict['pos'], RADIUS)
            # Ah, if you got to here you must be invested in this code, or just very very bored. This is where 
            # we act if the user releases his mouse button. In here, we measure what the starting speed of the new particle
            # is according to the starting location of his mouse and his new one, and make a new particle in that location
            # with that speed.
            elif event.type == pygame.MOUSEBUTTONUP and new_begin_loc:
                new_end_loc = event.__dict__['pos']
                new_end_loc = Location(new_end_loc[0], new_end_loc[1])
                # delta-x and delta-y variables will help us to check on the size and direction of the particle's speed vector.
                dy = new_end_loc.locationY - new_begin_loc.locationY
                dx = new_end_loc.locationX - new_begin_loc.locationX
                # Generate the speed - the multiplier is a constant, which is reappearing throughout the program so I figured
                # what the hell.
                new_speed = Vector()
                new_speed.set_xy(dx / GRAPHICAL_SPEED_MULTIPLIER, dy / GRAPHICAL_SPEED_MULTIPLIER)
                # Initiallize the new particle in the program, with a random color, the starting location will be the 
                # beginning location of the mouse thing, the speed will be the one we just calculated.
                new_particle = Particle(color = (random.randint(0,255),random.randint(0,255),random.randint(0,255)), loc = new_begin_loc, speed = new_speed, size = random.randint(5, 25))
                new_begin_loc = None
                part_list.append(new_particle)
            # If the event is caused by the user pressing down one of his keys on his keyboard, then do things.
            elif event.type == pygame.KEYDOWN:
                key = event.__dict__['unicode'].upper()
                
                part_list = ac.act(key, part_list) # Call the function according to the button pressed 
        frame_id += 1

main()