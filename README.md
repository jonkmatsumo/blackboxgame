# Black Box
Black Box was a board game published by the Waddingtons in the 1970s. The game consists of players shooting rays into a black box, an area the users know nothing about.
Per the [Wikipedia](https://en.wikipedia.org/wiki/Black_Box_(game)) page, As they traverse through this Black Box, the rays change position as they encounter "atoms", the objects that the players are looking for. An example of a Black Box game board is:

![Sample Black Box Board](/assets/blackboxboard.png)


A "ray" will move forward from the direction it is declared until one of the following occurs:

- Hit: A ray encounters an Atom in its direct path. The ray ends here and there is no exit point.

![Sample Hit](/assets/blackboxhit.png)

- Deflection

![Sample Deflection](/assets/blackboxdeflection.png)

- Reflection

![Sample Reflection](/assets/blackboxreflection.png)

- Double Deflection


![Sample Double Deflection](/assets/blackboxdoubledeflection.png)

- Miss

![Sample Miss](/assets/blackboxmiss.png)

- Detour

![Sample Detour](/assets/blackboxdetour.png)


Each Entry and Exit location count as a point. Per the [Wikipedia](https://en.wikipedia.org/wiki/Black_Box_(game)) page, "Hits and reflections therefore cost one point, while detours cost two points. When the seeker guesses the location of the atoms in the grid, each misidentified atom position costs penalty points: ten in the original Waddingtons rules, five in the Parker Brothers version and most computer editions." For this implementation, the penalty points are decided in accordance to the latter.
