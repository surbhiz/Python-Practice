def print_hun(value):
    a = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    b = ['Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen',
         'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    c = ['Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty',
         'Sixty', 'Seventy', 'Eighty', 'Ninety']
    if value == '000':
        return ''
    ans = ''
    if value[0] != '0':
        ans += a[int(value[0]) - 1] + ' ' + 'Hundred' + ' '
    if 10 < int(value[1:]) <= 19:
        ans += b[int(value[1:]) - 11] + ' '
    elif value[1] != '0' and value[2] == '0':
        ans += c[int(value[1]) - 1] + ' '
    elif value[1] == '0' and value[2] != '0':
        ans += a[int(value[2]) - 1] + ' '
    elif value[1] != '0' and value[2] != '0':
        ans += c[int(value[1]) - 1] + ' ' + a[int(value[2]) - 1] + ' '
    else:
        pass
    return ans


def print_in_words(value):
    ans = ''
    while len(value) != 12:
        value = '0' + value
    print(value)
    bil = print_hun(value[:3])
    mil = print_hun(value[3:6])
    tho = print_hun(value[6:9])
    hun = print_hun(value[9:])
    if bil != '':
        ans += bil + 'Billion' + ' '
    if mil != '':
        ans += mil + 'Million '
    if tho != '':
        ans += tho + 'Thousand '
    if hun != '':
        ans += hun + ' '
    if ans == '':
        print('Zero')
    else:
        print(ans)
    return


for _ in range(int(input())):
    print_in_words(input())
