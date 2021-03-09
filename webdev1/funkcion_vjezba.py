def make_cup(color, liquid, pattern):
    return {
        "color": color,
        "liquid": liquid,
        "pattern": pattern
    }

tea_cup = make_cup(color="blue", liquid="tea", pattern="oriental")
coffe_cup = make_cup(color="white", liquid="coffe", pattern="british")
juice_cup = make_cup(color="black", liquid="juice", pattern="plain")

print(tea_cup)
print(coffe_cup)
print(juice_cup)