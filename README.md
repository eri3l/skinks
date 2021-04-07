# Skink Search Tool

The app filters existing skink data by multiple criteria in order to help with the identification of skinks.  
You can see it live [here](https://share.streamlit.io/eri3l/skinks/main/app.py).

### Toes
Use this option to search by missing toes only.  
This search filters by all possible combinations of  **`missing toes`** and excludes other missing toes.  
Example:
> `selected toes` = [LF1, LF2]   
> Results:   
> The search returns all skinks where [LF1], [LF2], [LF1, LF2] or [none] toes are missing. 

### Search
Use this option to search by multiple criteria:
- SVL (snout to vent length) (mm)  
  Existing skinks above 70mm are classified as adults and labelled with `projected_SVL`=100.  
  The search considers matches within 5 mm of the selected length. All skinks above 70 mm (`@adult`) are classified as adults. 
  In finding matches, it is assumed that skinks grow by  **10** mm per year (`@delta`) and reach adult size at **70** mm (`@adult`). 
  Search is performed on a calculated variable, `projected_SVL`:
  ```python
  projected_SVL= skink_SVL + delta*(current_year – skink_Year) 
  ```  
  
- Paddock/traplist  
  Each paddock contains multiple traps, click below to view the full list of traps:
  | Paddock | Traps |
  | ------ | ------ |
  | pdk_R66 | ['R66', 'board', 'R67', 'M14', 'R68', 'R69', 'R70', 'M11', 'PR1'] |
  | pdk_R71 | ['R71', 'PR2', 'R72', 'M9', 'P3', 'PR3', 'R73', 'M8', 'PR4', 'R74', 'M7', 'PR5', 'R75', 'PR6', 'R76', 'M5', 'PR7'] |
  | pdk_R77 | ['R2', 'PR13', 'R3', 'PR14', 'R4', 'PR15', 'P16', 'PR16', 'R6', 'PR17'] |
  | pdk_R02 | ['W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'W7', 'W8', 'W9', 'W10', 'W11', 'W12', 'W13'] |
  | ... | ... |
  
 - Toes  
    Search by intact or missing toes.
    
### License
This software is distributed under the MIT Software License. See LICENSE.txt for further details or a copy [here](https://opensource.org/licenses/MIT).  

Copyright © 2021 Polina Stucke
