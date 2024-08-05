#include <vector>
using namespace std;

class Solution {
public:
    int m;
    int n;

    void DFS(vector<vector<char>>& board, int i, int j) {
        // 만약 i 또는 j가 보드의 범위를 벗어나거나 보드[i][j]가 'O'가 아니면 반환
        if (i < 0 || i >= m || j < 0 || j >= n || board[i][j] != 'O') {
            return;
        }
        // 보드[i][j]를 '#'로 표시
        board[i][j] = '#';
        // 상하좌우로 DFS 호출 (DFS(i-1,j), DFS(i+1, j), DFS(i, j-1), DFS(i,j+1))
        DFS(board, i - 1, j);
        DFS(board, i + 1, j);
        DFS(board, i, j - 1);
        DFS(board, i, j + 1);
    }

    void solve(vector<vector<char>>& board) {
        if (board.empty()) return;

        m = board.size();
        n = board[0].size();

        // 1. 가장자리와 연결된 'O' 식별
        for (int i = 0; i < m; i++) {
            DFS(board, i, 0);
            DFS(board, i, n - 1);
        }
        for (int j = 0; j < n; j++) {
            DFS(board, 0, j);
            DFS(board, m - 1, j);
        }

        // 보드 순회하여 표시되지 않은 모든 'O'를 'X'로 변환
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 'O') {
                    board[i][j] = 'X';
                }
            }
        }

        // 임시 문자 '#'을 다시 'O'로 복원
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == '#') {
                    board[i][j] = 'O';
                }
            }
        }
    }
};
