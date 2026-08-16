#include <cstdio>
#include <cstdint>
#include <cstddef>
#include <cassert>
#include <cctype>
#include <vector>
#include <algorithm>
#include <utility>
#include <tuple>
#include <limits>
#include <string>

constexpr intmax_t  operator ""_jd(unsigned long long n) { return static_cast<intmax_t>(n); }
constexpr uintmax_t operator ""_ju(unsigned long long n) { return static_cast<uintmax_t>(n); }
constexpr size_t    operator ""_zu(unsigned long long n) { return static_cast<size_t>(n); }
constexpr ptrdiff_t operator ""_td(unsigned long long n) { return static_cast<ptrdiff_t>(n); }

template <
  typename Monoid,
  typename Container = std::vector<typename Monoid::first_type>
>
class basic_segment_tree {
public:
  using size_type = size_t;
  using first_type = typename Monoid::first_type;
  using second_type = typename Monoid::second_type;
  using value_type = first_type;
  using binary_operation = typename Monoid::binary_operation;
  using external_binary_operation = typename Monoid::external_binary_operation;
  using container = Container;

private:
  size_type M_base_size;
  binary_operation M_op1;
  external_binary_operation M_op2;
  container M_c;

  template <typename Predicate>
  size_type M_search_root(Predicate pred, value_type& x) {
    size_type n = M_base_size;
    size_type l = n;
    size_type r = n+n;
    size_type v = r;
    std::vector<size_type> rs;
    x = M_op1.identity;
    while (l < r) {
      if (l & 1) {
        if (!pred(M_op1(x, M_c[l]))) return l;
        x = M_op1(x, M_c[l++]);
      }
      if (r & 1) rs.push_back(--r);
      l >>= 1;
      r >>= 1;
    }
    while (!rs.empty()) {
      size_type r = rs.back();
      rs.pop_back();
      if (!pred(M_op1(x, M_c[r]))) return r;
      x = M_op1(x, M_c[r]);
    }
    return v;
  }

  template <typename Predicate>
  size_type M_search_leaf(Predicate pred, size_type v, value_type& x) {
    size_type n = M_base_size;
    while (v < n) {
      size_type c = v << 1;
      if (pred(M_op1(x, M_c[c]))) {
        x = M_op1(x, M_c[c]);
        c |= 1;
      }
      v = c;
    }
    return v - n;
  }

public:
  basic_segment_tree() = default;
  basic_segment_tree(basic_segment_tree const&) = default;
  basic_segment_tree(basic_segment_tree&&) = default;

  basic_segment_tree(size_type n, first_type const& x = binary_operation().identity):
    M_base_size(n),
    M_op1(binary_operation()),
    M_op2(external_binary_operation()),
    M_c(n+n, x)
  {
    for (size_type i = n; i--;)
      M_c[i] = M_op1(M_c[i<<1|0], M_c[i<<1|1]);
  }

  template <typename InputIt>
  basic_segment_tree(InputIt first, InputIt last):
    M_base_size(std::distance(first, last)),
    M_op1(binary_operation()),
    M_op2(external_binary_operation()),
    M_c(M_base_size*2)
  {
    for (size_type i = M_base_size; first != last; ++i)
      M_c[i] = *first++;
    for (size_type i = M_base_size; i--;)
      M_c[i] = M_op1(M_c[i<<1|0], M_c[i<<1|1]);
  }

  basic_segment_tree& operator =(basic_segment_tree const&) = default;
  basic_segment_tree& operator =(basic_segment_tree&&) = default;

  void modify(size_type i, second_type const& x) {
    i += M_base_size;
    M_c[i] = M_op2(M_c[i], x);
    while (i > 1) {
      i >>= 1;
      M_c[i] = M_op1(M_c[i<<1|0], M_c[i<<1|1]);
    }
  }

  first_type accumulate(size_type l, size_type r) const {
    first_type resl = M_op1.identity;
    first_type resr = resl;
    l += M_base_size;
    r += M_base_size;
    while (l < r) {
      if (l & 1) resl = M_op1(resl, M_c[l++]);
      if (r & 1) resr = M_op1(M_c[--r], resr);
      l >>= 1;
      r >>= 1;
    }
    return M_op1(resl, resr);
  }

  template <typename Predicate>
  size_type bound(Predicate pred) {
    value_type x;
    size_type root = M_search_root(pred, x);
    return M_search_leaf(pred, root, x);
  }

  first_type operator [](size_t i) const { return M_c[i+M_base_size]; }
};

template <typename Tp>
struct range_xor_single_noop {
  using first_type = Tp;
  using second_type = Tp;
  struct binary_operation {
    first_type identity{0};
    first_type operator ()(first_type const& x, first_type const& y) const {
      return x ^ y;
    }
  };
  struct external_binary_operation {
    first_type operator ()(first_type const& x, second_type const&) const { return x; }
  };
};
template <typename Tp>
struct range_and_single_noop {
  using first_type = Tp;
  using second_type = Tp;
  struct binary_operation {
    first_type identity = ~first_type{0};
    first_type operator ()(first_type const& x, first_type const& y) const {
      return x & y;
    }
  };
  struct external_binary_operation {
    first_type operator ()(first_type const& x, second_type const&) const { return x; }
  };
};
template <typename Tp>
struct range_or_single_noop {
  using first_type = Tp;
  using second_type = Tp;
  struct binary_operation {
    first_type identity{0};
    first_type operator ()(first_type const& x, first_type const& y) const {
      return x | y;
    }
  };
  struct external_binary_operation {
    first_type operator ()(first_type const& x, second_type const&) const { return x; }
  };
};

using tsurai_type = unsigned;

tsurai_type nya(tsurai_type x, tsurai_type y, size_t p) {
  if (p == 0) return x | y;
  if (p == 1) return x & y;
  if (p == 2) return x ^ y;
  assert(false);
}

tsurai_type tsurai(std::string const& s, size_t l, size_t r,
                   std::vector<size_t> const& b0,
                   std::vector<size_t> const& b1,
                   std::vector<size_t> const& b2,
                   std::vector<size_t> const& e0,
                   std::vector<size_t> const& e1,
                   std::vector<size_t> const& e2,
                   std::vector<size_t> const& d0,
                   std::vector<size_t> const& d1,
                   std::vector<size_t> const& d2,
                   basic_segment_tree<range_or_single_noop<tsurai_type>> const& s0,
                   basic_segment_tree<range_and_single_noop<tsurai_type>> const& s1,
                   basic_segment_tree<range_xor_single_noop<tsurai_type>> const& s2,
                   size_t preced) {

  if (!isdigit(s[l])) ++l;
  if (l >= s.length()) return 0;
  if (preced == 3) {
    tsurai_type x = 0;
    for (size_t i = l; i < r && isdigit(s[i]); ++i) x = x*10 + s[i]-'0';
    return x;
  }

  auto const& b = ((preced == 0)? b0 : (preced == 1)? b1:b2);
  auto const& e = ((preced == 0)? e0 : (preced == 1)? e1:e2);
  auto const& d = ((preced == 0)? d0 : (preced == 1)? d1:d2);

  size_t ll = b[l];
  size_t rr = e[r];
  if (ll == rr) {
    tsurai_type xl = tsurai(s, l, ll, b0, b1, b2, e0, e1, e2, d0, d1, d2, s0, s1, s2, preced+1);
    tsurai_type xr = tsurai(s, rr, r, b0, b1, b2, e0, e1, e2, d0, d1, d2, s0, s1, s2, preced+1);
    if (!(l < ll)) return xr;
    if (!(rr < r)) return xl;
    return nya(xl, xr, preced);
  }
  if (ll > rr) {
    return tsurai(s, l, r, b0, b1, b2, e0, e1, e2, d0, d1, d2, s0, s1, s2, preced+1);
  }

  tsurai_type x;
  if (preced == 0) {
    x = s0.accumulate(d[ll], d[rr]);
  } else if (preced == 1) {
    x = s1.accumulate(d[ll], d[rr]);
  } else if (preced == 2) {
    x = s2.accumulate(d[ll], d[rr]);
  }

  if (l < ll) {
    tsurai_type y = tsurai(s, l, ll, b0, b1, b2, e0, e1, e2, d0, d1, d2, s0, s1, s2, preced+1);
    x = nya(x, y, preced);
  }
  if (rr < r) {
    tsurai_type y = tsurai(s, rr, r, b0, b1, b2, e0, e1, e2, d0, d1, d2, s0, s1, s2, preced+1);
    x = nya(x, y, preced);
  }
  return x;
}

std::vector<std::string> const ops = {"|", "&", "^"};
unsigned parse(std::string const& s, size_t& i, size_t preced = 0) {
  if (preced == ops.size()) {
    unsigned res = s[i]-'0';
    while (isdigit(s[++i])) res = res*10+s[i]-'0';
    return res;
  }

  unsigned res = parse(s, i, preced+1);
  while (i < s.length()) {
    char op = s[i];
    if (!std::count(ops[preced].begin(), ops[preced].end(), op)) break;
    unsigned tmp = parse(s, ++i, preced+1);
    if (op == '|') res |= tmp;
    if (op == '&') res &= tmp;
    if (op == '^') res ^= tmp;
  }
  return res;
}

int main() {
  size_t n;
  scanf("%zu", &n);

  char buf[131072];
  scanf("%s", buf);
  std::string s = buf;

  std::vector<tsurai_type> num0, num1, num2;
  tsurai_type cur = 0;
  std::vector<size_t> delim{0};
  for (size_t i = 0; i <= n; ++i) {
    if (isdigit(s[i])) {
      cur = cur*10+s[i]-'0';
    } else {
      num2.push_back(cur);
      cur = 0;
      delim.push_back(i);
    }
  }

  // begin, end
  std::vector<size_t> b0(n+1, n), e0(n+1, 0);  // '|'
  std::vector<size_t> b1(n+1, n), e1(n+1, 0);  // '&'
  std::vector<size_t> b2(n+1, n), e2(n+1, 0);  // '^'
  b0[0] = b1[0] = b2[0] = 0;
  e0[n] = e1[n] = e2[n] = n;

  // index, de-index
  std::vector<size_t> i0{0}, i1{0}, i2{0};
  std::vector<size_t> d0(n+1), d1(n+1), d2(n+1);
  for (size_t i = 0; i < n; ++i) {
    if (s[i] == '^') {
      b2[i+1] = e2[i] = i;
      i2.push_back(i);
    } else if (s[i] == '&') { 
      b2[i+1] = e2[i] = i;
      b1[i+1] = e1[i] = i;
      i2.push_back(i);
      i1.push_back(i);
    } else if (s[i] == '|') {
      b2[i+1] = e2[i] = i;
      b1[i+1] = e1[i] = i;
      b0[i+1] = e0[i] = i;
      i2.push_back(i);
      i1.push_back(i);
      i0.push_back(i);
    }
  }
  i2.push_back(n);
  i1.push_back(n);
  i0.push_back(n);

  for (size_t i = 0; i < i0.size(); ++i) d0[i0[i]] = i;
  for (size_t i = 0; i < i1.size(); ++i) d1[i1[i]] = i;
  for (size_t i = 0; i < i2.size(); ++i) d2[i2[i]] = i;

  for (size_t i = n+1; i-- > 1;) {
    b0[i-1] = std::min(b0[i-1], b0[i]);
    b1[i-1] = std::min(b1[i-1], b1[i]);
    b2[i-1] = std::min(b2[i-1], b2[i]);
  }
  for (size_t i = 1; i <= n; ++i) {
    e0[i] = std::max(e0[i-1], e0[i]);
    e1[i] = std::max(e1[i-1], e1[i]);
    e2[i] = std::max(e2[i-1], e2[i]);
  }

  basic_segment_tree<range_xor_single_noop<tsurai_type>> s2(num2.begin(), num2.end());

  for (size_t i = 1; i < i1.size(); ++i)
    num1.push_back(s2.accumulate(d2[i1[i-1]], d2[i1[i]]));

  basic_segment_tree<range_and_single_noop<tsurai_type>> s1(num1.begin(), num1.end());

  for (size_t i = 1; i < i0.size(); ++i)
    num0.push_back(s1.accumulate(d1[i0[i-1]], d1[i0[i]]));

  basic_segment_tree<range_or_single_noop<tsurai_type>> s0(num0.begin(), num0.end());

  size_t q;
  scanf("%zu", &q);

  for (size_t i = 0; i < q; ++i) {
    size_t l, r;
    scanf("%zu %zu", &l, &r);
    ++r;

    unsigned got = tsurai(s, l, r, b0, b1, b2, e0, e1, e2, d0, d1, d2, s0, s1, s2, 0);
    printf("%u\n", got);
  }
}

