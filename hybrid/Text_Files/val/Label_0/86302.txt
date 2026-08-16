#include <bits/stdc++.h>
using namespace std;
int sg[] = {0, 1, 2, 1, 4, 3, 2, 1, 5,  6, 2, 1, 8,  7,  5, 9,
            8, 7, 3, 4, 7, 4, 2, 1, 10, 9, 3, 6, 11, 12, 14};
int n;
unordered_map<int, int> vis;
int len[1000005];
int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> n;
  int sum = 1, num = 0, tot = 0, sq = sqrt(n);
  for (long long i = 2; i * i <= n; i++) {
    if (vis[i]) continue;
    long long j = i;
    ++tot;
    while (j <= n) {
      if (j > sq) num++;
      vis[j] = 1;
      len[tot]++;
      j *= i;
    }
  }
  int nn = n - sq - num;
  for (int i = 1; i <= tot; i++) sum ^= sg[len[i]];
  if (nn & 1) sum ^= 1;
  if (sum)
    cout << "Vasya\n";
  else
    cout << "Petya\n";
}
