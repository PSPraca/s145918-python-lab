class Data(object):

    def __str__(self):
        return 'str'

    def __repr__(self):
        return 'repr'

print('{} {}'.format('one', 'two'))
print('{1} {0}'.format('one', 'two'))
print('{0!s} {0!r}'.format(Data()))
print('{:>10}'.format('test'))
print('{:_<10}'.format('test'))