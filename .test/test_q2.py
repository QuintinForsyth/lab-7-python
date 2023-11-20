import q2

twelve = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24],
    [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36],
    [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48],
    [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60],
    [0, 6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72],
    [0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84],
    [0, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96],
    [0, 9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108],
    [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],
    [0, 11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132],
    [0, 12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144],
]


def test_returns_empty_on_negative():
  assert [] == q2.make_times_table(
      -1), "Passing a negative number to make_times_table should yield []"


def test_0():
  assert [[0]] == q2.make_times_table(
      0), "Passing 0 to make_times_table should yield [ [0] ]"


def test_1():
  assert [[0, 0], [0, 1]] == q2.make_times_table(
      1), "Passing 1 to make_times_table should yield [ [0,0], [0,1] ]"


def test_2():
  assert [[0, 0, 0], [0, 1, 2], [0, 2, 4]] == q2.make_times_table(
      2), "Passing 2 to make_times_table does not yield the correct table"


def test_12():
  assert twelve == q2.make_times_table(
      12), "Passing 12 to make_times_table does not yield the correct table"


def test_123():
  actual = q2.make_times_table(123)

  ok = True
  message = ""

  assert len(
      actual
  ) == 124, f"There should be 124 rows in the table but there were {len(actual)}"

  for i in range(len(actual)):
    i_times = actual[i]
    assert len(
        i_times
    ) == 124, f"There should be 124 columns in each row of the table but in row {i} there were {len(i_times)}"

    for j in range(len(i_times)):
      expected = i * j
      assert expected == i_times[
          j], f"Your table at index ({i},{j}) should be {expected} but was {i_times[j]}"
