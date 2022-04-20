from durable.lang import *

with ruleset('animal'):
    @when_all((m.predicate == 'eats') & (m.object =='flies'))
    def frog(c):
        c.assert_fact({'subject':c.m.subject,'predicate':
                       'is','object':'frog'})
    @when_all((m.predicate=='eats') & (m.object == 'frog'))
    def green(c):
        c.assert_fact({'subject':c.m.subject,'predicate':'is','object':'green'})
    @when_all ((m.predicate =='is') & (m.object == 'bird'))
    def black(c):
        c.assert_fact({'subject':c.m.subject,'predicate':'is','object':'black'})
    @when_all(+m.subject)
    def ouptut(c):
        print('Fact:{0} {1} {2}'.format(c.m.subject,c.m.predicate,c.m.object))

    assert_fact('animal',{'subject':'Kermit','predicate':'eats','object':'flies'})