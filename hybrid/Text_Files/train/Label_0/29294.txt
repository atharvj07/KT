#include <bits/stdc++.h>
using namespace std;
const int inf = 0x3f3f3f3f;
const double eps = 1e-8;
int n, k1, k2;
int cnt[14005], edges[2], res[14005];
int a[7005], b[7005];
vector<int> rev[2];
bool visited[14005];
queue<int> q;
int main() {
  ios_base::sync_with_stdio(0);
  while (cin >> n) {
    cin >> k1;
    for (int i = 0; i < k1; ++i) {
      cin >> a[i];
      rev[0].push_back(a[i]);
    }
    cin >> k2;
    for (int i = 0; i < k2; ++i) {
      cin >> b[i];
      rev[1].push_back(b[i]);
    }
    edges[0] = k2;
    edges[1] = k1;
    memset(cnt, 0, sizeof(cnt));
    memset(visited, 0, sizeof(visited));
    memset(res, -1, sizeof(res));
    q.push(0);
    q.push(1);
    visited[0] = visited[1] = 1;
    res[0] = res[1] = 0;
    int cur, nxt;
    while (q.size()) {
      cur = q.front();
      q.pop();
      if (res[cur] != -1) {
        for (int i = 0; i < rev[cur % 2].size(); ++i) {
          nxt = ((cur - (rev[cur % 2][i] << 1) + (n << 1)) % (n << 1)) ^ 1;
          if (!visited[nxt]) {
            if (res[cur]) cnt[nxt]++;
            if (!res[cur] || cnt[nxt] == edges[nxt % 2]) {
              res[nxt] = 1 - res[cur];
              visited[nxt] = 1;
              q.push(nxt);
            }
          }
        }
      }
    }
    for (int i = 1; i < n; ++i) {
      if (res[i << 1 | 1] == -1)
        cout << "Loop ";
      else if (res[i << 1 | 1])
        cout << "Win ";
      else
        cout << "Lose ";
    }
    cout << "\n";
    for (int i = 1; i < n; ++i) {
      if (res[i << 1] == -1)
        cout << "Loop ";
      else if (res[i << 1])
        cout << "Win ";
      else
        cout << "Lose ";
    }
    cout << "\n";
    rev[0].clear();
    rev[1].clear();
  }
  return 0;
}
