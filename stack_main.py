'''
generic stack overflow comments:

what have you tried so far ?
the question needs sufficient code for a minimal reproducible example:
https://stackoverflow.com/help/minimal-reproducible-example

too much code, please reduce to this:
https://stackoverflow.com/help/minimal-reproducible-example

how to ask a good question:
https://stackoverflow.com/help/how-to-ask

Why should I not upload images of code?
https://meta.stackoverflow.com/questions/285551/why-should-i-not-upload-images-of-code-data-errors-when-asking-a-question/285557#285557


avoid wildcard imports:
https://stackoverflow.com/questions/73698351/is-anyone-know-how-to-connect-tkinter-webcam-to-yolov5/73712541#73712541


post the code and not the pictures of code.
Users need to be able to replicate the problem quickly, 
which text allows for (and pictures do not).
https://stackoverflow.com/help/how-to-ask

'''


# %%

# import speech_recognition as sr

import pandas as pd

print('hello world')
print('hi there')

def main():
    ''' main function '''
    read_file()
    return

def read_file():
    '''
    reads a file
    '''
    df = pd.read_csv('test.csv')
    print(df)

    return

if __name__=='__main__':
    # run as the main program guard
    main()

