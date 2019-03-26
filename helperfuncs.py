from particle import *

def initiallize_particles(num_of_particles):
    '''
        This function will initialize all particles in the canvas. It will sort then in a random manner, with a random color
        for each one. it will put them all in a list and return that list. the size of the list will be decided by the parameter
        which the function gets.
        input:
            the number of particles
        output:
            the new list of particles.
    '''
    random.seed()
    lis = []
    for i in range(num_of_particles):
        lis.append(Particle(color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), loc = Location(random.randint(10, WIDTH - 10), random.randint(10, HEIGHT - 10)), speed = Vector(size = random.uniform(1, 10), angle = random.uniform(0, math.pi)), size = random.randint(5, 20)))
    return lis

def find_total_energy(particle_list):
    '''
        This function will find the total energy in the system, which will be calculated with physics and stuff.
    '''
    outcome = 0
    for particle in particle_list:
        outcome += particle.size * (particle.speed.size ** 2) /(2)
        outcome +=  particle.size * CONSTANT_ACCELERATION * (HEIGHT - particle.loc.locationY) /  (2)
    return int(outcome)

def get_opposite_color(color):
    new_color = []
    for byte in color:
        new_color.append(255 - byte)
    return tuple(new_color)

def generate_in_radius(pos, radius):
    '''
        This function will get a center position and a radius, and generate particles in that range, while also
        ensuring that no particles spawn outside of the borders.
        input:
            the center location of the circle, the radius of the circle.
        output:
            the new particles in the system.
    '''

    max_x, min_x = pos[0] + radius, pos[0] - radius
    max_y, min_y = pos[1] + radius, pos[1] - radius
    max_x = max_x if max_x < WIDTH else WIDTH
    max_y = max_y if max_y < HEIGHT else HEIGHT
    min_y = min_y if min_y > 0 else 0
    min_x = min_x if min_x > 0 else 0
    num_of_p = random.randint(0, NUM_OF_PARTICLES)
    new_parts = initiallize_particles(num_of_p)
    for part in new_parts:
        part.loc = Location(random.randint(min_x, max_x), random.randint(min_y, max_y))
    return new_parts