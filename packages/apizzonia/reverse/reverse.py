def reverse(args):
  inp = args.get("input", "")
  out = "reverse"
  if inp != "":
    out = inp[::-1]
  return { "output": out }
