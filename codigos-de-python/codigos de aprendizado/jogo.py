guerreiro = {"vida": 200, "dano": 20}
goblin = {"vida": 100, "dano":10}

while guerreiro["vida"] >0 and goblin["vida"] >0:

    goblin["vida"] -= guerreiro["dano"]
    print(f"o usuario atacou e deu {guerreiro['dano']} deixando o goblin com {goblin['vida']}")
     
    if goblin["vida"] <= 0:
        print("parabens voce matou um goblin")
        break
    
    guerreiro["vida"] -= goblin["dano"]
    print(f"o goblin atacou e deu {goblin['dano']} deixando o gobseu boneco com {guerreiro['vida']}")

print("fimmm ")