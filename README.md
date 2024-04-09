## Shielding simulation experiment 
(translated into Python.)

The particle shielding simulation is a
parameterized Monte Carlo algorithm.

It simulates the collision of K particles with a W-unit
thick shield constructed of material with density D.
We model a sub-atomic particle, e.g. a neutron,
which collides C times with atoms within the shield,
each time bouncing off in a random direction and retaining
M percentage of its incident momentum. The horizontal
distance traveled between collisions, deltaX, is inversely
related to the material density by a constant of proportionality P.

This text is taken from
"Scientific Computation with JavaSpaces"
by Michael S. Noble & Stoyanka Zlateva (2001).
https://doi.org/10.1007/3-540-48228-8_75
See "algorithm body" on p663.

The Python code is transliterated from the
C code given in the paper.
