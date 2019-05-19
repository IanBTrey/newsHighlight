

def test():
    '''
    Run unit tests(this feature is the coolest bana)
    '''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

# manager.add_command('server',Server)
if __name__ == '__main__':
    manager.run()
