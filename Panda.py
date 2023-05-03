import pandas as pd

data_list = [
{"title": "Frozen Red Sour Pitted Cherries", "price": "$120.35 / 40 LB"},
{"title": "Frozen Sliced Peaches", "price": "$65.55 / 10 KG"},
{"title": "Black Plums", "price": "$66.10 / 48-56 CT X 2 LYR"},
{"title": "Red Plums", "price": "$71.30 / 48-56 CT X 2 LYR"},
{"title": "Yellow Peaches", "price": "$70.20 / 48 CT X 2 LYR"},
{"title": "White Donut Peaches", "price": "$75.15 / 60-65 CT X 10 LB"},
{"title": "Red Pluots", "price": "$45.70 / 48-56 CT X 2 LYR"},
{"title": "Large Loose Artichokes", "price": "$84.40 / 20 LB"},
{"title": "Artichokes", "price": "$45.30 / 24 CT"},
{"title": "Artichokes", "price": "$50.65 / 18 CT"},
{"title": "Artichokes", "price": "$41.70 / 12 CT"},
{"title": "Artichokes", "price": "$37.75 / 30/36 CT"},
{"title": "Puple Artichokes", "price": "$51.60 / 12-18 CT"},
{"title": "Sunchokes", "price": "$22.90 / 5 LB"},
{"title": "European Heirloom Sunchokes", "price": "$28.95 / 11 LB"},
{"title": "Sunchokes", "price": "$71.35 / 20 LB"},
{"title": "Artichokes", "price": "$63.90 / 24 CT"},
{"title": "Organic Artichokes", "price": "$51.85 / 24 CT"},
{"title": "Organic Artichokes", "price": "$75.95 / 12 CT"},
{"title": "Baby Artichokes", "price": "$92.85 / 20 LB"}
]

df = pd.DataFrame(data_list)


df.to_excel('output.xlsx', index=False)