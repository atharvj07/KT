#include <bits/stdc++.h>
using namespace std;
int T;
signed long long N, M;
int num[62];
void solve() {
  int i, j, k, l, r, x, y;
  string s;
  cin >> T;
  while (T--) {
    cin >> N >> M;
    memset(num, 0, sizeof(num));
    signed long long sum = 0;
    for (i = 0; i < (M); i++) {
      cin >> x;
      y = 0;
      while (1 << (y + 1) <= x) y++;
      num[y]++;
    }
    signed long long ret = 0;
    for (i = 0; i < (60); i++) {
      if (N & (1LL << i)) {
        if (num[i]) {
          num[i]--;
        } else {
          for (j = i + 1; j < 60; j++)
            if (num[j]) break;
          if (j == 60) {
            ret = -1;
            break;
          }
          ret += j - i;
          num[j]--;
          for (x = i + 1; x < j; x++) num[x]++;
        }
      }
      num[i + 1] += num[i] / 2;
    }
    cout << ret << endl;
  }
}
int main(int argc, char** argv) {
  string s;
  int i;
  if (argc == 1) ios::sync_with_stdio(false), cin.tie(0);
  for (i = 0; i < (argc - 1); i++) s += argv[i + 1], s += '\n';
  for (i = 0; i < (s.size()); i++) ungetc(s[s.size() - 1 - i], stdin);
  cout.tie(0);
  solve();
  return 0;
}
