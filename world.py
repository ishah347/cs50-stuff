__author__ = 'Imran Shah'

"""Establish empty _world object"""
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
    with open('resources/map.txt', 'r') as f:
        rows = f.readlines()
    """Go through every line and column in the map.txt value to isolate each room"""
    x_max = 0
    for row in rows:
        if len(row.split('\t')) > x_max:
            x_max = len(row.split('\t'))
    for y in range(len(rows)):
        cols = rows[y].split('\t')
        for x in range(x_max):
            try:
                tile_name = cols[x].replace('\n', '')
            except IndexError:
                break
            """Establish StartingRoom as entry room"""
            if tile_name == 'StartingRoom':
                global starting_position
                starting_position = (x, y)
            _world[(x, y)] = None if tile_name == '' else getattr(__import__('tiles'), tile_name)(x, y)


