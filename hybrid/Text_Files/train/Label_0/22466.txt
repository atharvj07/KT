#include <bits/stdc++.h>
using namespace std;
const long long mod = 1009;
const long long MAXN = 1000005;
const double pi = acos(-1);
long long rev[4 * MAXN];
void fft(complex<double> *a, long long n, long long opt) {
  long long bit = 0;
  while ((1 << bit) < n) bit++;
  for (long long i = 0; i < n; i++) {
    rev[i] = (rev[i >> 1] >> 1) | ((i & 1) << (bit - 1));
    if (i < rev[i]) swap(a[i], a[rev[i]]);
  }
  for (long long mid = 1; mid < n; mid <<= 1) {
    complex<double> temp(cos(pi / mid), opt * sin(pi / mid));
    for (long long i = 0; i < n; i += mid + mid) {
      complex<double> omega(1, 0);
      for (long long j = 0; j < mid; j++, omega *= temp) {
        complex<double> x = a[i + j], y = omega * a[i + j + mid];
        a[i + j] = x + y, a[i + j + mid] = x - y;
      }
    }
  }
  if (opt == -1)
    for (long long i = 0; i < n; i++) a[i] /= n;
}
complex<double> a[4 * MAXN], b[4 * MAXN];
long long c[200005];
long long num[200005];
vector<long long> v[200005];
struct node {
  long long id;
  friend bool operator<(const node &a, const node &b) {
    return v[a.id].size() > v[b.id].size();
  }
};
priority_queue<node> q;
void Merge(long long id1, long long id2) {
  long long sz1 = v[id1].size();
  long long sz2 = v[id2].size();
  long long nsiz = sz1 + sz2 - 1;
  long long len = 1;
  while (len <= nsiz) len <<= 1;
  for (long long i = 0; i < sz1; i++) a[i] = v[id1][i];
  for (long long i = sz1; i <= len; i++) a[i] = 0;
  for (long long i = 0; i < sz2; i++) b[i] = v[id2][i];
  for (long long i = sz2; i <= len; i++) b[i] = 0;
  fft(a, len, 1);
  fft(b, len, 1);
  for (long long i = 0; i <= len; i++) a[i] = a[i] * b[i];
  fft(a, len, -1);
  v[id1].clear();
  v[id2].clear();
  for (long long i = 0; i <= nsiz; i++) {
    v[id1].push_back(((long long)(a[i].real() + 0.5)) % 1009);
  }
}
vector<long long> bb;
int main() {
  long long n, m, k;
  scanf("%lld%lld%lld", &n, &m, &k);
  for (long long i = 1; i <= n; i++) {
    long long x;
    scanf("%lld", &x);
    c[x]++;
  }
  for (long long i = 1; i <= n; i++) num[c[i]]++;
  bb.push_back(1);
  long long nn = 0;
  v[nn] = bb;
  q.push(node{nn});
  nn++;
  for (long long i = 1; i <= n; i++) {
    bb.push_back(1);
    if (num[i] == 0) continue;
    for (long long k = 1; k <= num[i]; k++) {
      v[nn] = bb;
      q.push(node{nn});
      nn++;
    }
  }
  long long siz = q.size() - 1;
  while (siz--) {
    long long id1 = q.top().id;
    q.pop();
    long long id2 = q.top().id;
    q.pop();
    Merge(id1, id2);
    q.push(node{id1});
  }
  printf("%lld\n", (v[q.top().id][k] + 1009) % 1009);
  return 0;
}
