#include <bits/stdc++.h>
using namespace std;
long long int a[2005], b[2005];
int main() {
  int n, m;
  scanf("%d", &n);
  long long int suma = 0, sumb = 0;
  for (int i = 0; i < n; i++) {
    scanf("%lld", &a[i]);
    suma += a[i];
  }
  scanf("%d", &m);
  for (int i = 0; i < m; i++) {
    scanf("%lld", &b[i]);
    sumb += b[i];
  }
  bool flag = 0;
  if (suma < sumb) {
    flag = 1;
    swap(a, b);
    swap(n, m);
    swap(suma, sumb);
  }
  multiset<pair<long long int, pair<int, int> > > s;
  for (int i = 0; i < n; i++)
    for (int j = i + 1; j < n; j++)
      s.insert(make_pair(a[i] + a[j], make_pair(i, j)));
  long long int ex = suma - sumb;
  long long int ans = ex;
  vector<pair<int, int> > sw;
  for (int i = 0; i < n; i++)
    for (int j = 0; j < m; j++) {
      if (abs((sumb - b[j] + a[i]) - (suma - a[i] + b[j])) < ans) {
        ans = abs((sumb - b[j] + a[i]) - (suma - a[i] + b[j]));
        sw.clear();
        sw.push_back(make_pair(i, j));
      }
    }
  for (int i = 0; i < m; i++)
    for (int j = i + 1; j < m; j++) {
      long long int sum = b[i] + b[j];
      multiset<pair<long long int, pair<int, int> > >::iterator it =
          s.upper_bound(make_pair(sum + ex / 2, make_pair(-1, -1)));
      if (it != s.end()) {
        long long int tem = abs(ex - 2 * (it->first - sum));
        if (tem < ans) {
          ans = tem;
          sw.clear();
          sw.push_back(make_pair(it->second.first, i));
          sw.push_back(make_pair(it->second.second, j));
        }
      }
      if (it != s.begin()) {
        it--;
        long long int tem = abs(ex - 2 * (it->first - sum));
        if (tem < ans) {
          ans = tem;
          sw.clear();
          sw.push_back(make_pair(it->second.first, i));
          sw.push_back(make_pair(it->second.second, j));
        }
      }
    }
  cout << ans << endl;
  printf("%d\n", sw.size());
  for (int i = 0; i < sw.size(); i++) {
    if (flag) swap(sw[i].first, sw[i].second);
    printf("%d %d\n", sw[i].first + 1, sw[i].second + 1);
  }
  return 0;
}
