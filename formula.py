#!/usr/bin/env python3
import math
import statistics
def circle(s, n): # Circle operations: 1 = area, 2 = circumferance
  if (s == 1):
    return math.pi * n ** 2
  elif (s == 2):
    return math.pi * n * 2
  else:
    return "Invalid Parameters"
def triangle(s, n, m, l): # Triangle operations: 1 = Heron's Formula
  if (s == 1):
    semip = (n + m + l) / 2
    return math.sqrt(semip * (semip - n) * (semip - m) * (semip - l))
  else:
    return "Invalid Parameters"
def stats(s,a,b,*c): #Statistical operations: 1 = mean, 2 = median, 3 = mode, 4 = range
  if (s == 1):
    string = [a,b]
    for c in c:
      c_str = str(c)
      c_filtered = c_str.replace(")", "")
      c_filteredz = c_filtered.replace(",", "")
      c_final = c_filteredz.replace("(", "")
      string.append(float(c))
    return statistics.mean(string)
  elif (s == 2):
    string = [a,b]
    for c in c:
      c_str = str(c)
      c_filtered = c_str.replace(")", "")
      c_filteredz = c_filtered.replace(",", "")
      c_final = c_filteredz.replace("(", "")
      string.append(float(c))
    return statistics.median(string)
  elif (s == 3):
    string = [a,b]
    for c in c:
      c_str = str(c)
      c_filtered = c_str.replace(")", "")
      c_filteredz = c_filtered.replace(",", "")
      c_final = c_filteredz.replace("(", "")
      string.append(float(c))
    return statistics.mode(string)
  elif (s == 4):
    string = [a,b]
    for c in c:
      c_str = str(c)
      c_filtered = c_str.replace(")", "")
      c_filteredz = c_filtered.replace(",", "")
      c_final = c_filteredz.replace("(", "")
      string.append(float(c))
    return max(string) - min(string)
  else:
    return "Invalid Parameters"