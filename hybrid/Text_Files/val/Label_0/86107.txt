#include <bits/stdc++.h>

using namespace std;

int n, m;
vector<string> s;

int f(int w, int b, int r) {
  int res = 0;
  for (int i = 0; i < w; i++) {
    for (int j = 0; j < m; j++) {
      res += s[i][j] != 'W';
    }
  }
  for (int i = w; i < w + b; i++) {
    for (int j = 0; j < m; j++) {
      res += s[i][j] != 'B';
    }
  }
  for (int i = w + b; i < n; i++) {
    for (int j = 0; j < m; j++) {
      res += s[i][j] != 'R';
    }
  }
  return res;
}

int main(void) {
  cin >> n >> m;

  s.resize(n);
  for (int i = 0; i < n; i++) {
    cin >> s[i];
  }

  int ans = 50 * 50;
  for (int i = 1; i < n; i++) {
    for (int j = 1; i + j < n; j++) {
      ans = min(ans, f(i, j, n - i - j));
    }
  }

  cout << ans << endl;

  return 0;
}
