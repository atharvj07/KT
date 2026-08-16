#include <bits/stdc++.h>
using namespace std;
const int maxn = 3e5 + 5;
const char choice[6][2] = {{'A', 'C'}, {'A', 'G'}, {'A', 'T'},
                           {'C', 'G'}, {'C', 'T'}, {'G', 'T'}};
int n, m;
string str[maxn];
int ord[2][maxn][6], cnt[2][maxn];
string out[maxn];
void print(int rc, int k) {
  for (int i = 0; i < n; i++) out[i] = "";
  if (rc == 0) {
    for (int i = 0; i < n; i++)
      for (int j = 0; j < m; j++)
        out[i] += choice[(i & 1) ? 5 - k : k][(j & 1) ^ ord[0][i][k]];
  } else {
    for (int j = 0; j < m; j++)
      for (int i = 0; i < n; i++)
        out[i] += choice[(j & 1) ? 5 - k : k][(i & 1) ^ ord[1][j][k]];
  }
  for (int i = 0; i < n; i++) cout << out[i] << endl;
}
int main() {
  cin >> n >> m;
  for (int i = 0; i < n; i++) cin >> str[i];
  memset(cnt, 0, sizeof(cnt));
  for (int i = 0; i < n; i++) {
    for (int k = 0; k < 6; k++) {
      int now1 = 0, now2 = 0;
      for (int j = 0; j < m; j++) {
        now1 += (str[i][j] != choice[(i & 1) ? 5 - k : k][j & 1]);
        now2 += (str[i][j] != choice[(i & 1) ? 5 - k : k][(j & 1) ^ 1]);
      }
      ord[0][i][k] = now1 < now2 ? 0 : 1;
      cnt[0][k] += min(now1, now2);
    }
  }
  for (int j = 0; j < m; j++) {
    for (int k = 0; k < 6; k++) {
      int now1 = 0, now2 = 0;
      for (int i = 0; i < n; i++) {
        now1 += (str[i][j] != choice[(j & 1) ? 5 - k : k][i & 1]);
        now2 += (str[i][j] != choice[(j & 1) ? 5 - k : k][(i & 1) ^ 1]);
      }
      ord[1][j][k] = now1 < now2 ? 0 : 1;
      cnt[1][k] += min(now1, now2);
    }
  }
  int ans = 0x3f3f3f3f, RC, K;
  for (int rc = 0; rc <= 1; rc++) {
    for (int k = 0; k < 6; k++) {
      if (cnt[rc][k] < ans) ans = cnt[rc][k], RC = rc, K = k;
    }
  }
  print(RC, K);
}
