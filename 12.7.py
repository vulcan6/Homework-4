# Erick Jimenez
# PSID 1463639
# Zylab 12.7

def get_age():
    age = int(input())
    # Age required to be between 18 and 75 otherwise bring an error
    if age < 18 or age > 75:
    raise ValueError("Invalid age")
    return age
# Should be fine. WIP

def fat_burning_heart_rate(age):
    # Adult Fat Burning Heart Rate = (70% * 220) - Age
    heart_rate = 220 - age
    heart_rate *= 0.7
    return heart_rate

if __name__ == "__main__":
    try:

    age = get_age()
    rate = fat_burning_heart_rate(age)
    print("Fat burning rate for a ", age, " year-old:")
    print(rate, "bpm")
    except ValueError as excpt:
    print(excpt)
    print("Could not calculate heart rate")
    
    age = get_age()