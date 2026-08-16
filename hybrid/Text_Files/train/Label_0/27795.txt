#include <bits/stdc++.h>
using namespace std;
const int N = 2e6;
struct Node {
  long long cnt, dp[5];
};
long long n, k;
vector<int> g[N];
Node tr[N];
long long ans;
void build(int c, int p) {
  auto& nn(tr[c]);
  nn.cnt = nn.dp[0] = 1;
  for (auto it : g[c]) {
    if (it != p) {
      build(it, c);
      nn.cnt += tr[it].cnt;
      for (int i = 0; i < k; i++)
        for (int j = 0; j < k; j++) {
          ans += nn.dp[i] * tr[it].dp[j] * ((((k - (i + j + 1)) % k) + k) % k);
        }
      for (int i = 0; i < k; i++) nn.dp[(i + 1) % k] += tr[it].dp[i];
    }
  }
  ans += nn.cnt * (n - nn.cnt);
}
int main() {
  scanf("%lld%lld", &n, &k);
  for (int i = 0; i < n - 1; i++) {
    int a, b;
    scanf("%d%d", &a, &b);
    g[a].push_back(b);
    g[b].push_back(a);
  }
  build(1, 0);
  printf("%lld\n", ans / k);
  return 0;
}
