#include <vector>

extern "C" int count_neighbours(const int** MAP, int rows_size, int cols_size, int row_num, int col_num, int val) {
    int num_rows = rows_size;
    int num_cols = cols_size;
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