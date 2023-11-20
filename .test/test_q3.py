import util

import conway.q3 as q3
import conway.world as cworld


def test_get_world():
  cworld.world = """.....\n..*..\n..*..\n..*..\n....."""

  world = q3.get_world()
  assert isinstance(world,
                    list), "get_world must return a list but yours doesn't"

  for row in world:
    assert isinstance(
        world[0], list
    ), "get_world must return a list of lists but not all items in the list returned from your function are lists"

  for row in world:
    for item in row:
      assert item == '.' or item == '*', "get_world must return a list of lists of '.' or '*' characters, but yours includes other characters"

  assert len(world) == 5 and len(
      world[0]
  ) == 5, "The world returned from get_world must be the same size as the string defined in the world module; the size of your returned world is not correct"

  cworld.world = """.*.\n*.*\n.**"""
  world = q3.get_world()
  assert world == [
      ['.', '*', '.'], ['*', '.', '*'], ['.', '*', '*']
  ], "The world returned from your get_world does not always match the one defined in the world module"


def test_count_live_neighbours_for_dead_world():

  world = [['.']]

  assert q3.count_live_neighbours(
      world, 0, 0
  ) == 0, "A world with a single cell should return a count of 0 live neighbours"

  world = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]

  for i, row in enumerate(world):
    for j, cell in enumerate(row):
      assert q3.count_live_neighbours(
          world, i, j
      ) == 0, "A world with no live cells should return a count of 0 live neighbours for any location"


def test_count_live_neighbours_for_full_world():
  world = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]

  assert q3.count_live_neighbours(
      world, 1, 1
  ) == 8, "A 3x3 world with all live cells should return a count of 8 live neighbours for the middle location"


def test_count_live_neighbours_corners():
  world = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]

  assert q3.count_live_neighbours(
      world, 0, 0
  ) == 3, "A 3x3 world with all live cells should return a count of 3 live neighbours for the corner locations"
  assert q3.count_live_neighbours(
      world, 0, 2
  ) == 3, "A 3x3 world with all live cells should return a count of 3 live neighbours for the corner locations"
  assert q3.count_live_neighbours(
      world, 2, 0
  ) == 3, "A 3x3 world with all live cells should return a count of 3 live neighbours for the corner locations"
  assert q3.count_live_neighbours(
      world, 2, 2
  ) == 3, "A 3x3 world with all live cells should return a count of 3 live neighbours for the corner locations"


def test_count_live_neighbours_noncorner_edges():
  world = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]

  assert q3.count_live_neighbours(
      world, 0, 1
  ) == 5, "A 3x3 world with all live cells should return a count of 5 live neighbours for non-corner edge locations"
  assert q3.count_live_neighbours(
      world, 1, 0
  ) == 5, "A 3x3 world with all live cells should return a count of 5 live neighbours for non-corner edge locations"
  assert q3.count_live_neighbours(
      world, 2, 1
  ) == 5, "A 3x3 world with all live cells should return a count of 5 live neighbours for non-corner edge locations"
  assert q3.count_live_neighbours(
      world, 1, 2
  ) == 5, "A 3x3 world with all live cells should return a count of 5 live neighbours for non-corner edge locations"


def test_count_live_neighbours_4():
  world = [['*', '.', '*'], ['.', '*', '.'], ['*', '.', '*']]

  assert q3.count_live_neighbours(
      world, 1, 1
  ) == 4, "The center cell of the following world should have a live neighbour count of 4 but yours does not: \n*.*\n.*.\n*.*"


def test_count_live_neighbours_3():
  world = [['*', '.', '.'], ['*', '*', '*'], ['.', '.', '.']]

  assert q3.count_live_neighbours(
      world, 1, 1
  ) == 3, "The center cell of the following world should have a live neighbour count of 3 but yours does not: \n*..\n***\n..."


def test_count_live_neighbours_2():
  world = [['.', '*', '.'], ['.', '.', '.'], ['.', '*', '.']]

  assert q3.count_live_neighbours(
      world, 1, 1
  ) == 2, "The center cell of the following world should have a live neighbour count of 2 but yours does not: \n.*.\n...\n.*."


def test_count_live_neighbours_1():
  world = [['.', '.', '*'], ['.', '.', '.'], ['.', '.', '.']]

  assert q3.count_live_neighbours(
      world, 1, 1
  ) == 1, "The center cell of the following world should have a live neighbour count of 2 but yours does not: \n..*\n.*.\n..."


def test_count_live_neighbours_5():
  world = [['*', '*', '*'], ['.', '*', '.'], ['*', '.', '*']]

  assert q3.count_live_neighbours(
      world, 1, 1
  ) == 5, "The center cell of the following world should have a live neighbour count of 4 but yours does not: \n***\n.*.\n*.*"


def test_count_live_neighbours_6():
  world = [['*', '*', '*'], ['.', '*', '*'], ['*', '.', '*']]

  assert q3.count_live_neighbours(
      world, 1, 1
  ) == 6, "The center cell of the following world should have a live neighbour count of 4 but yours does not: \n***\n.**\n*.*"


def test_count_live_neighbours_7():
  world = [['*', '*', '*'], ['*', '*', '.'], ['*', '*', '*']]

  assert q3.count_live_neighbours(
      world, 1, 1
  ) == 7, "The center cell of the following world should have a live neighbour count of 4 but yours does not: \n***\n**.\n***"


def test_evolve_returns_valid_2d_list():
  world = [['.', '.', '.'], ['.', '*', '.'], ['.', '.', '.']]

  next_world = q3.evolve(world)

  assert next_world is not world, "evolve must not return a reference to the same list it was given (yours does)"

  assert isinstance(
      next_world, list
  ), f"evolve must return a list but yours returns a {type(next_world)}"
  for row in next_world:
    assert isinstance(
        row, list
    ), f"evolve must return a list of lists, but at least one row in your returned list is a {type(row)}"

  assert len(
      next_world
  ) == 3, f"The evolved world should have 3 rows but yours has {len(next_world)}"

  for row in next_world:
    assert len(
        row
    ) == 3, f"The evolved world should have 3 rows of 3 items but at least one of your rows has {len(row)} items"
    for cell in row:
      assert cell in [
          '.', '*'
      ], f"The evolved world should have only '.' and '*' characters but yours has a '{cell}'"


def test_evolve_underpopulation():
  world = [['.', '.', '.'], ['.', '*', '.'], ['.', '.', '.']]

  next_world = q3.evolve(world)
  assert next_world[1][
      1] == '.', "The center cell of the following world should die, but it doesn't using your evolve function:\n...\n.*.\n..."

  world = [['.', '.', '.'], ['.', '*', '*'], ['.', '.', '.']]

  next_world = q3.evolve(world)
  assert next_world[1][
      1] == '.', "The center cell of the following world should die, but it doesn't using your evolve function:\n...\n.**\n..."


def test_evolve_overpopulation():
  world = [['.', '*', '.'], ['*', '*', '*'], ['.', '*', '.']]

  next_world = q3.evolve(world)
  assert next_world[1][
      1] == '.', "The center cell of the following world should die, but it doesn't using your evolve function:\n.*.\n***\n.*."

  world = [['.', '*', '.'], ['*', '*', '*'], ['.', '*', '*']]

  next_world = q3.evolve(world)
  assert next_world[1][
      1] == '.', "The center cell of the following world should die, but it doesn't using your evolve function:\n.*.\n***\n.**"

  world = [['*', '*', '.'], ['*', '*', '*'], ['.', '*', '*']]

  next_world = q3.evolve(world)
  assert next_world[1][
      1] == '.', "The center cell of the following world should die, but it doesn't using your evolve function:\n**.\n***\n.**"

  world = [['*', '*', '.'], ['*', '*', '*'], ['*', '*', '*']]

  next_world = q3.evolve(world)
  assert next_world[1][
      1] == '.', "The center cell of the following world should die, but it doesn't using your evolve function:\n**.\n***\n***"

  world = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]

  next_world = q3.evolve(world)
  assert next_world[1][
      1] == '.', "The center cell of the following world should die, but it doesn't using your evolve function:\n***\n***\n***"


def test_evolve_reproduction():
  world = [['.', '*', '.'], ['*', '.', '*'], ['.', '.', '.']]

  next_world = q3.evolve(world)
  assert next_world[1][
      1] == '*', "The center cell of the following world should change from dead to live, but it doesn't using your evolve function:\n.*.\n*.*\n..."


def test_evolve_stable():
  world = [['.', '*', '.'], ['*', '*', '.'], ['.', '.', '.']]

  next_world = q3.evolve(world)
  assert next_world[1][
      1] == '*', "The center cell of the following world should stay live, but it doesn't using your evolve function:\n.*.\n**.\n..."

  world = [['.', '*', '.'], ['*', '*', '.'], ['.', '.', '*']]

  next_world = q3.evolve(world)
  assert next_world[1][
      1] == '*', "The center cell of the following world should stay live, but it doesn't using your evolve function:\n.*.\n**.\n..*"
