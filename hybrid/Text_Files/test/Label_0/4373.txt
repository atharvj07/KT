#include <bits/stdc++.h>
using namespace std;
const int N = 200010;
int b[N], n;
long long res = -1;
map<int, long long> mp;
int main() {
  scanf("%d", &n);
  for (int i = 1; i <= n; i++) {
    scanf("%d", b + i);
    mp[b[i] - i] += b[i];
  }
  for (auto it = mp.begin(); it != mp.end(); it++) {
    if (res < it->second) res = it->second;
  }
  cout << res << endl;
  return 0;
}
