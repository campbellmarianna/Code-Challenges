for a in range(1, 50):
  for b in range(1, 50):
    for c in range(1, 50):
      for d in range(1, 50):
        if a**3+b**3 == c**3+d**3:
          print(f"a: {a}, b: {b}, c: {c}, d: {d}")
