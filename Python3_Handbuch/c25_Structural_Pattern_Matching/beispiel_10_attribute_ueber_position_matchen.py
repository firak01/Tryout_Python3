#!/usr/bin/env python

class Aufgabe:
    __match_args__ = ("op1", "operator", "op2")
    def __init__(self, operand1, operator, operand2):
        self.op1 = operand1
        self.operator = operator
        self.op2 = operand2

    def auswerten(self):
        match self:
            case Aufgabe(int(op1), op, int(op2)):
                match op:
                    case "+": return op1 + op2
                    case "-": return op1 - op2
                    case "*": return op1 * op2
                    case "/": return op1 // op2
                    case _: raise ValueError(f"Unbekannter Operator: {op}")
            case Aufgabe(Aufgabe() as op1, op, op2):
                return Aufgabe(op1.auswerten(), op, op2).auswerten()
            case Aufgabe(op1, op, op2=Aufgabe() as op2):
                return Aufgabe(op1, op, op2.auswerten()).auswerten()
            case _:
                print("Ungültige Aufgabe:", self)

    def __str__(self):
        match (self.operator, self.op1, self.op2):
            case (op, Aufgabe() as op1, Aufgabe() as op2):
                return f"({op1}) {op} ({op2})"
            case (op, Aufgabe() as op1, int(op2)):
                return f"({op1}) {op} {op2}"
            case (op, int(op1), Aufgabe() as op2):
                return f"{op1} {op} ({op2})"
            case (op, op1, op2):
                return f"{op1} {op} {op2}"


if __name__ == "__main__":
    aufgabe = Aufgabe(Aufgabe(Aufgabe(23,"-",3), "/", 5), "+", Aufgabe(2,"*",3))
    print(f"{aufgabe} = {aufgabe.auswerten()}")
