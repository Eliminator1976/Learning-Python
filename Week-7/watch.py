#<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0?si=ayeDTUFrkiJwZtVe" 
#title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
#referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

import re
import sys
def main():
    print(parse(input("HTML: ")))

def parse(s):
    if matches := re.search(r"src=\"(?:https|http)://(?:www\.|)youtube\.com/embed/([^\"]+)",s, re.IGNORECASE):
        return f"https://youtu.be/{matches.group(1)}"

if __name__ == "__main__":
    main()