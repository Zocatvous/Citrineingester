## ABOUT ##
This ingester extracts the physical properties,SMILES/InChI keys and Database Tag, in an .xyz file placed in the subdirectory called "xyz", It then converts them into PIF files with the Database ID tag provided by the xyz file.

## REQUIREMENTS ##
Python 3.3

## SETUP ##

-Place the file "xyz_ingester.py" in a directory that you would like all of the output PIFs to end up.
-Place all the .xyz files that you would like to convert into a directory called "xyz" with the ingester.
-Run the ingester



##NOTES##

I made the naming convention for each of the output JSON objects the data tag for the chemical since I did not develop a method for converting the SMILES key into an IUPAC systematic name for the compound.  

This ingester extracts all data contained in each of the files in the sample set of 290 xyz files selected from the given database.



## HOW I WENT ABOUT THE PROBLEM ##

I learned alot Python coding during my work on this challenge.
I began working on this project by alotting several hours everyday to read and plan what methods I would create by creating a "diary" of sorts that documented my progress on each of the problems I encountered while creating my ingester.

I immediately became aware that I did not have the familiarity with the basics of object-oriented-programming or class object construction that I would need to complete the coding challenge. I immediately sought out a resource for learning the basics of Python coding that I was unfamiliar with. As I worked through excercizes in the book I found, I would come back to particular challenges that I encountered while working on the coding challenge and one by one I was able to slowly construct the methods that would become my ingester.




