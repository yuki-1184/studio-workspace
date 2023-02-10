from create_html import *
from create_css import *

def main():
    args = []
    for i in range(1, len(sys.argv), 2):
        subset = []
        subset.append(int(sys.argv[i]))
        subset.append(int(sys.argv[i+1]))
        args.append(subset)
    print(args)

    # create html file
    create_html_file(args)
    
    # create css file
    create_css_file(args)

if __name__ == "__main__":
    main()