Assignment 2
===================

----------

Synopsis
------------
The following folder contains the **code** and **output** files for Assignment 2 submission.
For first part, we are supposed to prove Zipf's law using the nltk packages and for second part, we are supposed to categorize and segregate the json files and extract information from those json files into a single file.

File **Assingment2_Question1** contains *code* for Zipf's law proof with conclusion. FIle **word_rank.csv** is the *output* csv file with *Word, Rank, Frequency* and **word_rank.xlsx** is exactly same as *word_rank.csv* plus a **log-log plot**.

File **Assingment2_Question2** contains *code* for both **Part 1** and **Part 2** 
Folder structure is under **Data Processed** folder. The hierarchy is **Data Processed / Country / City / Term / Category / FileName.json**
File **restaurant_timings.csv** contains the output in the format as mentioned later in this document.

----------

Question 1
---------
#### Description
Read about Zipf's law from Wikipedia and also seen the YouTube video shared by professor. Proved the Zipf's law using the text from **Gutenberg** package. Plotted a log-log plot and a bar plot using **matplotlib** and in **excel file** shared as output

> **Steps followed:**
> 
> - Used **glob** to read all the *.txt* files from Gutenberg corpus in a loop
> - Created a single **list** containing all the words in Gutenberg corpus
> - Converted all the words to **lower case**
> - Wrote a **function** to *remove all the punctuation*
> - Wrote a **lambda expression** to *remove all the numbers*
> - Called the **lambda expression** to remove numbers **from function**, that way, got rid of all the punctuations and all the numbers in one function call
> - Wrote a **lambda expression** to *remove all the stop words* but **didn't use this** lambda expression
> - Created a **dictionary** and added all these *words as keys* and their *frequencies as values*
> - **Sorted** the dictionary according to the *values* i.e. the **word frequencies** and sorted all the words **alphabetically** having *same frequencies*
> - Wrote a **function** to allocate *ranks* to words in which used a simple **for loop** to assign *ranks* to all words
> - Created a **list** of string containing **word, rank, frequency** as each element
> - Created a **word_rank.csv** file. Added *title row* to it and added all the details in a sorted order
> - Created a **log-log plot** in *excel* file
> - **Read** the *csv file* back to jupyter notebook and created a list of *word rank and word frequency* in each row
> - Using ```plt.loglog()``` function of **matplotlib**, drafted a **log-log** plot with *frequency on Y axis* and *word rank on X axis*
> - Using ```plt.bar()``` function of **matplotlib**, drafted a **bar**  plot with *frequency on Y axis* and *word on X axis*
> - **Conclusion** at the end proving the **zipf's law**
#### Conclusion 
**Did not call the lambda function to remove stop words as we need all the stopwords in this example**
**Zipf's law says *the*,*of*,*I* are the top three words used in day to day lives and top 25 words are almost all stop-words**
**According to the log-log and bar plot, if can be proved that the Zipf's law holds true and the top 20% of words are used 80% of the time**
**The *rank'ed* word is *1/rank times* used word in day to day life**

----------

Question 2
---------
### Part 1
#### Description
Created the folder structure with data_processed as the base folder. Used *relative path* to create folder structure using ```__file__``` in-build variable. Wrote function to create folder structure and to write the data to json file with same name. Didn't use name field to create name of file as it could have been duplicated. The folder structure created is **Country > City > Type > Category > File**. 

> **Steps followed:**
> 
> - Wrote a *function* to create parent folder **Data Processed**
> - Used **relative path** to create *Data Processed*. Using **```__file__```** variable, get the current folder's path and created the *Data Processed* at this location
> - Created *Data Processed* **only if it does not exist**
> - Used **```mkdir```** command to create folders
> - Wrote *function* to create the folder hierarchy with input parameters as **country**, **city**, **term** and **category** and returned the created folders path
> - If folder is already present, then returned the path
> - Wrote a *function* to **write data to json** file with *file name* and *json data* as input parameters and *no return *
> - Used **glob** to read all the *.json* files from *Data* folder in a loop
> - Separated file name using **```os.path.basename```** command
> - Identified **categories** used for each restaurant and created *sub folders* accordingly and placed the restaurant in *all the categories* mentioned in its json file
> - Removed **extra spaces** in **city** names. *For ex. New(space)York and New(space)(space)York are to be identified as same city*
> - The folder structure created is **Data Processed / Country / City / Term / Category / File.json**
> - Called function to write json data to above created folder and populate the structure

#### Output Format
The folder structure/hierarchy looks something like this:
**Data Processed / Country / City / Term / Category / FileName.json**

### Part 2
#### Description
Read all json files and used *only restaurants* to get timing for their operations. Created a *dummy row* in order to prevent code from crashing and to write **NA** wherever the restaurant **time is not mentioned**.
Also as mentioned for **Bonus**, separated out the hours and minutes for each restaurants opening and closing time.

> **Steps followed:**
> 
> - Wrote a **function** to add *each restaurant's* data for *each day* as a separate row in a list
> - Wrote a **function** to write data to *.csv* file with *file name* and *file data* as input parameters
> - Used **utf-8** encoding as some of the restaurants have names which cannot be represented in *English* language 
> - Used  ```escapechar``` variable while writing data to *.csv* file because of the presence of **utf-8 ** encoded text in files
> - Used title row in *.csv* file
> -  Used **glob** to read all the *.json* files from *Data* folder in a loop
> - Filtered out only **restaurants** jsons
> - Used **try-except** block to nullify the risk of crashes in case any restaurant doesn't have **hours** and **open** as field parameters mentioning its operations timing
> - If the values are not present, populate **NA**
> - Populate the data in a *single list* with operation timing for different days of same restaurant as different rows
> - Separated out the **hours** and **minutes** for each restaurant
> - Call function to write the data to *.csv* file

#### Output Format
The data in final csv file looks something like this:
Name of Restaurant | City | Country Code | Day of week | Start Time Hour | Start Time Minutes | End Time Hour | End Time Minutes

1 Abercrombie Lane | Sydney | AU | 0 | 07 | 30 | 15 | 30

1 Abercrombie Lane | Sydney | AU | 1 | 07 | 30 | 15 | 30

1 Abercrombie Lane | Sydney | AU | 2 | 07 | 30 | 15 | 30

1 Abercrombie Lane | Sydney | AU | 3 | 07 | 30 | 15 | 30

1 Abercrombie Lane | Sydney | AU | 4 | 07 | 30 | 15 | 30

\#1 Chicken Rice & Seafood | Houston | US | 0 | 10 | 30 | 20 | 30

\#1 Chicken Rice & Seafood | Houston | US | 1 | 10 | 30 | 20 | 30

\#1 Chicken Rice & Seafood | Houston | US | 2 | 10 | 30 | 20 | 30

\#1 Chicken Rice & Seafood | Houston | US | 3 | 10 | 30 | 20 | 30

\#1 Chicken Rice & Seafood | Houston | US | 4 | 10 | 30 | 20 | 30

\#1 Chicken Rice & Seafood |Houston | US | 5 | 10 | 30 | 20 | 30

140 Perth | Perth | AU | NA | NA | NA | NA | NA


----------