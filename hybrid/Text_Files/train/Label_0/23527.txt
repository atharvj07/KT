#include <bits/stdc++.h>
using namespace std;
template <class T>
inline T bigmod(T p, T e, T M) {
  long long ret = 1;
  for (; e > 0; e >>= 1) {
    if (e & 1) ret = (ret * p) % M;
    p = (p * p) % M;
  }
  return (T)ret;
}
template <class T>
inline T gcd(T a, T b) {
  if (b == 0) return a;
  return gcd(b, a % b);
}
template <class T>
inline T modinverse(T a, T M) {
  return bigmod(a, M - 2, M);
}
int Set(int N, int pos) { return N = N | (1 << pos); }
int Reset(int N, int pos) { return N = N & ~(1 << pos); }
bool Chkbit(int N, int pos) { return (bool)(N & (1 << pos)); }
int month[] = {-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
int dx[] = {1, 0, -1, 0};
int dy[] = {0, 1, 0, -1};
const double eps = 1e-6;
long long a[100005];
long long ap[100005];
long long aq[100005];
long long ar[100005], q, r;
long long tree[3 * 100005];
long long init(int node, int b, int e) {
  if (b == e) {
    return tree[node] = a[b] * r;
  }
  int left = node * 2;
  int right = node * 2 + 1;
  int mid = (b + e) / 2;
  tree[node] = max(init(left, b, mid), init(right, mid + 1, e));
  return tree[node];
}
long long query(int node, int b, int e, int i, int j) {
  if (i > e || j < b) return -1000000000000000002LL;
  if (i <= b && j >= e) return tree[node];
  int left = node * 2;
  int right = node * 2 + 1;
  int mid = (b + e) / 2;
  long long p = max(query(left, b, mid, i, j), query(right, mid + 1, e, i, j));
  return p;
}
int main() {
  long long n, p;
  cin >> n >> p >> q >> r;
  for (int i = 0; i < n; i++) scanf("%lld", &a[i]);
  init(1, 0, n - 1);
  for (int i = 0; i < n; i++) {
    aq[i] = q * a[i];
    if (i == 0)
      ap[i] = p * a[i];
    else {
      ap[i] = max(ap[i - 1], p * a[i]);
    }
  }
  long long sum = -1000000000000000002LL;
  for (int i = 0; i < n; i++) {
    if (i == 0) {
      sum = ap[i] + aq[i] + query(1, 0, n - 1, 0, n - 1);
    } else {
      long long tmp = ap[i] + aq[i] + query(1, 0, n - 1, i, n - 1);
      sum = max(sum, tmp);
    }
  }
  cout << sum << endl;
  return 0;
}
