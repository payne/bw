import os

fa = os.listdir(".")
with open("index.html","w") as fp:
   for f in fa:
       print(f"<td><a href='{f}'><img src='{f}'/></a></td>", file=fp)

