import os
import sys

top_html_string = """
<!DOCTYPE html>
<html lang="en">
<head>
    <!-- <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0"> -->
    <title>Document</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <!-- <script src="script.js"></script> -->
    <div class="center">
"""

texts = ["", "Power", "Testimonials", "Discover what the creaters and customers who use technology think about us. Discover what the creaters and customers who use technology think about us. Discover what the creaters and customers who use technology think about us. Discover what the creaters and customers who use technology think about us."]

def create_html_content(input):
    space_count = 0
    text_count = 0
    html_contents = []
    for line in input:
        if line[0] == 0:
            space_count += 1
            html_content = """
        <div class="container">
            <div class="left no-text">{0} {1}</div>
            <div class="right">
                <p class="space{2}"></p>
            </div>
        </div>
            """.format(line[0], line[1], space_count)
            html_contents.append(html_content)
        else:
            text_count += 1
            html_content = """
        <div class="container">
            <div class="left text">{0} {1}</div>
            <div class="right">
                <p class="text{2}">{3}</p>
            </div>
        </div>
            """.format(line[0], line[1], text_count, texts[text_count])
            html_contents.append(html_content)
        
    return "".join(html_contents)

bottom_html_string = """
    </div>
</body>
</html>
"""

# Create the program source code 
def pp_program(input):
    
    # create html file content
    html_content_str = create_html_content(input)
    
    # join content with header and footer
    return "".join([top_html_string, html_content_str, bottom_html_string])

# Write a string to a file (helper function)
def write_str_to_file(str_, fname):
    f = open(fname, 'w')
    f.write(str_)
    f.close()
    
def create_html_file(args):
    # create html source code
    html_source = pp_program(args)
    
    # write it to file (index.htm;)
    write_str_to_file(html_source, "index.html")

    