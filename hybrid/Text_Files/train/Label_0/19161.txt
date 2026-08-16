
/* -------------------------------- Template -------------------------------- */

#include <algorithm>
#include <array>
#include <bitset>
#include <cassert>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstring>
#include <deque>
#include <functional>
#include <iomanip>
#include <locale>
#include <iostream>
#include <map>
#include <memory>
#include <new>
#include <numeric>
#include <queue>
#include <random>
#include <set>
#include <sstream>
#include <string>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

#define REP(i,n) for(int i=0;i<(int)(n);i++)
#define ALL(x) (x).begin(),(x).end()

using ll = long long;
using ld = long double;

template <typename T> T &chmin(T &a, const T &b) { return a = std::min(a, b); }
template <typename T> T &chmax(T &a, const T &b) { return a = std::max(a, b); }
template <typename T> int len(const T &x) { return x.size(); }

// template<typename T> constexpr T inf = [](){ assert(false); };
// template<> constexpr int inf<int> = 1e9;
// template<> constexpr ll inf<ll> = 1e18;
// template<> constexpr ld inf<ld> = 1e30;

struct yes_no : std::numpunct<char> {
  string_type do_truename()  const { return "Yes"; }
  string_type do_falsename() const { return "No"; }
};

void solve();

int main() {
  std::locale loc(std::locale(), new yes_no);
  std::cout << std::boolalpha << std::setprecision(12) << std::fixed;
  std::cout.imbue(loc);
  solve();
  return 0;
}

using namespace std;

/* -------------------------------- Library -------------------------------- */

/* ---------------------------------- Main ---------------------------------- */

int A[128000], B[128000];

void solve() {
  int N, Q;
  cin >> N >> Q;
  A[1] = 1;
  B[1] = 1;
  B[2] = 1;
  int p = 1;
  REP(i,Q) {
    int L, R;
    cin >> L >> R;
    swap(A[L], A[R]);
    swap(B[L], B[R]);
    if (A[L]) p = L;
    if (A[R]) p = R;
    B[p-1] = 1;
    B[p+1] = 1;
  }
  cout << accumulate(B + 1, B + N + 1, 0) << endl;
  return;
}
