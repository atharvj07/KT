#include <bits/stdc++.h>
using namespace std;
const int md = 998244353;
inline void add(int &a, int b) {
  a += b;
  if (a >= md) a -= md;
}
inline void sub(int &a, int b) {
  a -= b;
  if (a < 0) a += md;
}
inline int mul(int a, int b) { return (int)((long long)a * b % md); }
inline int power(int a, long long b) {
  int res = 1;
  while (b > 0) {
    if (b & 1) {
      res = mul(res, a);
    }
    a = mul(a, a);
    b >>= 1;
  }
  return res;
}
inline int inv(int a) { return power(a, md - 2); }
vector<int> integrate(vector<int> a) {
  vector<int> b = {0};
  for (int i = 0; i < (int)a.size(); i++) {
    b.push_back(mul(a[i], inv(i + 1)));
  }
  return b;
}
void sub(vector<int> &a, vector<int> b) {
  while (a.size() < b.size()) {
    a.push_back(0);
  }
  for (int i = 0; i < (int)b.size(); i++) {
    sub(a[i], b[i]);
  }
}
int eval(vector<int> a, int x) {
  int res = 0;
  for (int i = (int)a.size() - 1; i >= 0; i--) {
    res = mul(res, x);
    add(res, a[i]);
  }
  return res;
}
const int COEFF = 1000000;
int main() {
  int n;
  cin >> n;
  vector<int> x(n), fracs;
  for (int i = 0; i < n; i++) {
    double foo;
    cin >> foo;
    x[i] = (int)(foo * COEFF + 0.5);
    fracs.push_back(x[i] % COEFF);
  }
  fracs.push_back(0);
  sort(fracs.begin(), fracs.end());
  fracs.resize(unique(fracs.begin(), fracs.end()) - fracs.begin());
  int cnt = (int)fracs.size();
  vector<int> point(n * cnt + 1);
  for (int i = 0; i <= n * cnt; i++) {
    point[i] = i / cnt * COEFF + fracs[i % cnt];
  }
  vector<int> cut(n);
  for (int i = 0; i < n; i++) {
    cut[i] = (int)(find(point.begin(), point.end(), x[i]) - point.begin());
  }
  vector<int> sz(n * cnt);
  for (int i = 0; i < n * cnt; i++) {
    sz[i] = mul((point[i + 1] - point[i] + md) % md, inv(COEFF));
  }
  vector<vector<int> > a(n * cnt);
  vector<int> sum(n * cnt);
  for (int i = 0; i < n * cnt; i++) {
    a[i] = i < min(cnt, cut[0]) ? vector<int>{0, 1} : vector<int>{0};
    sum[i] = a[i].size() == 1 ? 0 : sz[i];
  }
  for (int id = 1; id < n; id++) {
    for (int i = n * cnt - 1; i >= 0; i--) {
      if (i >= cut[id]) {
        a[i] = {0};
        sum[i] = 0;
      } else {
        for (int j = i - 1; j >= i - cnt && j >= 0; j--) {
          add(a[i][0], sum[j]);
        }
        if (i - cnt >= 0) {
          sub(a[i], a[i - cnt]);
        }
        a[i] = integrate(a[i]);
        sum[i] = eval(a[i], sz[i]);
      }
    }
  }
  int ans = 0;
  for (int i = 0; i < n * cnt; i++) {
    add(ans, sum[i]);
  }
  printf("%d\n", ans);
  return 0;
}
