#include <bits/stdc++.h>
using namespace std;
map<int, int> mp;
set<int> s;
int a[2345];
int b[2345];
int sum[2345];
int main() {
  mp.clear();
  s.clear();
  int k, n, h = 0, flag = 1;
  scanf("%d %d", &k, &n);
  for (int i = 0; i < k; i++) {
    scanf("%d", &a[i]);
    if (i) {
      sum[i] = a[i] + sum[i - 1];
      mp[sum[i]] = 1;
    } else {
      sum[i] = a[i];
      mp[sum[i]] = 1;
    }
  }
  for (int i = 0; i < n; i++) {
    scanf("%d", &b[i]);
  }
  for (int i = 0; i < k; i++) {
    int t = b[0] - sum[i];
    if (i == 0 || sum[i] != sum[i - 1]) {
      for (int j = 1; j < n; j++) {
        if (!mp[b[j] - t]) {
          flag = 0;
          break;
        }
      }
      if (flag) s.insert(t);
      flag = 1;
    }
  }
  printf("%d\n", (int)s.size());
  return 0;
}
