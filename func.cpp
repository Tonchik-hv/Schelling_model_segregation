#include <vector>

extern "C" int count_neighbours(const int* map_data, int size, int row_num, int col_num, int val) {
    // Reshape the data into the vector of vectors
    std::vector<std::vector<int>> MAP;
    int index = 0;
    for (int i = 0; i < size; ++i) {
        std::vector<int> row;
        for (int j = 0; j < size; ++j) {
            row.push_back(map_data[index]);
            ++index;
        }
        MAP.push_back(row);
    }

    // Count neighbours
    int num_rows = MAP.size();
    int num_cols = MAP[0].size();
    int n_neighbours = 0;

    for (int i = -1; i <= 1; ++i) {
        for (int j = -1; j <= 1; ++j) {
            int new_row = (row_num + i + num_rows) % num_rows;
            int new_col = (col_num + j + num_cols) % num_cols;
            
            if (new_row != row_num || new_col != col_num) {
                if (MAP[new_row][new_col] == val) {
                    n_neighbours++;
                }
            }
        }
    }

    return n_neighbours;
}