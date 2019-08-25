def read_cats_file(filename):
    catslist = open(filename, "r").readlines()
    return catslist

def format_cats_list(cats_list):
    formatted_cats_list = []
    for cat in cats_list:
        formatted_cats_list.append(cat.lower())
    return formatted_cats_lists #Typo here will generate a stack trace

def print_cats(cats_list):
    formatted_cats_list = format_cats_list(cats_list)
    for cat in formatted_cats_list:
        print(cat)

def process_cats():
    cats_list = read_cats_file("cats.txt")
    print_cats(cats_list)

process_cats()
    

