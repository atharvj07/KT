#include <bits/stdc++.h>
using namespace std;
long long ab(long long n) { return n < 0 ? -n : n; }
int main() {
  long long n, m, in;
  vector<long long> A, B;
  scanf("%lld %lld", &n, &m);
  for (int i = 0; i < n; i++) {
    scanf("%lld", &in);
    A.push_back(in);
  }
  for (int i = 0; i < n; i++) {
    scanf("%lld", &in);
    B.push_back(in);
  }
  long long ans = INT_MAX;
  set<long long> S;
  set<long long>::iterator it;
  vector<long long> d;
  for (int i = 0; i < n; i++) {
    int x = B[n - 1] - A[i];
    if (x < 0) x += m;
    S.insert(x);
  }
  for (it = S.begin(); it != S.end(); it++) {
    d.push_back(*it);
  }
  int len = d.size();
  sort(B.begin(), B.end());
  for (int i = 0; i < len; i++) {
    vector<long long> tmp;
    for (int j = 0; j < n; j++) {
      tmp.push_back((A[j] + d[i]) % m);
    }
    sort(tmp.begin(), tmp.end());
    if (tmp == B) {
      ans = d[i];
      break;
    }
  }
  printf("%lld\n", ans);
  return 0;
}
