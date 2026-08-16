#include <bits/stdc++.h>
#pragma GCC optimize("O3")
#pragma comment(linker, "/STACK:100000000")
const double pi = acos(-1);
const int MOD = 1e9 + 7;
const int INF = 1e9 + 7;
const int MAXN = 5e3 + 5;
const double eps = 1e-9;
using namespace std;
bool vis[MAXN];
int a[MAXN * 20], L[MAXN], R[MAXN], mx[MAXN];
double dp[MAXN][MAXN], P[MAXN], tmp2[MAXN];
set<int> ind;
int main() {
  int n, q;
  scanf("%d", &(n)), scanf("%d", &(q));
  for (int i = 0; i < n; i++) ind.insert(i);
  for (int i = 0; i < (n); i++) scanf("%d", &(a[i]));
  for (int i = 0; i < q; i++) {
    scanf("%d %d %lf", L + i, R + i, P + i);
    L[i]--, R[i]--;
    for (int j = 0; j < i; j++)
      if (R[j] - L[j] > R[i] - L[i])
        swap(L[i], L[j]), swap(R[i], R[j]), swap(P[i], P[j]);
  }
  L[q] = 0, R[q] = n - 1, P[q] = 0, q++;
  for (int i = 0; i < q; i++) {
    vector<int> tmp;
    for (int j = 0; j < i; j++)
      if (L[i] <= L[j] && R[j] <= R[i] && !vis[j]) {
        vis[j] = 1;
        tmp.push_back(j);
        mx[i] = max(mx[i], mx[j]);
      }
    while (1) {
      set<int>::iterator it = ind.lower_bound(L[i]);
      if (it != ind.end() && *it <= R[i])
        mx[i] = max(mx[i], a[*it]), ind.erase(it);
      else
        break;
    }
    for (int j = 0; j <= q; j++) tmp2[j] = 1;
    for (int x = 0; x < tmp.size(); x++) {
      int j = tmp[x];
      for (int k = 0; k <= q; k++)
        if (mx[i] + k - mx[j] <= q) tmp2[k] *= dp[j][mx[i] + k - mx[j]];
    }
    for (int j = q; j > 0; j--) tmp2[j] -= tmp2[j - 1];
    dp[i][0] = (1 - P[i]) * tmp2[0];
    for (int j = 1; j <= q; j++)
      dp[i][j] = dp[i][j - 1] + P[i] * tmp2[j - 1] + (1 - P[i]) * tmp2[j];
  }
  double ans = dp[q - 1][0] * mx[q - 1];
  for (int i = 1; i <= q; i++)
    ans += (dp[q - 1][i] - dp[q - 1][i - 1]) * (mx[q - 1] + i);
  printf("%.15f\n", ans);
  return 0;
}
