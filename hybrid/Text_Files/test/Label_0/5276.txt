#include <bits/stdc++.h>
#pragma GCC optimize("Ofast")
#pragma GCC optimization("unroll-loops")
std::pair<int, int> DR[] = {{-1, 0}, {0, 1},   {1, 0}, {0, -1},
                            {-1, 1}, {-1, -1}, {1, 1}, {1, -1}};
using namespace std;
const long long mod = 998244353;
long long gcd(long long a, long long b) {
  if (b > a) swap(b, a);
  if (b == 0) return a;
  return gcd(b, a % b);
}
long long bexp(long long num, long long e) {
  long long ans = 1;
  while (e > 0) {
    if (e & 1) {
      ans *= num;
    }
    num *= num;
    e >>= 1;
  }
  return ans;
}
long long mexp(long long num, long long e) {
  long long ans = 1;
  while (e > 0) {
    if (e & 1) {
      ans = (ans * num) % mod;
    }
    num = (num * num) % mod;
    e >>= 1;
  }
  return ans % mod;
}
long long modinv(long long a) { return mexp(a, mod - 2); }
bool check(vector<int> &a, int st, int x, int &k) {
  int j = 0;
  for (long long i = 0; i < (a.size()); i++) {
    if (j < k && (((j % 2) == st && a[i] <= x) || ((j % 2) == 1 - st))) {
      j++;
      if (j == k) break;
    }
  }
  return (j == k);
}
void solve() {
  int n, k;
  cin >> n >> k;
  vector<int> a(n);
  for (long long i = 0; i < (n); i++) {
    cin >> a[i];
  };
  int l = 0, r = 1e9 + 5;
  while (l < r) {
    int mid = (l + r) >> 1;
    if (check(a, 0, mid, k) || check(a, 1, mid, k)) {
      r = mid;
    } else
      l = mid + 1;
  }
  cout << (l) << endl;
  ;
}
int main() {
  cin.tie(NULL);
  cout.tie(NULL);
  ios::sync_with_stdio(false);
  int t = 1;
  for (long long T = 1; T <= (t); T++) {
    solve();
  }
  return 0;
}
