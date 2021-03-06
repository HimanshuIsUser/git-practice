import re
mystr ="One of the most common examples 919818812568 of an algebraic data type is the singly linked list. A list type is a sum type with two variants, Nil for an empty list and Cons x xs for the combination of a new element x with a list xs to create a new list. Here is an example of how a singly linked list would be declared in Haskell:data List a = Nil | Cons a (List a)Cons is an abbreviation of construct. Many languages have special syntax for lists defined in this way. For example, Haskell and ML use [] for Nil, : or :: for Cons, respectively, and square brackets for entire lists. So Cons 1 (Cons 2 (Cons 3 Nil)) would normally be written as 1:2:3:[] or [1,2,3] in Haskell, or as 1::2::3::[] or [1;2;3] in ML.For a slightly more complex example, binary trees may be implemented in Haskell as follows:data Tree = Empty| Leaf INode Tree TreeHere, Empty represents an empty tree, Leaf contains a piece of data, and Node organizes the data into branches.In most languages that support algebraic data types, it is possible to define parametric types. Examples are given later in this article.Somewhat similar to a function, a data constructor is applied to arguments of an appropriate type, yielding an instance of the data type to which the type constructor belongs. For example, the data constructor Leaf is logically a function Int -> Tree, meaning that giving an integer as an argument to Leaf produces a value of the type Tree. As Node takes two arguments of the type Tree itself, the datatype is recursive."
print(mystr)
# patt = re.compile(r'is')
# patt = re.compile(r'.sing')
# patt = re.compile(r'^One')
# patt = re.compile(r'recursive.$')
# patt = re.compile(r'ab*')
# patt = re.compile(r'ab+')
# patt = re.compile(r'ab{2}')
# patt = re.compile(r'(ab){1}')
# patt = re.compile(r'ab{1}|tat')
# patt = re.compile(r'\AOne')
# patt = re.compile(r'\bco')
# patt = re.compile(r'ne\b')
# patt = re.compile(r'\Bing')
# patt = re.compile(r'\D')
# patt = re.compile(r'\s')
# patt = re.compile(r'\wis')
# patt = re.compile(r'\S')
# patt = re.compile(r'.\Z')
# patt = re.compile(r'\d{12}')
match = patt.finditer(mystr)
for matches in match:
    # print(matches)
    # print(mystr[1292:1486])
    print(matches)
    # print(mystr[42:44])
