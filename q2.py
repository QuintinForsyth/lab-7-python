def make_times_table(n):
  # Check for precondition
  if n < 0:
      return []

  # Initialize the 2D list
  times_table = []

  # Populate the times table using nested loops
  for i in range(n + 1):
      row = []
      for j in range(n + 1):
          row.append(i * j)
      times_table.append(row)

  return times_table
