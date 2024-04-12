# Meeting with Ms. Sayrs (CHOC Sponsor) - 4/11/24
## Participants
- Lois Sayrs
- Kenny Yu
- Evan Leong
- Kelly Hu
- Marcus Linture
- Calvin Nguyen

Talked about feature selection 
- In medicine, a patient might have data left out for column since its not relevant 
    - Know the context for why someone might have missing data
        - Is it true missing or is it relevant to the data	
    - Assign someone to look back and see if the left out data has clinical relevance

Knn columns
Comes from a node analysis which was saved in the data
Can ignore it (not important)

Having a high percent of null since they are happening over a number of hours 
Such as hemoglobin 
Impute this data 

Follow up columns
Was there an ongoing bleed within the child?
Data taken weeks later 

100% of vaso patients are in shock

Exlap and lap are surgery columns 
Primary column to train the model on 

Angio
Good candidates after hour 2-5 for angio 
Take the median (prob around 7 hours)
Maybe take the patients who met these criteria 

CTblush a key indicator for bleeding

Eliminating overlapping edges?
Set min of col i+1 to max of col i
In traditional biostatistics, each column has to be mutually exclusive

Check mean and stdev of each (time1, hb1)
Wide stdev (stdev > 0.5 * mean), then make intervals smaller

3 groups of patients
Clearly bleeding, hb trending down
Clearly getting better, hb trending up
Unsure 
We want to try to predict the unsure group
