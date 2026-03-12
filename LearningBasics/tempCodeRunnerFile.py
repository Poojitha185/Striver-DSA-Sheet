for i in range(1,6):
    if i%2!=0:
      h=1
    else:
      h=0
    for j in range(1,i+1):
      print(h,end="")
      if h==0:
        h=1
      else:
        h=0
    print()