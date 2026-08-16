#include <bits/stdc++.h>
using namespace std;
signed main() {
  std ::ios_base ::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  ;
  long long n;
  cin >> n;
  string s;
  cin >> s;
  long long res = 0;
  for (long long j = 0; j < n; j++) {
    s[j] == '+' ? res++ : res--;
    if (res < 0) res++;
  }
  cout << res;
}
