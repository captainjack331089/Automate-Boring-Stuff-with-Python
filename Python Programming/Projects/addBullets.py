"""
When editing a Wikipedia article, you can create a bulleted list by putting each list item on its own line and placing a star in front. But say you have a really large list that you want to add bullet points to. You could just type those stars at the beginning of each line, one by one. Or you could auto- mate this task with a short Python script.
The bulletPointAdder.py script will get the text from the clipboard, add a star and space to the beginning of each line, and then paste this new text to the clipboard. For example, if I copied the following text (for the Wikipedia article “List of Lists of Lists”) to the clipboard:
             Lists of animals
             Lists of aquarium life
             Lists of biologists by author abbreviation
             Lists of cultivars
and then ran the bulletPointAdder.py program, the clipboard would then con- tain the following:
             * Lists of animals
             * Lists of aquarium life
             * Lists of biologists by author abbreviation
             * Lists of cultivars
This star-prefixed text is ready to be pasted into a Wikipedia article as a bulleted list.
"""