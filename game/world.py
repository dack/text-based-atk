_world = {}
starting_position = (0, 0)

def tile_exists(x, y):
        """Returns the tile at the given coordinates or None if there is no tile.
        :param x: the x-coordinate in the worldspace
        :param y: the y-coordinate in the worldspace
        :return: the tile at the given coordinates or None if there is no tile
        """
        return _world.get((x, y))


def load_tiles():
    """Parses a file that describes the world space into the _world object"""

    with open('resources/map.txt') as f:
        lines = f.read().replace('\r','\n')
    with open('resources/map.txt','w') as f1:
        f1.write(lines)
    with open('resources/map.txt', 'r') as f2:
        rows = f2.readlines()

    x_max = len(rows[0].split('\t'))
    for y in range(len(rows)):
        cols = rows[y].split('\t')
        for x in range(x_max):
            tile_name = cols[x].replace('\n', '')
            #print(cols[x], tile_name , y, x, x_max)
            if tile_name == 'StartingRoom':
                global starting_position
                starting_position = (x, y)
            _world[(x, y)] = None if tile_name == '' else getattr(__import__('tiles'), tile_name)(x, y)
