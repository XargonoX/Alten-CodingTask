# Alten-CodingTask
## MERGE-Function
### Preconditions

- working python 3.x
- installed numpy package (install with pip3 install numpy)

### How to Use
The Script reads the Interval data from an text file which is specified with the argument **-i**.

The merge result is is written to the file which is specified with the argument **-o**.

You can find an example input file in the **exampleData** folder.


- Start the Script with: **merge.py -i INPUTFILE -o OUTPUTFILE**
- To get help type: **merge.py -h**


### Code Runtime
##### Bestcase
In the bestcase the function has a runtime of O(n) if all intervals are overlapping.
##### Worstcase
In the worstcase the function has a runtime of O(n^2) if non of the intervals are overlapping.

### Memory Consumption
The memory consumption of the program depends on the quantity of data read.
Through the deletion of computed intervals the memory consumption of the program does not raise over the lifetime of the program.

### Robustness
To Ensure the robustness of this Script there should be more information about the way the data gets into the Program.
If the are other ways than a file read(maybe multiple files or database connection), and the data is larger that the memory of the running machine
 i would add a logic which pause the reading of the data, merge the already read an read the rest of the data and continue with it.
 
 If this is also not enought, cause the merged data is grater that the memory the merged data itself has to be outsourced to file or an database and has to be read in again after the rest of the inputdata is computed. In the end the program then has to merge the merged data. 