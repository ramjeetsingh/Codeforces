t = int(input())
for _ in range(0,t):
    char_health, char_attack = map(int, input().split())
    monster_health, monster_attack = map(int, input().split())

    total_coins, attack_up, health_up = map(int, input().split())

    monster_health_temp = monster_health
    char_won = False

    for coins_in_health in range(0, total_coins + 1):
        char_attack_now = char_attack + attack_up*(total_coins - coins_in_health)
        char_health_now = char_health + health_up*(coins_in_health)
        monster_health = monster_health_temp
 
        attacks_on_char = char_health_now//monster_attack 
        if char_health_now % monster_attack != 0:
            attacks_on_char += 1

        attacks_on_monster = monster_health//char_attack_now
        if monster_health % char_attack_now != 0:
            attacks_on_monster += 1
 
        if attacks_on_char >= attacks_on_monster:
            char_won = True
            print("YES")
            break
        
    if char_won == False:
        print("NO")