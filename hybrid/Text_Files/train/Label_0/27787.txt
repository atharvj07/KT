#include <bits/stdc++.h>
using namespace std;
int main() {
  std::ios::sync_with_stdio(false);
  int n;
  cin >> n;
  char **v = new char *[n];
  for (int i = 0; i < n; i++) {
    v[i] = new char[n];
    for (int j = 0; j < n; j++) cin >> v[i][j];
  }
  for (int i = 0; i < n; i++)
    for (int j = 0; j < n; j++) {
      if ((j == 0 || j == n - 1 || i > n - 2) && v[i][j] == '#') {
        cout << "NO";
        return 0;
      } else if (v[i][j] == '#') {
        if (v[i + 1][j] == '#' && v[i + 1][j + 1] == '#' &&
            v[i + 1][j - 1] == '#' && v[i + 2][j] == '#')
          v[i][j] = v[i + 1][j] = v[i + 1][j + 1] = v[i + 1][j - 1] =
              v[i + 2][j] = '.';
        else {
          cout << "NO";
          return 0;
        }
      }
    }
  cout << "YES";
}
