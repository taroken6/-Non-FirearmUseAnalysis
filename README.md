# -Non-FirearmUseAnalysis

Creates a nested list of Firearm/Nonfirearm use in each state sorted in descending order.

Run through homicideanalysis.py

import firearms_class<br />
import nonfirearms_class

Add all of these to the bottom of the 'main()' function in homicideanalysis.py
  - firearms_class.Firearms(homicide_array)<br />
  - nonfirearms_class.Nonfirearms(homicide_array)<br />

// Since idk how to return a list<br />
Add these in order to sort the lists in order from highest to lowest of homicide in each state
  - firearms_data = sorted(firearms_class.Firearms.state_data, key=lambda x: x[1], reverse=True)<br />
  - nonfirearms_data = sorted(nonfirearms_class.Nonfirearms.state_data, key=lambda x: x[1], reverse=True)<br />
  
Incase y'need help to print the top 5 for each state
  -  for item in firearms_data[:5]:<br />
        print(item)<br />
  -  for item in  nonfirearms_data[:5]:<br />
        print(item)
