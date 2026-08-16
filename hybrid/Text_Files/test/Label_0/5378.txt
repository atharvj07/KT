#include <bits/stdc++.h>
using namespace std;
const int MaxN = 1e5 + 15;
const int LOG = 18;
int n, mod;
vector<int> primeDivisors;
vector<vector<int> > powers;
int fiMOD;
int a[MaxN];
int goodPart[MaxN];
vector<int> f[MaxN];
int phi(int n) {
  int res = n;
  for (int i = 2; i * i <= n; ++i)
    if (n % i == 0) {
      while (n % i == 0) n /= i;
      res -= res / i;
    }
  if (n > 1) res -= res / n;
  return res;
}
int bpow(int a, int b) {
  int res = 1;
  while (b) {
    if (b & 1) res = (long long)res * a % mod;
    b >>= 1;
    a = (long long)a * a % mod;
  }
  return res;
}
struct node {
  vector<int> cnt;
  int sum;
  int mulPrimes;
  bool flag;
} tree[MaxN * 4];
void calcLeafSum(int x) {
  int sum = tree[x].mulPrimes;
  for (int j = 0; j < tree[x].cnt.size(); ++j)
    sum = (long long)sum * powers[j][tree[x].cnt[j]] % mod;
  tree[x].sum = sum;
}
void push(int x) {
  if (!tree[x].flag) return;
  tree[x].flag = false;
  for (int i = 0; i < tree[x].cnt.size(); ++i) {
    tree[x + x].cnt[i] += tree[x].cnt[i];
    tree[x + x + 1].cnt[i] += tree[x].cnt[i];
    tree[x + x].sum =
        (long long)tree[x + x].sum * powers[i][tree[x].cnt[i]] % mod;
    tree[x + x + 1].sum =
        (long long)tree[x + x + 1].sum * powers[i][tree[x].cnt[i]] % mod;
    tree[x].cnt[i] = 0;
  }
  tree[x + x].flag = tree[x + x + 1].flag = true;
  tree[x + x].sum = (long long)tree[x + x].sum * tree[x].mulPrimes % mod;
  tree[x + x + 1].sum =
      (long long)tree[x + x + 1].sum * tree[x].mulPrimes % mod;
  tree[x + x].mulPrimes =
      (long long)tree[x + x].mulPrimes * tree[x].mulPrimes % mod;
  tree[x + x + 1].mulPrimes =
      (long long)tree[x + x + 1].mulPrimes * tree[x].mulPrimes % mod;
  tree[x].mulPrimes = 1;
}
void updateMul(int x, int l, int r, int ll, int rr, int value) {
  if (l > rr || r < ll) return;
  if (l >= ll && r <= rr) {
    for (int i = 0; i < f[value].size(); ++i) tree[x].cnt[i] += f[value][i];
    tree[x].mulPrimes = (long long)tree[x].mulPrimes * goodPart[value] % mod;
    tree[x].sum = (long long)tree[x].sum * value % mod;
    tree[x].flag = true;
    return;
  }
  int mid = (l + r) / 2;
  push(x);
  updateMul(x + x, l, mid, ll, rr, value);
  updateMul(x + x + 1, mid + 1, r, ll, rr, value);
  tree[x].sum = (tree[x + x].sum + tree[x + x + 1].sum) % mod;
}
void updateDiv(int x, int l, int r, int pos, int value) {
  if (l == r) {
    tree[x].mulPrimes =
        (long long)tree[x].mulPrimes * bpow(goodPart[value], fiMOD - 1) % mod;
    for (int i = 0; i < tree[x].cnt.size(); ++i) tree[x].cnt[i] -= f[value][i];
    calcLeafSum(x);
  } else {
    int mid = (l + r) / 2;
    push(x);
    if (pos <= mid)
      updateDiv(x + x, l, mid, pos, value);
    else
      updateDiv(x + x + 1, mid + 1, r, pos, value);
    tree[x].sum = (tree[x + x].sum + tree[x + x + 1].sum) % mod;
  }
}
void build(int x, int l, int r) {
  if (l == r) {
    tree[x].sum = 1;
    tree[x].mulPrimes = 1;
    tree[x].flag = false;
    tree[x].cnt.resize(primeDivisors.size(), 0);
    updateMul(x, l, r, l, r, a[l]);
  } else {
    int mid = (l + r) / 2;
    build(x + x, l, mid);
    build(x + x + 1, mid + 1, r);
    tree[x].sum = (tree[x + x].sum + tree[x + x + 1].sum) % mod;
    tree[x].mulPrimes = 1;
    tree[x].flag = false;
    tree[x].cnt.resize(primeDivisors.size(), 0);
  }
}
int getAns(int x, int l, int r, int ll, int rr) {
  if (l > rr || r < ll) return 0;
  if (l >= ll && r <= rr) return tree[x].sum;
  push(x);
  int mid = (l + r) / 2;
  return (getAns(x + x, l, mid, ll, rr) +
          getAns(x + x + 1, mid + 1, r, ll, rr)) %
         mod;
}
vector<int> factorize(int x) {
  vector<int> res;
  for (int i = 2; i * i <= x; ++i)
    if (x % i == 0) {
      x /= i;
      res.push_back(i);
      while (x % i == 0) x /= i;
    }
  if (x > 1) res.push_back(x);
  return res;
}
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cin >> n >> mod;
  fiMOD = phi(mod);
  primeDivisors = factorize(mod);
  powers.resize(primeDivisors.size());
  for (int i = 0; i < powers.size(); ++i) {
    powers[i].resize(MaxN * LOG);
    powers[i][0] = 1;
    for (int j = 1; j < MaxN * LOG; ++j)
      powers[i][j] = (long long)powers[i][j - 1] * primeDivisors[i] % mod;
  }
  for (int i = 1; i < MaxN; ++i) {
    f[i].resize(primeDivisors.size(), 0);
    int x = i;
    for (int j = 0; j < primeDivisors.size(); ++j)
      while (x % primeDivisors[j] == 0) {
        ++f[i][j];
        x /= primeDivisors[j];
      }
    goodPart[i] = x;
  }
  for (int i = 1; i <= n; ++i) cin >> a[i];
  build(1, 1, n);
  int q;
  cin >> q;
  while (q-- > 0) {
    int t;
    cin >> t;
    if (t == 1) {
      int l, r, x;
      cin >> l >> r >> x;
      updateMul(1, 1, n, l, r, x);
    } else if (t == 2) {
      int p, x;
      cin >> p >> x;
      updateDiv(1, 1, n, p, x);
    } else if (t == 3) {
      int l, r;
      cin >> l >> r;
      cout << getAns(1, 1, n, l, r) << '\n';
    }
  }
  return 0;
}
