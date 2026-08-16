#include <bits/stdc++.h>
const long long OO = 1000000007;
const int MAXN = 100005;
using namespace std;
int n;
vector<int> a(200000), b(200000), c(200000);
vector<int> ina(200000, 0), inb(200000, 0), inc(200000, 0);
bool used[200000];
void add(int cur, int val, vector<int>& ina) {
  while (cur < n) {
    ina[cur] += val;
    cur = cur | (cur + 1);
  }
}
int sum(int cur, vector<int>& ina) {
  int res = 0;
  while (cur >= 0) {
    res += ina[cur];
    cur = (cur & (cur + 1)) - 1;
  }
  return res;
}
int main() {
  cin >> n;
  for (int i = 0; i < n; ++i) {
    cin >> a[i];
    add(a[i], 1, ina);
    a[i] -= sum(a[i], ina) - 1;
  }
  for (int i = 0; i < n; ++i) {
    cin >> b[i];
    add(b[i], 1, inb);
    b[i] -= sum(b[i], inb) - 1;
  }
  int buf = 0;
  for (int i = n - 1; i >= 0; --i) {
    c[i] = (a[i] + b[i] + buf) % (n - i);
    buf = (a[i] + b[i] + buf) / (n - i);
  }
  for (int i = 0; i < n; ++i) {
    int l = 0, r = n;
    while (l + 1 < r) {
      int mid = (l + r) / 2;
      if ((used[mid] ? sum(mid, inc) - 1 : sum(mid, inc)) + c[i] < mid)
        r = mid;
      else
        l = mid;
    }
    c[i] = l;
    used[l] = true;
    add(c[i], 1, inc);
    cout << c[i] << ' ';
  }
  return 0;
}
