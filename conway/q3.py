import conway.world as world

# Answer the Part 3a questions here:
#
#
#
#


def get_world():
  """Returns a non-ragged 2d list representing the starting state of
     a game of Conway's Game of Life
     The individual elements are one of:
     - '.' (an empty space), or 
     - '*' (a live cell)
  """
  # Start with the world string from the world module
  world_str = world.get_world_str()

  # TOOD: build the world list from the contents of world_str
  return [['.', '*', '.'], ['.', '.', '*'], ['*', '.', '.']]



def count_live_neighbours(world, x, y):
  """Returns the number of live neighbours of the cell at (x, y) 
    in the given world.
    
    world must be a non-ragged 2d list of . or * characters
    (* represents a live cell)
    x and y must be integers that are valid indices of world
  """
  # Calculate the width and height of the world
  height = len(world)
  width = len(world[0])

  # TODO: implement this correctly
  return 0



def evolve(world):
  """Returns the next state of the world given the current state,
    according to the rules of Conway's Game of Life.
    world must be a non-ragged 2d list of . or * characters.

    Rules:
    1. Underpopulation: 
          Any live cell (*) with fewer than 2 live neighbours dies (.)
    2. Stable: 
          Any live cell (*) with 2 or 3 live neighbours lives (*)
    3. Overpopulation: 
          Any live cell (*) with more than 3 live neighbours dies (.)
    4. Reproduction: 
          Any dead cell (.) with 3 live neighbours becomes a live cell (*)
    """

  # TODO: implement this correctly
  return world