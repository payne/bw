import os

def make_page(f):
    fn = f.split(".")[0]
    page_file_name = "p/" + fn + ".html"
    with open(f"{page_file_name}","w") as fp:
        print(f"<html><body><img src='../{f}'/><p><a href='../index.html'><h1>index</h1></a></body></html>", file=fp)
    return page_file_name

def main():
    fa = os.listdir(".")
    row = 0
    with open("index.html","w") as fp:
        print("<html><body><table><tr>", file=fp)
        for f in fa:
            if "webp" not in f:
                continue
            page_file_name = make_page(f)
            print(f"<td width='50%'><a target='_blank' href='{page_file_name}'><img src='{f}'/></a></td>", file=fp)
            row += 1
            if (row % 2 == 0):
                print("</tr><tr>", file=fp)
        print("</tr></table></body></html>", file=fp)



if __name__ == "__main__":
    main()

