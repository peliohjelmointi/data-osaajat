def vero():
     if tulot <= 10000:
        verot = 0
        return  verot
     elif tulot <= 20000:
        verot = (tulot-10000) * 0.1
        return verot
     elif tulot > 20000:
        verot = (10000 * 0.1) + ((tulot-20000) * 0.2)
        return verot
    


tulot = int(input("Sinun tulot: "))
verot = vero()
print("Maksettava vero on:", round(verot, 2), "€")
print("Veroprosentti on:", round(verot/tulot*100, 2), "%")
