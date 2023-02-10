import os
import sys

top_css_string = """
.center {
  margin: auto;
  width: 60%;
  border: 3px solid #73AD21;
  padding: 10px;
}

.container {
    display: grid;
    grid-template-columns: 1fr 3fr;
    grid-auto-rows: 1fr;
}

.left {
    display: flex;
    margin-right: 20px;
}

.no-text {
    align-items: center;
    justify-content: center;
    font-size: 18px;
    opacity: 0.5;
    border-right: 1px dashed black;
}

.text {
    align-items: center;
    justify-content: center;
    font-size: 22px;
    opacity: 1;
    border-right: 1px solid black;
}
"""

texts = ["", "Power", "Testimonials", "Discover what the creaters and customers who use technology think about us. Discover what the creaters and customers who use technology think about us. Discover what the creaters and customers who use technology think about us. Discover what the creaters and customers who use technology think about us."]

def create_css_content(input):
    space_count = 0
    text_count = 0
    space_contents = []
    text_contents = []
    comment_space = "/* Spaces between the texts (font-size = 0) */"
    comment_text = "/* Text contents (font-size, font-weight are given) */"
    for line in input:
        if line[0] == 0:
            space_count += 1
            function = ".space" + str(space_count) + " {"
            content = "    margin: {0}px;".format(line[1])
            close_function = "}"
            
            joined = "\n".join([function, content, close_function])
            space_contents.append(joined)
        else:
            text_count += 1
            function = ".text" + str(text_count) + " {"
            content = "    margin: 0px;\n    font-weight: {0};\n    font-size: {1}px;\n    line-height: 1em;".format(line[0]*100, line[1])
            close_function = "}"
            
            joined = "\n".join([function, content, close_function])
            text_contents.append(joined)
        
    return "\n\n".join([comment_space, "\n".join(space_contents), comment_text, "\n".join(text_contents)])


# Create the program source code 
def pp_program(input):
    
    # create css file content
    css_content_str = create_css_content(input)
    
    # join content with header and footer
    return "\n".join([top_css_string, css_content_str])

# Write a string to a file (helper function)
def write_str_to_file(str_, fname):
    f = open(fname, 'w')
    f.write(str_)
    f.close()

def create_css_file(args):
    # create html source code
    css_source = pp_program(args)
    
    # write it to file (index.htm;)
    write_str_to_file(css_source, "style.css")

    