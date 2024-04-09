import argparse
import math
import random


def main():
    parser = argparse.ArgumentParser(description='Particle shielding simulation.')

    parser.add_argument('--numParticles', type=int, metavar='K', default=100,
                    help='number of particles (neutrons)  to simulate')
    parser.add_argument('--thickness', type=float, metavar='w', default=2,
                    help='shield thickness measured in particles')
    parser.add_argument('--density', type=float, metavar='d', default=0.5,
                    help='density of shielding material')
    parser.add_argument('--collisions', type=int, metavar='c', default=100,
                    help='number of times each particle (neutron) collides with atoms within shield')
    parser.add_argument('--momentum', type=float, metavar='m', default=0.9,
                    help='proportion of incident momentum retained after each collision')
    parser.add_argument('--proportionality', type=float, metavar='p', default=0.5,
                    help='constant of proportionality')

    args = parser.parse_args()
    numParticles = args.numParticles
    w = args.thickness
    d = args.density
    c = args.collisions
    m = args.momentum
    p = args.proportionality

    penetrated = 0   #### <------- this is the shared variable
    deltaX = p/d

    random.seed(42)
    for i in range (numParticles):   #### <---- this could be parallelized
        x = deltaX
        momentum = 1.0
        for k in range(c):
            x += math.cos(math.pi*random.random()) * deltaX*momentum
            if x>w:
                penetrated += 1
                break
            elif x < 0:
                break
            else:
                momentum *= m

    print ("penetrated:", penetrated)

        
if __name__ == "__main__":
    main()
