data = [{"roll":101,"name":"Amit","eng":90,"hindi":80,"maths":40},
        {"roll":102,"name":"Rahul","eng":30,"hindi":70,"maths":50},
        {"roll":103,"name":"Dev","eng":50,"hindi":40,"maths":60},
        {"roll":104,"name":"Anjali","eng":0,"hindi":0,"maths":0},
        {"roll":105,"name":"Mayank","eng":9,"hindi":8,"maths":4},
    ]

for row in data:
    for key in row:
        print(key,row[key])
    print("*******")
