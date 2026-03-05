import json

class PlantExpertSystem:
    def __init__(self, data_file):
        # Вчитување на податоците од JSON фајлот
        with open(data_file, 'r') as f:
            self.plants = json.load(f)

    def recommend(self, u_light, u_humidity, u_temp):
        recommendations = []
        
        for plant in self.plants:
            score = 0
            # Систем на бодување (Светлината е најважна = 3 бода)
            if plant['light'] == u_light: score += 3
            if plant['humidity'] == u_humidity: score += 2
            if plant['temp'] == u_temp: score += 1
            
            # Ако има барем 5 од 6 бода, го препорачуваме
            if score >= 5:
                recommendations.append((plant['name'], score))
        
        # Сортирање според најдобар резултат
        return sorted(recommendations, key=lambda x: x[1], reverse=True)

def get_input(prompt, options):
    while True:
        user_choice = input(f"{prompt} ({'/'.join(options)}): ").lower()
        if user_choice in options:
            return user_choice
        print(f"Невалиден внес. Ве молиме изберете од: {options}")

if __name__ == "__main__":
    print("--- Напреден советник за затворени растенија (AI-Based) ---")
    
    # Креирање на системот
    try:
        expert = PlantExpertSystem('plants.json')
        
        # Собирање податоци од корисникот
        light = get_input("Ниво на светлина", ["low", "medium", "high"])
        humidity = get_input("Ниво на влажност", ["low", "medium", "high"])
        temp = get_input("Температурен опсег", ["cool", "moderate", "warm"])
        
        results = expert.recommend(light, humidity, temp)
        
        print("\n--- Резултати од истражувањето ---")
        if results:
            for plant, score in results:
                match_percent = int((score / 6) * 100)
                print(f"✔ {plant} ({match_percent}% совпаѓање)")
        else:
            print("За жал, не најдовме идеално растение за вашите услови.")
            
    except FileNotFoundError:
        print("Грешка: Не е пронајден фајлот 'plants.json'. Проверете дали е во истата папка.")