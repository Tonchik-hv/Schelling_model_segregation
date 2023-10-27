import unittest
from source import *

class Test_Schelling_model(unittest.TestCase):
    def setUp(self):
        print("\nRunning setUp method...")
        self.model_1 = Schelling_model(size=3, threshold=0.5, max_iter=50)
        self.model_2 = Schelling_model(size=3, threshold=0.5, max_iter=50)

    def tearDown(self):
        print("Running tearDown method...")
    
    def test_n_neighbours(self):
        print("Running test_n_neighbours")

        val_1 = self.model_1.map[1, 1]
        val_2 = self.model_2.map[1, 0]

        if val_1 == 1:
            n_neighbours_1_true = self.model_1.map.sum() - 1
        else:
            n_neighbours_1_true = 8 - self.model_1.map.sum()

        if val_2 == 1:
            n_neighbours_2_true = self.model_2.map.sum() - 1
        else:
            n_neighbours_2_true = 8 - self.model_2.map.sum()

        c_array_1 = python_list_to_c_array(self.model_1.map)
        c_array_2 = python_list_to_c_array(self.model_2.map)

        n_neighbours_1 = mylib.count_neighbours(c_array_1, self.model_1.map.shape[0], self.model_1.map.shape[1], 1, 1, val_1)
        n_neighbours_2 = mylib.count_neighbours(c_array_2, self.model_2.map.shape[0], self.model_2.map.shape[1], 1, 0, val_2)

        self.assertEqual(n_neighbours_1, n_neighbours_1_true)
        self.assertEqual(n_neighbours_2, n_neighbours_2_true)

    def test_map_size(self):
        print("Running test_map_size")

        self.assertEqual(self.model_1.map.shape[0], 3)
        self.assertEqual(self.model_1.map.shape[1], 3)
        self.assertEqual(self.model_2.map.shape[0], 3)
        self.assertEqual(self.model_2.map.shape[1], 3)

    def test_map_values(self):
        print("Running test_map_values")

        self.assertIn(np.unique(self.model_1.map).all(), [0, 1])
        self.assertIn(np.unique(self.model_2.map).all(), [0, 1])
    


        
if __name__=='__main__':
	unittest.main()