import cleaner
import inout

def main():
    x= inout.read()
    y= cleaner.clean_types(x)
    z=cleaner.clean_missing(y)
    w=cleaner.clean_double(z)
    inout.saver()       