#include <bits/stdc++.h>
using namespace std;
string s[105];
bool mark_row[105];
int n, m;
void ngk() {
  cin >> n >> m;
  for (int i = 1; i <= n; i++) cin >> s[i], s[i] = '0' + s[i] + '0';
  int ans = 0;
  for (int j = 1; j <= m; j++) {
    bool bruh = 0;
    for (int i = 1; i < n; i++) {
      if (!mark_row[i] && s[i][j] > s[i + 1][j]) {
        bruh = 1;
        break;
      }
    }
    if (bruh)
      ans++;
    else {
      for (int i = 1; i < n; i++)
        if (s[i][j] < s[i + 1][j]) mark_row[i] = 1;
    }
  }
  cout << ans;
}
int main(int argc, char *argv[]) {
  iostream::sync_with_stdio(0);
  int test = 1;
  while (test--) {
    ngk();
  }
  return 0;
}
