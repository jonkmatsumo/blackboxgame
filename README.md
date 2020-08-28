# Black Box
Black Box was a board game published by the Waddingtons in the 1970s. The game consists of players shooting rays into a black box, an area the users know nothing about.
Per the [Wikipedia](https://en.wikipedia.org/wiki/Black_Box_(game)) page, As they traverse through this Black Box, the rays change position as they encounter "atoms", the objects that the players are looking for. An example of a Black Box game board is:

![Sample Black Box Board](/assets/blackboxboard.png)


A "ray" will move forward from the direction it is declared until one of the following occurs:

- Hit: A ray encounters an Atom in its direct path. The ray ends here and there is no exit point.

![Sample Hit](/assets/blackboxhit.png)

- Deflection: If a ray comes in the proximity of (but does not touch) an Atom, it rotates its path 90 degrees in the opposite direction.

![Sample Deflection](/assets/blackboxdeflection.png)

- Reflection: If a ray comes in the proximity of two Atoms, it reverses its path. A Reflection starts and ends at the same position.

![Sample Reflection](/assets/blackboxreflection.png)

- Double Deflection: A ray can get deflected more than once.

![Sample Double Deflection](/assets/blackboxdoubledeflection.png)

- Miss: A ray that does not encounter any atoms (either directly or in its proximity) traverses the board in a straight line.

![Sample Miss](/assets/blackboxmiss.png)

- Detour: A ray that does not result in a Hit or a Reflection is called a Detour. These include single or multiple deflections and misses.

![Sample Detour](/assets/blackboxdetour.png)


Each Entry and Exit location count as a point. Per the [Wikipedia](https://en.wikipedia.org/wiki/Black_Box_(game)) page, "Hits and reflections therefore cost one point, while detours cost two points. When the seeker guesses the location of the atoms in the grid, each misidentified atom position costs penalty points: ten in the original Waddingtons rules, five in the Parker Brothers version and most computer editions." For this implementation, the penalty points are decided in accordance to the latter.
