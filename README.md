# StringToData
StringToData takes in string-formatted data (for example, "[10, 'hello world!', (3.6, 5)]") and converts it back into the proper
type of data (for example, a list containing 10, 'hello world!' and a tuple containing 3.6 and 5. StringToData currently works
for any combination of strings, ints, floats, lists, sets, and tuples, including empty containers.

StringToData currently does not support dictionary use.

Input data should be a single line in the format automatically applied when writing data to .txt files using the .write() method.
Functionality currently cannot be guaranteed if this format is not followed.

Functions Included in this Module:

strToData('string') - converts 'string' into the appropriate data type(s). Calls on all other functions during execution

strToNumber('string') - converts any number in string format (whole or decimal) to an int or float, whichever is appropriate. Ignores any characters after digits end (for example, '-12.34abcd' becomes -12.34).

strCutter(string',startCharacter) - determines when a string ends and returns the contents of the string. Not very useful by itself. Only works when the beginning quote is omitted. The startCharacter argument refers to whether the string began with an apostrophe or quotation mark. Doesn't work for triple apostrophes currently. Also ignores any characters after the string ends.

Please let me know if you encounter any bugs or issues!
