#include <bits/stdc++.h>
using namespace std;
signed main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  long long n, m, k;
  cin >> n >> m >> k;
  long long arr[m];
  for (long long i = 0; i < m; i++) cin >> arr[i];
  long long ans = 0;
  long long sub = 0;
  long long g = 1, temp;
  long long now = (arr[0] - 1) / k;
  ;
  for (long long i = 1; i < m; i++) {
    temp = (arr[i] - 1 - sub) / k;
    if (now == temp)
      g++;
    else {
      sub += g;
      g = 1;
      temp = (arr[i] - 1 - sub) / k;
      now = temp;
      ans++;
    }
  }
  cout << ans + 1;
}
