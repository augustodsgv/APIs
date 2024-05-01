import unittest
from ..api.date import Date
from ..api.task import Task



class TaskTest(unittest.TestCase):
    ## Test of __init__ method ##
    # Valid init
    def test_init(self):
        id = 1059
        task_name = 'Clean the room'
        is_done = False

        # Without tags and Date
        t1 = Task(id, task_name, is_done)
        self.assertEqual(id, t1.id)
        self.assertEqual(task_name, t1.task_name)
        self.assertEqual(is_done, t1.is_done)
        
        # With Date but without tags
        due_date = Date(15, 10, 2024)
        t2 = Task(id, task_name, is_done, due_date=due_date)
        self.assertEqual(id, t2.id)
        self.assertEqual(task_name, t2.task_name)
        self.assertEqual(is_done, t2.is_done)
        self.assertEqual(due_date, t2.due_date)

        # With tags but without date
        tags = ['Tomorrow', 'home']
        t3 = Task(id, task_name, is_done, tags=tags)
        self.assertEqual(id, t3.id)
        self.assertEqual(task_name, t3.task_name)
        self.assertEqual(is_done, t3.is_done)
        self.assertEqual('Tomorrow', t3.tags[0])
        self.assertEqual('home', t3.tags[1])

        # Test with tuple
        task_tuple = (id, task_name, is_done)
        t4 = Task(*task_tuple)
        self.assertEqual(id, t4.id)
        self.assertEqual(task_name, t4.task_name)
        self.assertEqual(is_done, t4.is_done)
        
        

    # Test __eq__ method
    def test_eq_(self):
        # Tests with no tags neither Date
        t1 = Task(143, 'ablublue', False)
        t2 = Task(143, 'ablublue', False)
        self.assertTrue(t1 == t2)
        t2.is_done = True      # Changing is_done
        self.assertFalse(t1 == t2)
        t2.is_done = False
        t2.task_name = 'abluble'
        self.assertNotEqual(t1, t2)

        # Tests with Date
        t3 = Task(143, 'abluble', True, Date(15, 10, 2045))
        t4 = Task(143, 'abluble', True, Date(15, 10, 2045))
        self.assertEqual(t3, t4)
        t3.due_date.day = 14
        self.assertNotEqual(t3, t4)

        # Tests with tags
        t5 = Task(143, 'beibe', False, tags=['Colege', 'Internship'])
        t6 = Task(143, 'beibe', False, tags=['Colege', 'Internship'])
        self.assertEqual(t5, t6)
        t5.tags.append('Important')
        self.assertNotEqual(t5, t6)

    ## Test has_tag ##
    # Task has the tag
    def test_has_tag_true(self):
        tag = 'todo'
        t = Task(143, 'ablublue', False, tags=[tag])
        self.assertTrue(t.has_tag(tag))
    
    # Task doesn't have the tag
    def test_has_tag_false(self):
        tag1 = 'todo'
        tag2 = 'done'
        t = Task(143, 'ablublue', False, tags=[tag1])
        self.assertFalse(t.has_tag(tag2))

    ## Tests for add_tag ##
    # Add new tag
    def test_add_tag_new_tag(self):
        tag = 'done'
        t = Task(143, 'ablublue', False)
        self.assertTrue(t.add_tag(tag))
        self.assertTrue(t.has_tag(tag))

    # Add already existing tag
    def test_add_tag_existing_tag(self):
        tag = 'done'
        t = Task(143, 'ablublue', False, tags=[tag])
        self.assertFalse(t.add_tag(tag))
        self.assertTrue(t.has_tag(tag))

    
    # Add non str tag 
    def test_add_tag_not_str_tag(self):
        tag = (None)
        t = Task(143, 'ablublue', False)
        self.assertRaises(Exception, t.add_tag, (tag))
        self.assertFalse(t.has_tag(tag))


    ## Tests for rm_tag ##
    # Removing tag that exists tag
    def test_rm_tag_existing_tag(self):
        tag = 'done'
        t = Task(143, 'ablublue', False, tags=[tag])
        self.assertTrue(t.rm_tag(tag))
        self.assertFalse(t.has_tag(tag))

    # Removing tag that doesn't exist
    def test_rm_tag_does_no_exists_tag(self):
        t = Task(143, 'ablublue', False)
        self.assertFalse(t.rm_tag('done'))

    ## Tests for tuple conversion ##
    def test_get_tuple(self):
        t = Task(143, 'abluble', True)
        self.assertEqual((143, 'abluble', True), t.get_tuple())

    def test_get_tags_tuple(self):
        tags = ['foo', 'bar', 'tomorrow']
        task_id = 143
        t = Task(task_id, 'abluble', True, tags=tags)
        tag_tuples = t.get_tags_tuple()
        self.assertEqual((task_id, tags[0]), tag_tuples[0])
        self.assertEqual((task_id, tags[1]), tag_tuples[1])
        self.assertEqual((task_id, tags[2]), tag_tuples[2])

        

    

if __name__ == '__main__':
    unittest.main()
