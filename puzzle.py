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
    # A either knight or knave
    Or(AKnight, AKnave),
    Not(And(AKnave, AKnight)),
    Implication(AKnight,And(AKnight,AKnave)),
    Implication(AKnave, Not(And(AKnave, AKnight)))
                

)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Implication(AKnave, Not(And(AKnave, BKnave))),
    Implication(AKnight, And(AKnave, BKnave)),
    Or(AKnight,AKnave),
    Or(BKnave,BKnight),
    Not(And(AKnave, AKnight)),
    Not(And(BKnave, BKnight)),
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # when A is a knight
    Implication(AKnight,Or(And(AKnight,BKnight), And(AKnave,BKnave))), 
    # when A is a knave
    Implication(AKnave, Not(Or(And(AKnight,BKnight), And(AKnave, BKnave)))),
    # when B is a knight
    Implication(BKnight, Or(And(BKnight, AKnave), And(BKnave, AKnight))),
    # when B is a knave
    Implication(BKnave, Or(And(BKnight, AKnight), And(BKnave, AKnave))),
    # to ensure that the rule evrey charcter is either knight or knave gets applyed
    Or(AKnight,AKnave),
    Or(BKnave,BKnight),
    Not(And(AKnave, AKnight)),
    Not(And(BKnave, BKnight)),
    

)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
ASaidKnave = Symbol("A said 'I am a knave'")
knowledge3 = And(
    Not(ASaidKnave),
    Implication(BKnight,ASaidKnave),
    Implication(BKnave,Not(ASaidKnave)),
    Implication(BKnight, CKnave),
    Implication(BKnave, CKnight),
    Implication(CKnight, AKnight),
    Implication(CKnave, AKnave),
    
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    Not(And(CKnight, CKnave)),
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
