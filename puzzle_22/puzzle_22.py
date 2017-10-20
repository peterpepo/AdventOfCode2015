spells = {
    "Magic Missile":{"cost": 53, "damage":4},
    "Drain":{"cost": 73, "damage":2, "hp_recover":2},
    "Shield":{"cost": 113, "armor":7, "lasts":6},
    "Poison":{"cost": 173, "damage":3, "lasts":6},
    "Recharge":{"cost": 229, "mana_recover":101, "lasts":5},
}

#--------------------------------------------------

class Player:
    global spells
    # Construct a player
    def __init__(self, hp, mana, mana_spent, spells_to_apply, boss_hp, boss_damage):
        self.hp = hp
        self.mana = mana
        self.mana_spent = mana_spent
        self.boss_hp = boss_hp
        self.boss_damage = boss_damage
        self.spells_to_apply = spells_to_apply

    def __cmp__(self, other):
        return (self.boss_hp > other.boss_hp) - (self.boss_hp < other.boss_hp)

    def __lt__ (self, other):
        return self.boss_hp < other.boss_hp
        # return self.mana_spent < other.mana_spent

    def __str__(self):
        return("Player-state: hp:{}; mana:{}, mana_spent:{}, boss_hp:{}, boss_damage:{}, spells_to_apply:{}".format(self.hp, self.mana, self.mana_spent, self.boss_hp, self.boss_damage, self.spells_to_apply))

    # Play a round
    def play(self):
        #puzzle-B
        self.hp -= 1
        if self.hp<=0:
            return "boss"

        # TEST
        if len(self.spells_to_apply)==0:
            return "noone"

        # List of spells which have run out of efect and shall be deleted
        spells_expired = []

        # In case, multiple shields we arective at the same time
        total_armor = 0

        # Apply all spells, which shall be applied in this step
        for current_spell_name in self.spells_to_apply:

            #Find how many times the spell shall be applied
            times_to_apply = self.spells_to_apply[current_spell_name]
            times_to_apply -= 1
            self.spells_to_apply[current_spell_name] = times_to_apply

            #If the spell has run out of effect, mark it to be deleted
            if times_to_apply <= 0:
                spells_expired.append(current_spell_name)

            # Apply effects of the spell
            # Check whether it causes some damage to enemy
            try:
                self.boss_hp -= spells[current_spell_name]["damage"]
            except KeyError:
                pass

            # Check whether it replenishes health
            try:
                self.hp += spells[current_spell_name]["hp_recover"]
            except KeyError:
                pass

            # Check whether it adds armor
            try:
                total_armor += spells[current_spell_name]["armor"]
            except KeyError:
                pass

            # Check, whether it replenishes mana
            try:
                self.mana += spells[current_spell_name]["mana_recover"]
            except KeyError:
                pass

        # Remove all expired spells
        for expired_spell in spells_expired:
            del self.spells_to_apply[expired_spell]

        spells_expired = []
        for current_spell_name in self.spells_to_apply:

            # Find how many times the spell shall be applied
            times_to_apply = self.spells_to_apply[current_spell_name]
            times_to_apply -= 1
            self.spells_to_apply[current_spell_name] = times_to_apply

            # If the spell has run out of effect, mark it to be deleted
            if times_to_apply <= 0:
                spells_expired.append(current_spell_name)

            # Apply effects of the spell
            # Check whether it causes some damage to enemy
            try:
                self.boss_hp -= spells[current_spell_name]["damage"]
            except KeyError:
                pass

            # Check whether it replenishes health
            try:
                self.hp += spells[current_spell_name]["hp_recover"]
            except KeyError:
                pass

            # Check whether it adds armor
            # try:
            #     total_armor += spells[current_spell_name]["armor"]
            # except KeyError:
            #     pass

            # Check, whether it replenishes mana
            try:
                self.mana += spells[current_spell_name]["mana_recover"]
            except KeyError:
                pass

        #Remove all expired spells
        for expired_spell in spells_expired:
            del self.spells_to_apply[expired_spell]

        if self.boss_hp <= 0:
            return "player"
        else:
            self.hp -= max(1, self.boss_damage - total_armor)

            if self.hp <= 0:
                return "boss"
        return "noone"

    def expand(self):
        expansions = []

        # Try to send every spell
        for new_spell in spells:

            # If player has money for it
            if self.mana > spells[new_spell]["cost"]:

                # If player has no same spell active (e.g two shields at the same time)
                if not(new_spell in self.spells_to_apply):
                    try:
                        times = spells[new_spell]["lasts"]
                    except KeyError:
                        times = 1

                    expansions.append((new_spell, times))

        return expansions

def solve():
    # puzzle_a_init_player = Player(10, 250, 0, {}, 13, 8)
    puzzle_a_init_player = Player(50, 500, 0, {}, 51, 9)

    import queue
    player_state_queue = queue.PriorityQueue()

    player_state_queue.put((puzzle_a_init_player.mana_spent, puzzle_a_init_player))
    counter = 1

    winner = "noone"
    player_state = None

    while (winner != "player" and not(player_state_queue.empty())):
        # print("Size of the queue: {}".format(player_state_queue.qsize()))

        queue_work = player_state_queue.get()

        player_state = queue_work[1]

        # print("Playing state: "+ player_state.__str__())
        winner = player_state.play()
        # print("After play state: " + player_state.__str__())
        # print("winner-of-fight:"+winner)
        if winner == "noone":
            new_player_state_extensions = player_state.expand()

            for new_player_spell_extension in new_player_state_extensions:
                # print(new_player_spell_extension)
                new_spells = player_state.spells_to_apply.copy()
                new_spells[new_player_spell_extension[0]] = new_player_spell_extension[1]

                new_player = Player(player_state.hp, player_state.mana-spells[new_player_spell_extension[0]]["cost"], player_state.mana_spent+spells[new_player_spell_extension[0]]["cost"], new_spells, player_state.boss_hp, player_state.boss_damage)

                player_state_queue.put((new_player.mana_spent, new_player))
                # player_state_queue.put((counter, new_player))
                counter += 1

        if player_state_queue.qsize() > 1000000:
            break

    print("---")
    print("winner: "+winner)
    print("Day22 puzzle: {}".format(player_state.mana_spent))
    print(player_state)


solve()
