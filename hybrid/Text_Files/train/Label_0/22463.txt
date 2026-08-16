#include <bits/stdc++.h>
using namespace std;
namespace FFT {
template <typename U>
struct RootsOfUnity {
  using Complex = complex<U>;
  static std::vector<Complex> roots[32];
  static bool initialized[32];
  static void initialize_to(long long w) {
    assert(w > 0 && w == (w & -w));
    long long lg = 31 - __builtin_clz(w);
    static const U PI = std::acos(static_cast<U>(-1));
    for (long long bit = 1; bit <= lg; ++bit) {
      if (initialized[bit]) continue;
      roots[bit].resize((1 << bit) + 1);
      for (long long j = 0; j <= (1 << bit); ++j) {
        roots[bit][j] = Complex(std::cos(2 * PI * j / (1 << bit)),
                                std::sin(2 * PI * j / (1 << bit)));
      }
      initialized[bit] = true;
    }
  }
};
template <typename U>
bool RootsOfUnity<U>::initialized[32];
template <typename U>
std::vector<complex<U>> RootsOfUnity<U>::roots[32];
using Complex = complex<double>;
const double PI = acos(-1);
void DiscreteFourier(vector<Complex> &a, bool invert) {
  long long n = a.size();
  for (long long i = 1, j = 0; i < n; i++) {
    long long bit = n >> 1;
    for (; j & bit; bit >>= 1) {
      j ^= bit;
    }
    j ^= bit;
    if (i < j) {
      swap(a[i], a[j]);
    }
  }
  for (long long len = 2; len <= n; len <<= 1) {
    for (long long i = 0; i < n; i += len) {
      for (long long j = 0; j < len / 2; j++) {
        long long ind = (invert ? len - j : j);
        Complex w = RootsOfUnity<double>::roots[31 - __builtin_clz(len)][ind];
        Complex u = a[i + j], v = a[i + j + len / 2] * w;
        a[i + j] = u + v;
        a[i + j + len / 2] = u - v;
      }
    }
  }
  if (invert) {
    for (Complex &x : a) {
      x /= n;
    }
  }
}
vector<long long> Convolve(const vector<long long> &a,
                           const vector<long long> &b) {
  long long n = 1;
  while (n < a.size() + b.size()) n <<= 1;
  RootsOfUnity<double>::initialize_to(n);
  vector<Complex> fa(a.begin(), a.end());
  vector<Complex> fb(b.begin(), b.end());
  fa.resize(n), fb.resize(n);
  DiscreteFourier(fa, false);
  DiscreteFourier(fb, false);
  for (long long i = 0; i < n; i++) fa[i] *= fb[i];
  DiscreteFourier(fa, true);
  vector<long long> result(a.size() + b.size());
  for (long long i = 0; i < a.size() + b.size(); i++)
    result[i] = llround(fa[i].real());
  return result;
}
};  // namespace FFT
long long cnt[500005];
vector<long long> go(long long l, long long r) {
  if (l == r) {
    vector<long long> v;
    for (long long i = (0); i <= (cnt[l]); i++) v.push_back(1);
    return v;
  }
  vector<long long> v1 = go(l, (l + r) / 2);
  vector<long long> v2 = go((l + r) / 2 + 1, r);
  auto ret = FFT::Convolve(v1, v2);
  for (long long &z : ret) z %= 1009;
  return ret;
}
int32_t main() {
  cin.tie(0);
  ios_base::sync_with_stdio(0);
  long long n, m, k;
  cin >> n >> m >> k;
  for (long long i = (1); i <= (n); i++) {
    long long x;
    cin >> x;
    cnt[x]++;
  }
  cout << go(1, m)[k];
  return 0;
}
