"""
File that contains some useful functions for natural language processing
"""

import re
import string

def clean(text, numbers = True, non_ascii = True):
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
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text) # removes punctuation

    if numbers:
        text = re.sub('\w*\d\w*', '', text) # removes numbers

    if non_ascii:
        text = re.sub(r'[^\x00-\x7F]+',' ', text)

    text = re.sub('\s+',' ',text)
    return text
