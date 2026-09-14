#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int M, N;
int best_square_count = 1000000000;
int solution_amount = 0;

vector<vector<int>> grid;

bool can_place(int x, int y, int size)
{
    if (x + size > M || y + size > N)
        return false;

    for (int i = x; i < x + size; i++)
    {
        for (int j = y; j < y + size; j++)
        {
            if (grid[i][j] != 0)
                return false;
        }
    }

    return true;
}

void set_square(int x, int y, int size, int value)
{
    for (int i = x; i < x + size; i++)
    {
        for (int j = y; j < y + size; j++)
        {
            grid[i][j] = value;
        }
    }
}

pair<int, int> find_empty_cell()
{
    for (int i = 0; i < M; i++)
    {
        for (int j = 0; j < N; j++)
        {
            if (grid[i][j] == 0)
                return {i, j};
        }
    }

    return {-1, -1};
}

void backtracking(int squares_count)
{
    // cout << "[BACKTRACK] Current squares: " << squares_count << endl;

    if (squares_count >= best_square_count)
    {
        // cout << "[STOP] Current count is not better than best result" << endl;
        return;
    }

    auto [x, y] = find_empty_cell();

    if (x == -1)
    {
        cout << "[FOUND] Field completed with " << squares_count << " squares" << endl;

        if (squares_count < best_square_count)
        {
            cout << "[NEW BEST] " << squares_count << " squares" << endl;
            best_square_count = squares_count;
            solution_amount = 1;
        }
        else if (squares_count == best_square_count)
        {
            // cout << "[SAME BEST] Another solution found" << endl;
            solution_amount++;
        }

        return;
    }

    // cout << "[EMPTY CELL] Position: (" << x << "," << y << ")" << endl;

    int max_size = min(M - x, N - y);
    max_size = min(max_size, N - 1);

    // cout << "[MAX SIZE] " << max_size << endl;

    for (int size = max_size; size >= 1; size--)
    {
        // cout << "[TRY] Square " << size << "x" << size << " at (" << x << "," << y << ")" << endl;

        if (can_place(x, y, size))
        {
            // cout << "[PLACE] Square " << size << "x" << size << " added" << endl;

            set_square(x, y, size, squares_count + 1);

            backtracking(squares_count + 1);

            // cout << "[ROLLBACK] Remove square " << size << "x" << size << " from (" << x << "," << y << ")" << endl;

            set_square(x, y, size, 0);
        }
        else
        {
            // cout << "[SKIP] Square " << size << "x" << size << " cannot be placed" << endl;
        }
    }

    // cout << "[RETURN] Back to previous level" << endl;
}

int main()
{
    cin >> M >> N;

    if (M < 2 || N < 2 || M > 20 || N > 20)
    {
        cout << "Table size must be between 2 and 20" << endl;
        return 0;
    }

    grid.assign(M, vector<int>(N, 0));

    best_square_count = M * N + 1;
    solution_amount = 0;

    cout << "[START] Solving field " << M << "x" << N << endl;

    backtracking(0);

    cout << "\nMin squares count: "
         << best_square_count << endl;

    cout << "Solutions amount: "
         << solution_amount << endl;

    return 0;
}
