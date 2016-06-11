#�ַ����ָ�split string
import re
def testSplit():
    line = 'asdf fjdk; afed, fjek,asdf, foo'
    res = re.split(r'[;,\s]\s*', line)
    print(res)
    #�������
    res = re.split(r'(;|,|\s)\s*', line)
    print("groiup=>", res)


from calendar import month_abbr



def testReplace():
    text = 'Todayis 11/27/2012.PyConstarts3/13/2013.'
    print(text.replace('Todayis', 'Today is'))
    res = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
    print(res)
    datepat = re.compile(r'(\d+)/(\d+)/(\d+)')#compile for eff
    res = datepat.sub(r'\3-\1-\2', text)
    print(res)
    
    def change_date(m):
        mon_name = month_abbr[int(m.group(1))]
        return '{} {} {}'.format(m.group(2), mon_name, m.group(3))

    res = datepat.sub(change_date, text)
    print(res)


import ExpressionEvaluator

if __name__ == "__main__":
    testSplit()
    print('-'*30, end='\n')
    testReplace()
    print('-'*30, end='\n')
    ExpressionEvaluator.descent_parser()