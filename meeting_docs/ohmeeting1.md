# OH Meeting 4/5/24

## Participants

- Evan Leong
- Marcus Linture
- Calvin Nguyen
- Barbara

## Meeting Notes

### neural networks

    - KNN probability is probabilioty that it = 1, 2, or 3
        - just takes the max of the three probabilities and outputs it

### preprocessing:

    - do an average, median, min, max of all the data and perform a statistical analysis?
    - statistical analysis: finding correlations to the SIPA values
        - ex: take the columns, do statistical analysis, and compare it with the output
            - output: is it the KNN prediction or whether or not they did intervene (this was not given to us)
    - hb_average, hb_max, min, median, rate of change for each patient
        - once these are attained, can drop all the other data( hb1, hb2….hbn)
        - pro: cleaner data, less variables so it becomes clearer for the model
    - or, have different decisions for each patient and use that data to train model
        - this may not work because we do not know the decision output for each time
    - can use binary to simiplify data
        - ex: if hB > 7 → 1, else → 0
