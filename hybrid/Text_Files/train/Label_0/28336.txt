#include <bits/stdc++.h>
#define rep(i,n) for (int i = 0; i < (n); ++i)
using namespace std;
typedef long long ll;

int main() {
  int n;
  cin >> n;
  vector<int> a(n);
  rep(i,n) {
    int x;
    cin >> x;
    a[x-1]++;
  }
  sort(a.begin(),a.end());
  vector<int> s(n+1); // sum of [0,i)
  rep(i,n) s[i+1] = s[i]+a[i];
  int ans = n;
  for (int k = 1; k <= n; ++k) {
    while (1) {
      bool ok = [&](int c) {
        int i = lower_bound(a.begin(), a.end(), c) - a.begin();
        int sum = c*(n-i) + s[i];
        return (sum >= c*k);
      }(ans);
      if (ok) break;
      --ans;
    }
    printf("%d\n", ans);
  }
  return 0;
}