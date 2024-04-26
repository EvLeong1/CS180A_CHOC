# Meeting with Ms. Sayrs (CHOC Sponsor) - 4/18/24
## Participants
- Lois Sayrs
- Kenny Yu
- Evan Leong
- Kelly Hu
- Marcus Linture
- Calvin Nguyen

Discussed feature selection choices
- HB, angio, iss, unstable columns

Unstable columns
- Is this patient unstable?
- 4 features of instability 
- Just being unstable doesn't mean death 
- If its not specifically ‘death’ then assume the patient is still alive

Diagnosed (screen cold, shock?) -> imaging -> Suspected of bleeding sent to angiography or OR  

Liver_grade is accurate and separate from other liver columns (reliable)
- Liver fluid and liver ctblush are confirmatory for the liver grade
- Replace all 888 with 0 in livet_ctblush(research in data dict what 888 means for this column, check if can be replaced with 0)

Block of null data usually means that a specific hospital did not take data for that specific column 

Maybe add back the hospital names (where the data was taken)
