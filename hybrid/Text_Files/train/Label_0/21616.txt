#include <bits/stdc++.h>
using namespace std;
const int mod = 1e9 + 7;
const int N = 5e5 + 10;
vector<char> ans(100);
int ii = 0;
void solve() {
  int r, c, k;
  cin >> r >> c >> k;
  string s[r];
  int cnt = 0;
  for (int i = 0; i < r; i++) {
    cin >> s[i];
    for (int j = 0; j < c; j++) {
      if (s[i][j] == 'R') cnt++;
    }
  }
  char res[r][c];
  vector<int> pabe(k + 1);
  for (int i = 0; i < k; i++) {
    pabe[i] = cnt / k;
    if (cnt % k > i) pabe[i]++;
  }
  int pp = 0;
  int flag = 0;
  int row = 0;
  while (row < r) {
    int col;
    if (flag) {
      col = c - 1;
      while (col >= 0) {
        if (s[row][col] == 'R') {
          res[row][col] = ans[pp];
          pabe[pp]--;
          if (pabe[pp] == 0) {
            if (pp < k - 1) pp++;
          }
        } else
          res[row][col] = ans[pp];
        col--;
      }
    } else {
      col = 0;
      while (col < c) {
        if (s[row][col] == 'R') {
          res[row][col] = ans[pp];
          pabe[pp]--;
          if (pabe[pp] == 0) {
            if (pp < k - 1) pp++;
          }
        } else
          res[row][col] = ans[pp];
        col++;
      }
    }
    row++;
    flag = 1 - flag;
  }
  for (int i = 0; i < r; i++) {
    for (int j = 0; j < c; j++) cout << res[i][j];
    cout << '\n';
  }
}
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  char cc = 'a';
  while (cc <= 'z') {
    ans[ii++] = cc;
    cc++;
  }
  cc = 'A';
  while (cc <= 'Z') {
    ans[ii++] = cc;
    cc++;
  }
  cc = '0';
  while (cc <= '9') {
    ans[ii++] = cc;
    cc++;
  }
  int t;
  cin >> t;
  while (t--) {
    solve();
  }
  return 0;
}
