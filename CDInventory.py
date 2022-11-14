#------------------------------------------#
# Title: CDInventory.py
# Desc: Inventory of CDs that user can add to, delete from or display
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# PBhamidipati, 2022-Nov-11, Edited File to add functionality to add, write, read and display menu items, including code to read and write date from list to file and vice versa
# PBhamidipati, 2022-Nov-12, Edited File to use dictionaries, making the data structure from a list of lists to list of dictionaries 
# PBhamidipati, 2022-Nov-13, Edited File to add delete option to the menu and its functionality; impacts ln#19, #22
#------------------------------------------#

# Declare variables

strChoice = '' # User input
lstTbl = []
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('\nWrite, Delete or Read file data.')
while True:
    print('\n[a] to add data to list\n[w] to write data to file\n[r] to read data from file')
    print('[d] to display data from file\n[e] to delete entry from file\n[exit] to quit the program')
    strChoice = input('Choose and type a, w, r, d, e or exit: ').lower()  # convert choice to lower case at time of input
    print('\n\n')
    
    strChoice = strChoice.strip()
    
    if strChoice == 'exit':
        break
    
    if strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        dictRow = {} # initialise variable to hold dictionary data
        
        # Ask user to input data and store it as a dictionary
        dictRow['Artist'] = str(input('Enter the CD\'s artist: ')) # ask Artist Name
        dictRow['Title'] = str(input('Enter CD title\'s name: ')) # ask CD Title
        
        # Add data to list in memory
        lstTbl.append(dictRow)
    
    elif strChoice == 'w': 
        
        # List to File
        # Write from in-memory list to file. (convert dictionary to string)
        for row in lstTbl:
            strRow = ''
            for key in row:
                strRow += row[key] + ','
            strRow = strRow[:-1] + '\n'
            objFile = open(strFileName, 'a')
            objFile.write(strRow)
            objFile.close()
            
    elif strChoice == 'r':
        
        # File to read
        objFile = open(strFileName, 'r')
        
        # Read the file line-by-line into in-memory list. (create back the dictionary type)
        for row in objFile:
            rdStrRow = row.strip().split(',')
            createDictRow = {'Artist': str(rdStrRow[0]), 'Title': str(rdStrRow[1])}
            lstTbl.append(createDictRow)
        objFile.close()
            
    elif strChoice == 'd':
        
        # Display data
        print('Artist, Title')
        
        # Display the data to the user.
        for row in lstTbl:
            print(row) # observation: if data is displayed before closing and restarting the program, then data maybe duplicated based on order of reading and displaying
        
    elif strChoice == 'e':
	
        # Get the name of Artist from user, whose entry is to be deleted
        delArtist = str(input('Enter Artist\'s name for entry deletion: '))

        # File to read
        objFile = open(strFileName, 'r')
        detInd = 0 # initialise a counter to determine the index of the entry to be deleted

        # Read the file line-by-line into in-memory list. (create back the dictionary type)
        for row in objFile:
            rdStrRow = row.strip().split(',')
            createDictRow = {'Artist': str(rdStrRow[0]), 'Title': str(rdStrRow[1])}
            lstTbl.append(createDictRow)
        objFile.close()
	  
        for item in lstTbl:      
            if delArtist == item['Artist']:
                break
            else:
                detInd +=1
            
        if detInd < len(lstTbl): 
            del lstTbl[detInd]
            objFile = open(strFileName, 'w') # so the file is overwritten
            objFile.truncate()

            for row in lstTbl:
                strRow = ''
                for key in row:
                    strRow += row[key] + ','
                strRow = strRow[:-1] + '\n'
                objFile.write(strRow)
            objFile.close()
    
    else:
        print('Please choose one of a, w, r, d, e or exit!')

