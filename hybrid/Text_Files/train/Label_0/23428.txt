#include <bits/stdc++.h>
using namespace std;
int Tc, N;
char Grid[205][205];
int main() {
  cin >> Tc;
  while (Tc--) {
    cin >> N;
    for (int i = 1; i <= N; i++) {
      for (int j = 1; j <= N; j++) cin >> Grid[i][j];
    }
    if (Grid[1][2] == Grid[2][1]) {
      if (Grid[N - 1][N] == Grid[N][N - 1] && Grid[1][2] == Grid[N][N - 1]) {
        cout << 2 << endl;
        cout << N << " " << N - 1 << endl;
        cout << N - 1 << " " << N << endl;
      } else if (Grid[N - 1][N] == Grid[N][N - 1])
        cout << 0 << endl;
      else if (Grid[N - 1][N] == Grid[1][2])
        cout << 1 << endl << N - 1 << " " << N << endl;
      else
        cout << 1 << endl << N << " " << N - 1 << endl;
    } else {
      if (Grid[N - 1][N] == Grid[N][N - 1]) {
        cout << 1 << endl;
        if (Grid[1][2] == Grid[N - 1][N])
          cout << 1 << " " << 2 << endl;
        else
          cout << 2 << " " << 1 << endl;
      } else {
        cout << 2 << endl;
        if (Grid[1][2] == '1')
          cout << 1 << " " << 2 << endl;
        else
          cout << 2 << " " << 1 << endl;
        if (Grid[N][N - 1] == '0')
          cout << N << " " << N - 1 << endl;
        else
          cout << N - 1 << " " << N << endl;
      }
    }
  }
}
