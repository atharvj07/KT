#include <bits/stdc++.h>
using namespace std;
template <class T>
void chmax(T &a, T b) {
  if (a < b) a = b;
}
template <class T>
void chmin(T &a, T b) {
  if (a > b) a = b;
}
constexpr long long INF = 1000000000000000000;
constexpr long long mod = 1000000007;
constexpr double eps = 1e-8;
const double pi = acos(-1);
long long dx[] = {0, 1, 0, -1}, dy[] = {1, 0, -1, 0};
long long Random(long long mi, long long ma) {
  random_device rnd;
  mt19937 mt(rnd());
  uniform_int_distribution<long long> engine(mi, ma);
  return engine(mt);
}
long long gcd(long long a, long long b) {
  if (b == 0) return a;
  return gcd(b, a % b);
}
long long lcm(long long a, long long b) { return a / gcd(a, b) * b; }
bool prime(long long a) {
  if (a == 1) return false;
  for (long long i = 2; i * i <= a; i++) {
    if (a % i == 0) return false;
  }
  return true;
}
long long modpow(long long a, long long b) {
  if (b == 0) return 1;
  if (b % 2) return modpow(a, b - 1) * a % mod;
  long long memo = modpow(a, b / 2);
  return memo * memo % mod;
}
vector<long long> kaijo, invkaijo;
void init_fact(long long n) {
  kaijo.resize(n + 1);
  invkaijo.resize(n + 1);
  kaijo[0] = 1;
  for (long long i = 1; i <= n; i++) {
    kaijo[i] = kaijo[i - 1] * i;
    kaijo[i] %= mod;
  }
  for (long long i = 0; i < n + 1; i++) invkaijo[i] = modpow(kaijo[i], mod - 2);
}
long long comb(long long a, long long b) {
  if (a < b) return 0;
  if (a < 0 || b < 0) return 0;
  return kaijo[a] * invkaijo[a - b] % mod * invkaijo[b] % mod;
}
long long inv(long long x) {
  x = modpow(x, mod - 2);
  return x;
}
void solve() {
  long long n, k, ans = INF;
  bool flag = false;
  cin >> n >> k;
  {
    if (2 * n % (k + 1) == 0) {
      long long hoge = 2 * n / (k + 1);
      if (hoge >= k) {
        hoge -= k;
        if (hoge % 2 == 0) {
          long long sum = hoge / 2;
          string s = "";
          if (sum <= 9 - k) {
            ans = sum;
            flag = true;
            goto ok;
          }
          sum -= (9 - k);
          while (sum > 9) {
            sum -= 9;
            s += '9';
          }
          s += (char)('0' + 9 - k);
          s = (char)('0' + sum) + s;
          ans = stoll(s);
          flag = true;
        }
      }
    }
  }
ok:;
  {
    for (long long l = 1; l <= 16; l++) {
      for (long long m = 0; m < k; m++) {
        long long hoge = 2 * n - (k + 1) * k - 18 * l * (m - k);
        if (hoge % (2 * (k + 1)) == 0) {
          long long sum = hoge / 2 / (k + 1);
          if (sum >= 9 - m) {
            sum -= (9 - m);
            string s = "";
            if (sum >= 9 * (l - 1)) {
              for (long long _ = 0; _ < l - 1; _++) s += '9';
              sum -= 9 * (l - 1);
            }
            if (sum <= 8) {
              s = (char)('0' + sum) + s;
            } else {
              sum -= 8;
              s = '8' + s;
              while (sum > 9) {
                sum -= 9;
                s = '9' + s;
              }
              s = (char)('0' + sum) + s;
            }
            s += (char)('0' + 9 - m);
            long long S = stoll(s);
            long long cnt = 0;
            long long t = S;
            while (t % 10 != 9) t++;
            while (t) {
              if (t % 10 == 9)
                cnt++;
              else
                break;
              t /= 10;
            }
            if (cnt != l) continue;
            if (flag == false) {
              flag = true;
              ans = S;
            } else {
              chmin(ans, S);
            }
          }
        }
      }
    }
  }
  if (flag == false)
    cout << -1 << endl;
  else
    cout << ans << endl;
}
signed main() {
  cin.tie(0);
  ios::sync_with_stdio(false);
  long long t;
  cin >> t;
  while (t--) solve();
  return 0;
}
