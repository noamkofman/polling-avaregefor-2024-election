import pandas as pd

pf = pd.read_csv('space t\president_polls.csv')



kamala_rating = (pf.loc[pf['candidate_name']== 'Kamala Harris'])
trump_rating = (pf.loc[pf['candidate_name']== 'Donald Trump'])

kamal_avg = kamala_rating['pct'].mean()
trump_avg = trump_rating['pct'].mean()

print(kamal_avg)
print('\n', trump_avg)
print(pf['state'])
full_state_values = pf['state'].dropna()

# Check if the filtered DataFrame has any values and print them
if not full_state_values.empty:
    print(full_state_values)
else:
    print("No full values in the 'state' column.")