#!/usr/bin/python3
# s_literal = 'String literal'
# print(s_literal)

# s_constructor = str('String created using the str constructor.')
# print(s_constructor)

# s_dunder = str.__str__('String created using str dunder method.')
# print(s_dunder)

# s_new = str.__new__(str, 'String created using new dunder method.')
# print(s_new)

# old_formating = str('%s %s, %s').__mod__(('Hello', 'there', 'silly'))
# old_formating = '%s %s, %s' % ('Hello', 'there', 'silly')
# print(old_formating)

# print(type(s))

# dunder_add = string_lit.__add__(' ').__add__(string_cons)
# print(dunder_add)

# print(dir(str))
# print('\u0028')

s = str().__add__('%s %s, %s').__rmod__(('Hi', 'there', 'silly'))
print(s)