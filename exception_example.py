class DividerWell:

    def divide_correctly(self):
        result = 15 / 5
        print(f'berechne 15/5: {result}')

    def divide_by_zero(self):
        try:
            result = 20 / 0
            print(f'berechne 20/0: {result}')
        except:
            print('Division mit 0')




class DividerUgly:

    def divide_correctly(self):
        result = 10 / 4
        print(f'berechne 10/4: {result}')

    def divide_by_zero(self):
        result = 10 / 0
        print(f'berechne 10/0: {result}')



if __name__ == '__main__':
    divider1 = DividerWell()
    divider2 = DividerUgly()
    #
    print('korrekte Ausführung\n---')
    divider1.divide_correctly()
    divider1.divide_by_zero()

    print('\n----------------------\nfehlerhafte Ausführung\n---')
    divider2.divide_correctly()
    divider2.divide_by_zero()
