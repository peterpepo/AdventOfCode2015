def solve():
    weapons = {
        "Dagger": [8, 4, 0],
        "Shortsword": [10, 5, 0],
        "Warhammer": [25, 6, 0],
        "Longsword": [40, 7, 0],
        "Greataxe": [74, 8, 0]
    }

    armors = {
        "Leather": [13, 0, 1],
        "Chainmail": [31, 0, 2],
        "Splintmail": [53, 0, 3],
        "Bandedmail": [75, 0, 4],
        "Platemail": [102, 0, 5]
    }

    rings = {
        "Damage +1": [25, 1, 0],
        "Damage +2": [50, 2, 0],
        "Damage +3": [100, 3, 0],
        "Defense +1": [20, 0, 1],
        "Defense +2": [40, 0, 2],
        "Defense +3": [80, 0, 3]
    }

    import itertools
    import math

    comb_weap = itertools.combinations(weapons, 1)
    comb_armr = itertools.chain(itertools.combinations(armors, 0), itertools.combinations(armors, 1))
    comb_rings = itertools.chain(itertools.combinations(rings, 0), itertools.combinations(rings, 1),
                                 itertools.combinations(rings, 2))

    comb_all = itertools.product(comb_weap, comb_armr, comb_rings)

    # Hit Points: 100
    # Damage: 8
    # Armor: 2
    ENEMY_HEALTH = 100
    ENEMY_ATTACK = 8
    ENEMY_DEFENSE = 2

    MY_HEALTH = 100

    minimum_price = None
    maximum_price = None

    for combination in comb_all:
        sel_weapons = combination[0]
        sel_armors = combination[1]
        sel_rings = combination[2]

        total_price = 0
        total_attack = 0
        total_defense = 0

        for weapon in sel_weapons:
            total_price += weapons[weapon][0]
            total_attack += weapons[weapon][1]

        for armor in sel_armors:
            total_price += armors[armor][0]
            total_defense += armors[armor][2]

        for ring in sel_rings:
            total_price += rings[ring][0]
            total_attack += rings[ring][1]
            total_attack += rings[ring][2]

        my_health_decrease = max(ENEMY_ATTACK - total_defense, 1)
        enemy_health_decrease = max(total_attack - ENEMY_DEFENSE, 1)

        rounds_to_defeat_enemy = math.ceil(ENEMY_HEALTH / enemy_health_decrease)
        rounds_to_get_killed = math.ceil(MY_HEALTH / my_health_decrease)

        if ((rounds_to_defeat_enemy <= rounds_to_get_killed)
                and (minimum_price is None or total_price < minimum_price)):
            minimum_price = total_price

        if ((rounds_to_defeat_enemy > rounds_to_get_killed)
                and (maximum_price is None or total_price > maximum_price)):
            maximum_price = total_price

    print("Puzzle21 part-A: {}".format(minimum_price))
    print("Puzzle21 part-B: {}".format(maximum_price))


solve()
