"""
File that contains some useful functions for natural language processing
"""

import re
import string

import re
import string

def clean(text, numbers = True, non_ascii = True, stop = False):
    """
    Function to clean text

    Dependencies:
    -------------

    import re
    import string

    Attributes:
    -----------

    text : str
        text to be cleaned

    numbers (True) : bool
        boolean to determine whether to remove numbers (True) or not (False)

    non_ascii (True) : bool
        boolean to determine whether to remove non-ascii characters (True) or not (False)

    """
    text = text.lower() # make text lower case


    # this needs fixing
    text = re.sub(' +', ' ', text)

    if numbers:
        text = re.sub('\w*\d\w*', '', text) # removes numbers

    if non_ascii:
        text = re.sub(r'[^\x00-\x7F]+',' ', text)    # remove non_ascii chars

    if not stop:

        stop_words = set(stopwords.words('english'))

        text = ' '.join([w for w in text.split() if not w in stop_words])

    text = re.sub('[%s]' % re.escape(string.punctuation), '', text) # removes punctuation



    return text
