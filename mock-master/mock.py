class MockFunction:
    def __init__(self, name, param_list):
        self.name = name
        self.param_list = param_list

    def __call__(self, *args, **kwargs):
        self.param_list.append((self.name, args, kwargs))

class Mock:
    def __init__(self):
        self.expected = []
        self.called = []

    def add_expected(self, name, *args, **kwargs):
        self.expected.append((name, args, kwards))

    def __getattr__(self, key):
       return MockFunction(key, object.__getattribute__(self, 'called'))

    def __enter__(self):
        pass

    def __exit__(self, _1, _2, _3):
        assert sorted(self.expected) == sorted(self.called)

a = Mock()
a.add_expected('print', (1,2,3), {'sep':'|'})
with a:
    a.print(1,2,3, sep='|')

a = Mock()
a.add_expected('print', (1,2,3), {'sep':'|'})
a.add_expected('sum', (1,2,3))
with a:
    a.print(1,2,3, sep='|')
    a.sum(1,2,3)
