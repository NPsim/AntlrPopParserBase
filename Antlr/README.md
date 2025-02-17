# Only continue if you want to rebuild the Antlr packages!

Put your antr.jar in the same folder as this readme. I used antlr-4.13.2-complete.jar
Download it at https://www.antlr.org/download.html

Then build ANTLR libraries using (change antlr jar file name as needed):

java -jar .\antlr-4.13.2-complete.jar -Dlanguage=Python3 -o output .\pop.g4 -no-listener -visitor