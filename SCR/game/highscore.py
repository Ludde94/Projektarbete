import json

class Highscore:
    
    def __init__(self):
        self.filename = "high_score.json"
    
    
    def read_file(self, filename):
        """read file"""
        with open(filename, "r") as file:
            data = json.load(file)
        return data
    
    
    def update_highscore(self, data, entry):
        """update highscore"""
        data.append(entry)
        return data
    
    def save_highscore(self, filename, data):
        with open(filename, "w") as file:
            json.dump(data, file)
    
    
    def show_highscore(self, data):

        data.sort(key=lambda d: d["rolls"])
        top_5 = data[:5]
        for index, i in enumerate(top_5, start=1):
            print(f"{index}.{i['name']} fick 100 poäng på {i['rolls']} slag")