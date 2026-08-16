#include <bits/stdc++.h>
using namespace std;
int N, M;
int p[500005], fav[500005], u[500005], v[500005], first[500005], nex[500005];
int u1[500005], v1[500005], first1[500005], nex1[500005], tot, tot1;
void add(int x, int y) {
  u[++tot] = x;
  v[tot] = y;
  nex[tot] = first[x];
  first[x] = tot;
}
void add1(int x, int y) {
  u1[++tot1] = x;
  v1[tot1] = y;
  nex1[tot1] = first1[x];
  first1[x] = tot1;
}
int main() {
  int i, j, k;
  cin >> N >> M;
  for (i = 1; i <= N; i++) {
    cin >> p[i];
  }
  for (j = 1; j <= M; j++) {
    int x, y;
    cin >> x >> y;
    add(x, y);
    add1(y, x);
  }
  for (i = 1; i <= N - 1; i++) {
    for (j = first[p[i]]; j; j = nex[j]) {
      if (v[j] == p[N]) {
        fav[p[i]]++;
      }
    }
  }
  int x = 0, ans = 0;
  for (i = N - 1; i >= 1; i--) {
    if (N - i - x == fav[p[i]]) {
      x++;
      ans++;
    } else {
      for (j = first1[p[i]]; j; j = nex1[j]) {
        fav[v1[j]]++;
      }
    }
  }
  cout << ans << endl;
}
