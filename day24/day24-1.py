# 16086
#
# https://adventofcode.com/2018/day/24

import sys
from copy import copy

# read lines in file
with open(sys.argv[1], 'r') as inputFile:
    lines = map(lambda s: s.strip(), list(inputFile))

class Group:

    def __init__(self, t, num, u, hp, ad, at, i, weak, immune):
        self.team = t
        self.number = num
        self.id = '{0}-{1}'.format(t, num)
        self.units = u   # number of units
        self.hitPoints = hp   #hit points per unit
        self.attackDamage = ad    # damage each unit deals
        self.attackType = at  
        self.initiative = i
        self.weaknesses = weak
        self.immunities = immune

    def getEffectivePower(self):
        return self.attackDamage * self.units

    def __repr__(self):
        return "id: {0}\nunits: {1}\neffective power:{8}\nhitpoints: {2}\ndamage: {3}\ntype: {4}\ninitiative: {5}\nweak: {6}\nimmunity: {7}\n".format( \
            self.id, self.units, self.hitPoints, self.attackDamage, self.attackType, self.initiative, self.weaknesses, self.immunities, self.getEffectivePower())

    def __gt__(self, other):
        if self.getEffectivePower() > other.getEffectivePower():
            return True
        if self.getEffectivePower() < other.getEffectivePower():
            return False
        else: # tied
            return self.initiative > other.initiative


immunes = []
infections = []

def getGroup(s):
    #s = 'immune 1021 10433 86 bludgeoning 12 weak-cold immune-slashing immune-bludgeoning'
    tokens = s.split(' ')
    team, number, units, hitpoints, damage, attackType, initiative = list(tokens[0:7])
    #print units
    units = int(units)
    hitpoints = int(hitpoints)
    damage = int(damage)
    initiative = int(initiative)
    other = tokens[7:]
    weaknesses = []
    immunities = []
    for token in other:
        if token.startswith('weak'):
            weaknesses.append(token.replace('weak-', ''))
        if token.startswith('immune'):
            immunities.append(token.replace('immune-', ''))

    g = Group(team, number, units, hitpoints, damage, attackType, initiative, weaknesses, immunities)
    return tokens[0], g

for line in lines:
    name, group = getGroup(line)
    #print name

    if name == 'immune':
        immunes.append(group)
    else:
        infections.append(group)

def addBoost(immunes, boost):
    for immune in immunes:
        immune.attackDamage += boost

def chooseTarget(attacker, defenders):
    # The attacking group chooses to target the group in the enemy army to which it would 
    # deal the most damage (after accounting for weaknesses and immunities, 
    # but not accounting for whether the defending group has 
    # units to actually receive all of that damage).

    # If an attacking group is considering two defending groups to which it would deal equal damage, 
    # it chooses to target the defending group with the largest effective power; 
    # if there is still a tie, it chooses the defending group with the highest initiative. 
    # If it cannot deal any defending groups damage, it does not choose a target. 
    # Defending groups can only be chosen as a target by one attacking group.

    damages = {}
    for defender in defenders:
        if defender.team == attacker.team:
            continue
        damage = calculateDamage(attacker, defender)
        if damage > 0:
            value = "{0:010}-{1:010}-{2:010}".format(damage, defender.getEffectivePower(), defender.initiative)
            damages[defender] = value

    if len(damages) == 0:
        return None

    maxDamage = max(damages.values())
    index = damages.values().index(maxDamage)
    chosen = damages.keys()[index]
    return chosen

def getTargetChoosingOrder(attackers):
    # During the target selection phase, each group attempts to choose one target. 
    # In decreasing order of effective power, groups choose their targets; 
    # in a tie, the group with the higher initiative chooses first. 
    return None

def calculateDamage(attacker, defender):
    # The damage an attacking group deals to a defending group depends on the attacking group's 
    # attack type and the defending group's immunities and weaknesses. 
    # By default, an attacking group would deal damage equal to its effective power 
    # to the defending group. However, if the defending group is immune to the attacking 
    # group's attack type, the defending group instead takes no damage;
    # if the defending group is weak to the attacking group's attack type, 
    # the defending group instead takes double damage.

    # The defending group only loses whole units from damage; 
    # damage is always dealt in such a way that it kills the most units possible,
    # and any remaining damage to a unit that does not immediately kill it is ignored. 
    # For example, if a defending group contains 10 units with 10 hit points each and 
    # receives 75 damage, it loses exactly 7 units and is left with 3 units at full health.

    damage = attacker.getEffectivePower()

    if attacker.attackType in defender.immunities:
        damage = 0

    if attacker.attackType in defender.weaknesses:
        damage = attacker.getEffectivePower() * 2

    #print attacker.id, defender.id, damage
    return damage

def applyDamage(attacker, defender):
    # The defending group only loses whole units from damage; damage is always dealt 
    # in such a way that it kills the most units possible, and any remaining damage to a 
    # unit that does not immediately kill it is ignored. 
    # For example, if a defending group contains 10 units with 10 hit points each 
    # and receives 75 damage, it loses exactly 7 units and is left with 3 units at full health.

    damage = calculateDamage(attacker, defender)
    unitsLost = min(damage/defender.hitPoints, defender.units)
    #print 'units lost', unitsLost
    defender.units -= unitsLost
    if defender.units <= 0:
        return True
    else:
        return False

    return False


def targetChoosingOrder(g):
    return "{0:010}-{1:010}".format(g.getEffectivePower(), g.initiative)


def attackingOrder(g):
    return g.initiative


def gameOver(groups):
    # game is over when all of one army is gone
    immunes = len([x for x in groups if x.team == 'immune'])
    infections = len(groups) - immunes
    return immunes == 0 or infections == 0


def playGame(immunes, infections, boost):
    # get the choosing order
    # create an array with all the groups
    allGroups = immunes + infections
    addBoost(immunes, boost)

    while not gameOver(allGroups):
        attacks = {}
        choosingOrder = sorted(allGroups, key=targetChoosingOrder, reverse = True)
        defenders = copy(allGroups)
        for attacker in choosingOrder:
            defender = chooseTarget(attacker, defenders)
            if defender:
                attacks[attacker] = defender
                defenders.remove(defender)

        attackOrder = sorted(attacks.keys(), key=attackingOrder, reverse = True)
        for attacker in attackOrder:
            killed = applyDamage(attacker, attacks[attacker])
            if killed:
                allGroups.remove(attacks[attacker])

    armies = sum([x.units for x in allGroups])
    return allGroups[0].team, armies


winner, armies = playGame(immunes, infections, 0)
print armies
