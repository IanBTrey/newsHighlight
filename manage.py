# Creating app instance
app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)
@manager.command

def test():
    '''
    function to run unit tests
    '''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

# manager.add_command('server',Server)
if __name__ == '__main__':
    manager.run()
