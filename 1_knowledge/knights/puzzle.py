from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # A must be a Knight or a Knave, but not both
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),
    # If A claims to be a Knave and a Knight, A is a Knave
    Implication(Not(And(AKnight, AKnave)), AKnave),
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # A must be a Knight or a Knave, but not both
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),
    # B must be a Knight of a Knave, but not both
    And(Or(BKnight, BKnave), Not(And(BKnight, BKnave))),
    # If A is a Knight, A and B are both Knaves
    Implication(AKnight, And(AKnave, BKnave)),
    # If A is a Knave, A and B are NOT both Knaves
    Implication(AKnave, Not(And(AKnave, BKnave))),
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # A must be a Knight or a Knave, but not both
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),
    # B must be a Knight of a Knave, but not both
    And(Or(BKnight, BKnave), Not(And(BKnight, BKnave))),
    # If A is a Knight, A and B are either both Knights or both Knaves
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    # If A is a Knave, either A is a Knight and B is a Knave, or vice versa
    Implication(AKnave, Or(And(AKnight, BKnave), And(AKnave, BKnight))),
    # If B is a Knight, either A is a Knight and B is a Knave, or vice versa
    Implication(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))),
    # If B is a Knave, A and B are either both Knights or both Knaves
    Implication(BKnave, Or(And(AKnight, BKnight), And(AKnave, BKnave)))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # A must be a Knight or a Knave, but not both
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),
    # B must be a Knight of a Knave, but not both
    And(Or(BKnight, BKnave), Not(And(BKnight, BKnave))),
    # C must be a Knight of a Knave, but not both
    And(Or(CKnight, CKnave), Not(And(CKnight, CKnave))),
    # If B is a Knight, A is a Knight and a Knave AND C is a Knave
    Implication(BKnight, And(And(AKnight, AKnave), CKnave)),
    # If B is a Knave, A is not a Knight and a Knave AND C is a Knight
    Implication(BKnave, And(Not(And(AKnight, AKnave)), CKnight)),
    # If C is a Knight, A is a Knight
    Implication(CKnight, AKnight),
    # If C is a Knave, A is a Knave
    Implication(CKnave, AKnave),
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
