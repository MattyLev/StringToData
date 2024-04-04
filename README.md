# StringToData
StringToData takes in string-formatted data (for example, "[10, 'hello world!', (3.6, 5)]") and converts it back into the proper
type of data (for example, a list containing 10, 'hello world!' and a tuple containing 3.6 and 5. StringToData currently works
for any combination of strings, ints, floats, lists, sets, and tuples, including empty containers.

StringToData currently does not support dictionary use.

Input data should be in the format automatically applied when writing data to .txt files using the .write() method.
Functionality currently cannot be guaranteed if this format is not followed.
