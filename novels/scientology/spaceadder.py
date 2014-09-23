def addspace(fname):
  with open(fname, 'r') as f:
    parsed = []
    for line in f:
      if not line.strip().endswith('  '):
        parsed.append(line.strip() + "  \n")
      else:
        parsed.append(line)
  with open(fname, 'w') as f:
    for l in parsed:
      f.write(l)


addspace('1-1.md')
addspace('1-2.md')
addspace('2-1.md')
addspace('2-2.md')
