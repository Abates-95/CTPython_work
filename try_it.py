#7-1
# prompt='what kind of car would you like? '
# car=input(prompt)
# print('\nLet me see if i can find you a ' + car)

#7-2
# prompt = 'How many persons are in your group? '
# p=int(input(prompt))

# if p > 8:
#     print('\nPlease wait...')
# else:
#     print('\nTable ready!')

#7-3
# prompt='Please input a number. '
# n=int(input(prompt))
# if n % 10 == 0:
#     print('multiple of 10')
# else:
#     print('not a multiple')

#7-4
# prompt = "\nPlease enter the name of a topping you would like:"
# prompt += "\n(Enter 'quit' when you are finished.) "
# while True:
#     topping = input(prompt)

#     if topping == 'quit':
#        break
#     else:
#        print("I'd love to add " + topping.title() + " for you!")


#7-5
# prompt = "\nHow old is the ticket holder?"
# prompt += "\n(Enter 'quit' when finished)"
# while True:

#     age = int(input(prompt))

#     if age =='quit':
#         break

#     elif age < 3:
#         print('ticket is free!')
#     elif age <= 12:
#         print('ticket is $10')
#     else:
#         print('ticket is $15')

age=1
while age<10:
    if age%2==1:
        if age==3:
            print('ding')
        elif age==4:
            print('dong')
        elif age==5:
            print('the')
        print('which')
    age+=1
print('is dead')