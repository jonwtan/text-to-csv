# text-to-csv
Converts a two-column data textfile into a two-column csv

This python script converts a two-column data textfile with entries separated by spaces, into a two-column .csv file with entries separated by commas. I made this as an exercise to be specifically used on a datafile of suburbs & corresponding postcodes/zipcodes in the state of Victoria, Australia.

Used without any code changes (except for the names of the input textfile and output csv file), one could use this on any textfile with two columns; where the first column is a digit, and the second column is a string. Examples include student ID numbers & student name, item price & item name, country code & country name, etc.


In the folder, are 3 files;
1) The .py script itself
2) The input file 'listofpostcodes.txt' as an example.
3) The output file 'vicpostcodes.csv' as an example of what the .py script will produce

Running the script converts the textfile....

3067 Abbotsford 
3040 Aberfeldie 
3825 Aberfeldy 
3714 Acheron 
3352 Addington 
3962 Agnes
3231 Aireys Inlet
....

into this .csv file;

3067, Abbotsford 
3040, Aberfeldie 
3825, Aberfeldy 
3714, Acheron 
3352, Addington 
3962, Agnes 
3231, Aireys Inlet 
....
