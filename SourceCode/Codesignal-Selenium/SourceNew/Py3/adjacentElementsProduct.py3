def adjacentElementsProduct(z):
  l = -1e10
  for el in range(1, len(z)):
    if z[el-1] * z[el] > l:
      l = z[el-1] * z[el]
  return l
    
