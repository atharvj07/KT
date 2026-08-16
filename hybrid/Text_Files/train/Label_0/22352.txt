#include <bits/stdc++.h>
using namespace std;
int n, a[1100000], pos;
int zh, fu;
vector<int> f[1100000];
long long ans;
int main() {
  scanf("%d", &n);
  for (int i = 1; i <= n; i++) {
    scanf("%d", &a[i]);
    if (a[i] > i)
      f[a[i] - i].push_back(i);
    else if (a[i] < i)
      f[n - i + a[i]].push_back(i);
    else
      f[0].push_back(i);
  }
  for (int i = 1; i <= n; i++) {
    ans += (long long)abs(a[i] - i);
    if (a[i] - i < 0)
      fu++;
    else if (a[i] - i > 0)
      zh++;
  }
  long long now = ans;
  for (int i = 1; i < n; i++) {
    int last = n - i + 1;
    if (a[last] < n) fu--;
    now -= (long long)zh;
    now += (long long)fu;
    now += (long long)f[i - 1].size();
    if (a[n - i + 1] == n) now--;
    now -= (long long)abs(a[last] - n);
    now += (long long)(a[last] - 1);
    if (a[last] > 1) zh++;
    for (int j = 0; j < f[i - 1].size(); j++) {
      int x = a[f[i - 1][j]];
      int y = f[i - 1][j] + i;
      if (y == n + 1) continue;
      if (y > n) y -= n;
      if (x > y)
        zh++;
      else
        fu++;
    }
    for (int j = 0; j < f[i].size(); j++) {
      int x = a[f[i][j]];
      int y = f[i][j] + i - 1;
      if (y == n) continue;
      if (y > n) y -= n;
      if (x > y)
        zh--;
      else
        fu--;
    }
    if (now < ans) ans = now, pos = i;
  }
  cout << ans << " " << pos << endl;
  return 0;
}
