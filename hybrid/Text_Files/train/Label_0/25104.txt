#include <bits/stdc++.h>
using namespace std;
const long long INF = 1e18 + 5;
const int mod = 1e9 + 9;
const int N = 3 * 1e5 + 5;
namespace FIB {
struct Matrix {
  int a[3][3];
  Matrix() { memset(a, 0, sizeof(a)); }
  Matrix operator*(const Matrix& M2) {
    Matrix result;
    for (int i = 0; i < 3; i++)
      for (int j = 0; j < 3; j++)
        for (int k = 0; k < 3; k++) {
          result.a[i][j] =
              (result.a[i][j] + 1ll * this->a[i][k] * M2.a[k][j]) % mod;
        }
    return result;
  }
  static Matrix eye() {
    Matrix res;
    for (int i = 0; i < 3; i++) res.a[i][i] = 1;
    return res;
  }
  Matrix exp(int pw) {
    if (pw == 0) return eye();
    if (pw == 1) return *this;
    Matrix half = this->exp(pw / 2);
    if (pw % 2) return half * half * (*this);
    return half * half;
  }
};
Matrix initMat() {
  Matrix res;
  int dx[] = {0, 0, 1, 2, 2};
  int dy[] = {0, 1, 0, 0, 2};
  for (int i = 0; i < 5; i++) res.a[dx[i]][dy[i]] = 1;
  return res;
}
Matrix matrices[N];
void initMatrices() {
  matrices[0] = Matrix::eye();
  matrices[1] = initMat();
  for (int i = 2; i < N; i++) matrices[i] = matrices[i - 1] * matrices[1];
}
pair<int, pair<int, int> > fib(int a, int b, int n) {
  Matrix& base = matrices[n - 1];
  pair<int, pair<int, int> > res;
  res.first = (1ll * base.a[0][0] * b + 1ll * base.a[0][1] * a +
               1ll * base.a[0][2] * a) %
              mod;
  res.second.first = (1ll * base.a[1][0] * b + 1ll * base.a[1][1] * a +
                      1ll * base.a[1][2] * a) %
                     mod;
  res.second.second = (1ll * base.a[2][0] * b + 1ll * base.a[2][1] * a +
                       1ll * base.a[2][2] * a) %
                      mod;
  return res;
}
}  // namespace FIB
namespace SegTree {
int n;
int s[4 * N], a[4 * N], lazyA[4 * N], lazyB[4 * N];
inline int aggr(int val1, int val2) { return (val1 + val2) % mod; }
void build(int l, int r, int id) {
  if (l == r) {
    s[id] = a[l];
  } else {
    int mid = (l + r) / 2;
    build(l, mid, id * 2);
    build(mid + 1, r, id * 2 + 1);
    s[id] = aggr(s[id * 2], s[id * 2 + 1]);
  }
}
void upd(int id, int l, int r, int va, int vb) {
  if (l == r) {
    s[id] = aggr(s[id], va);
  } else {
    lazyA[id] = aggr(lazyA[id], va);
    lazyB[id] = aggr(lazyB[id], vb);
    s[id] = aggr(s[id], FIB::fib(va, vb, r - l + 1).second.second);
  }
}
void shift(int id, int l, int r) {
  if (lazyA[id]) {
    int mid = (l + r) / 2;
    int va = lazyA[id];
    int vb = lazyB[id];
    upd(id * 2, l, mid, va, vb);
    pair<int, pair<int, int> > rb = FIB::fib(va, vb, mid + 2 - l);
    upd(id * 2 + 1, mid + 1, r, rb.second.first, rb.first);
    lazyA[id] = 0;
    lazyB[id] = 0;
  }
}
void update(int x, int y, int l, int r, int id, int va, int vb) {
  if (l >= x && r <= y) {
    pair<int, pair<int, int> > rb = FIB::fib(va, vb, l - x + 1);
    upd(id, l, r, rb.second.first, rb.first);
    return;
  }
  if (y < l || x > r) return;
  shift(id, l, r);
  int mid = (l + r) / 2;
  update(x, y, l, mid, id * 2, va, vb);
  update(x, y, mid + 1, r, id * 2 + 1, va, vb);
  s[id] = aggr(s[id * 2], s[id * 2 + 1]);
}
int query(int x, int y, int l, int r, int id) {
  if (l >= x && r <= y) {
    return s[id];
  }
  if (y < l || x > r) return 0;
  shift(id, l, r);
  int mid = (l + r) / 2;
  return aggr(query(x, y, l, mid, id * 2), query(x, y, mid + 1, r, id * 2 + 1));
}
}  // namespace SegTree
int main() {
  ios_base::sync_with_stdio(false);
  FIB::initMatrices();
  int n, m;
  cin >> n >> m;
  SegTree::n = n;
  for (int i = 0; i < n; i++) cin >> SegTree::a[i];
  SegTree::build(0, n - 1, 1);
  for (int i = 0; i < m; i++) {
    int choice, a, b;
    cin >> choice >> a >> b;
    a -= 1;
    b -= 1;
    if (choice == 1) {
      SegTree::update(a, b, 0, n - 1, 1, 1, 1);
    } else {
      int ans = SegTree::query(a, b, 0, n - 1, 1);
      cout << ans << endl;
    }
  }
  return 0;
}
