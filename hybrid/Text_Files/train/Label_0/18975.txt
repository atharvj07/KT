#include <bits/stdc++.h>
using namespace std;
const long long int inf = 1000000000000000LL;
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  long long int n, m;
  long long int k;
  cin >> n >> m >> k;
  vector<long long int> a(m);
  for (int j = 0; j < m; j++) cin >> a[j];
  long long int i = 0, ans = 0;
  long long int sum = 0, pag = 1ll;
  if (a[0] % k == 0) {
    pag = a[0] / k;
  } else
    pag = a[0] / k + 1;
  while (i < m) {
    if ((a[i] - sum) <= k * pag) {
      int cont = 0;
      while (i < m && (a[i] - sum) <= k * pag) {
        i++;
        cont++;
        if (i == m) break;
      }
      sum += cont;
      ans++;
    } else {
      if ((a[i] - sum) % k == 0) {
        pag = (a[i] - sum) / k;
      } else {
        pag = (a[i] - sum) / k + 1;
      }
    }
  }
  cout << ans;
  return 0;
}
