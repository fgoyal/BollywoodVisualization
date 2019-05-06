# BollywoodVisualization
Visualization of different Bollywood actors based on the number of movies they appeared in per year on a timeline from 1920-2017. It allows users to also see the number of times different actors have worked with each other before.

## Usage
1) Clone the repository 
2) Warning: It is critical that the python script runs from this folder because this is where the data set is hosted. 
3) Once in the folder directory, run the command ` python3 data.py `
4) Input the name(s) that you want to visualize. Separate names by commas. Click enter.
5) View Graph

## Examples
![amitabh bachchan](/Examples/AmitabhBachchan.png)
![shahrukhkhan and kajol](/Examples/ShahrukhKhan_Kajol.png)
![shahrukh khan, amitabh bachchan, and aishwarya rai](/Examples/AishwaryaRai_AmitabhBachchan_ShahrukhKhan.png)

## How to Add More Columns of People
To include data for another column, like music directors, follow the directions below in the file `data.py`.

1) Add the line `data['ColumnName'] = data['ColumnName'].str.replace(' ',',')` after line 12
2) Add ` + "," + data["ColumnName"] ` to the end of line 13 - `data['People'] = data['Director'] + "," + data["Cast"]`. Add any new columns to this line with a similar format.
3) Now if you run `data.py` following the above instructions, it will also use the people from the new column.

For example - 

To add a column with the title 'MusicalDirectors', the code would be 

`data['MusicalDirectors'] = data['MusicalDirectors'].str.replace(' ',',')

data['People'] = data['Director'] + "," + data["Cast"] + "," + data["MusicalDirectors"]`

and so on.
