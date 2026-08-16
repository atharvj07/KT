#include <bits/stdc++.h>
using std::abs;
using std::array;
using std::cerr;
using std::cin;
using std::cout;
using std::generate;
using std::get;
using std::make_pair;
using std::make_tuple;
using std::map;
using std::max;
using std::max_element;
using std::min;
using std::min_element;
using std::pair;
using std::queue;
using std::reverse;
using std::set;
using std::sort;
using std::string;
using std::swap;
using std::tuple;
using std::unique;
using std::vector;
template <typename T>
T input() {
  T res;
  cin >> res;
  {};
  return res;
}
template <typename IT>
void input_seq(IT b, IT e) {
  std::generate(b, e,
                input<typename std::remove_reference<decltype(*b)>::type>);
}
int main() {
  std::iostream::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);
  for (int tc = input<int>(); tc; --tc) {
    int64_t n = input<int64_t>();
    int64_t mx = 0;
    int64_t prev = -2e9;
    for (int64_t i = 0; i < n; ++i) {
      int64_t x = input<int64_t>();
      if (prev > x)
        mx = max(mx, prev - x);
      else
        prev = x;
    }
    if (not mx)
      cout << "0\n";
    else {
      int64_t rs = 0;
      while (mx > ((int64_t)2 << rs) - 1) ++rs;
      cout << rs + 1 << "\n";
    }
  }
  return 0;
}
