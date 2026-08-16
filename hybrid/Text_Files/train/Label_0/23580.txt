#include <bits/stdc++.h>
#pragma comment(linker, "/STACK:512000000")
using namespace std;
void solve();
void precalc();
clock_t start;
int testNumber = 1;
bool todo = true;
int main() {
  start = clock();
  int t = 1;
  cout.sync_with_stdio(0);
  cin.tie(0);
  precalc();
  cout.precision(10);
  cout << fixed;
  int testNum = 1;
  while (t--) {
    solve();
    ++testNumber;
  }
  return 0;
}
template <typename T>
T binpow(T q, T w, T mod) {
  if (!w) return 1 % mod;
  if (w & 1) return q * 1LL * binpow(q, w - 1, mod) % mod;
  return binpow(q * 1LL * q % mod, w / 2, mod);
}
void precalc() {}
template <typename T>
T gcd(T q, T w) {
  while (w) {
    q %= w;
    swap(q, w);
  }
  return q;
}
template <typename T>
T lcm(T q, T w) {
  return q / gcd(q, w) * w;
}
const long long L = 61;
const long long C = 500050;
vector<bitset<C>> sets(L);
bitset<C> zero, bad;
void solve() {
  long long n;
  cin >> n;
  vector<long long> a(n), b(n);
  for (long long i = 0; i < n; ++i) {
    cin >> a[i] >> b[i];
    for (long long j = 0; j < L; ++j) {
      bool bit_a = bool(a[i] & (1LL << j));
      bool bit_b = bool(b[i] & (1LL << j));
      if (bit_b) {
        sets[j].flip(n);
      }
      if (bit_a != bit_b) {
        sets[j].flip(i);
      }
    }
  }
  bad.flip(n);
  long long rk = 0;
  vector<long long> first_bits(L, -1);
  for (long long i = 0; i < L; ++i) {
    for (long long j = 0; j < i; ++j) {
      long long cur_bit = first_bits[j];
      if (cur_bit == -1) {
        continue;
      }
      if (sets[i][cur_bit]) {
        sets[i] ^= sets[j];
      }
    }
    if (sets[i] == bad) {
      cout << "1/1\n";
      return;
    }
    if (sets[i] == zero) {
      continue;
    }
    ++rk;
    for (long long j = 0; j < n; ++j) {
      if (sets[i][j]) {
        first_bits[i] = j;
        break;
      }
    }
  }
  unsigned long long res = 1;
  for (long long i = 0; i < rk; ++i) {
    res = res * 2;
  }
  cout << res - 1 << "/" << res << "\n";
}
