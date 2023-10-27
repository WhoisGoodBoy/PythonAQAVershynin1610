from lesson20.pytest_example.cat import Cat


class TestCat:
    def setup_class(self):
        self.example_cat = Cat('Falafel', 'brown', 5, 'Good boy') ### bad bad behaviour

    def setup(self):
        print('hiiiiiiii')

    def test_cat_age(self):
        self.example_cat.grow()
        assert self.example_cat.age == 3

    def test_cat_name(self):
        self.example_cat.name = 'defenitely not a Murchick'
        assert self.example_cat.name == 'Murchick'

    def test_empty(self):
        pass

    def teardown(self):
        print('hiiiiiii i`m teardown func')

    def teardown_class(self):
        print('hiiiiiii i`m teardown class func')