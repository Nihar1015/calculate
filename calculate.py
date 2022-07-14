from tokenize import Name


star_gravity = []

for index, name in enumerate(Name):
  gravity = (float(Mass[index])*5.972e+24) / (float(Radius[index])*float(Radius[index])*6371000*6371000) * 6.674e-11
  star_gravity.append(gravity)