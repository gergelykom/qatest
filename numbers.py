number = range(1,101)
yournumber = int(input('Enter your number:'))
ursqrd = yournumber * yournumber
def counter(number):
    for i in number:
        norm = i
        sqrd = i*i

        print('|Our normal range:',norm,'squared:', sqrd)
        if sqrd > 190:
            break

    for x in range(yournumber):
        normrange = x + 1
        normsqrd = (x + 1)* x
        print('|Your numbers:',normrange, 'squared:', normsqrd)

print('Choosen number:',yournumber,',squared:',ursqrd, counter(number))
