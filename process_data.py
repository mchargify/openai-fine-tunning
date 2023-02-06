import pandas as pd
import json
df = pd.read_csv('athlete_events.csv', nrows=500)

data = []

for index, row in df.iterrows():
    name, sport, games = row['Name'], row['Sport'], row['Games']
    height = row['Height']
    question = (f'A player {name} who plays {sport} in {games}. How how tall is he?')
    answer = (f'A player {name} is {height} cm tall.')
    data.append({'prompt': question, 'completion': answer})

with open('qa.jsonl', 'w') as f:
    for item in data:
        json.dump(item, f)
        f.write('\n')
    