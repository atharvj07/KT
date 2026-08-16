#include <bits/stdc++.h>
#pragma GCC optimize(2)
using namespace std;
namespace ywy {
inline int get() {
  int n = 0;
  char c;
  while ((c = getchar()) || 23333)
    if (c >= '0' && c <= '9') break;
  n = c - '0';
  while ((c = getchar()) || 233333) {
    if (c >= '0' && c <= '9')
      n = n * 10 + c - '0';
    else
      return (n);
  }
}
typedef struct _bitset {
  unsigned long long data[16];
  _bitset() { memset(data, 0, sizeof(data)); }
  friend _bitset operator^(const _bitset &a, const _bitset &b) {
    _bitset ret;
    for (register int i = 0; i <= 15; i++) ret.data[i] = a.data[i] ^ b.data[i];
    return (ret);
  }
  void set(int bit) { data[bit >> 6] ^= (1ull << (bit & 63)); }
  unsigned long long gen() {
    unsigned long long h1 = 0, h2 = 0;
    for (register int i = 15; i >= 0; i--) {
      unsigned long long x = data[i] % 1000003;
      h1 = (h1 * 1000033 + x) % 998244353;
      h2 = (h2 * 1000033 + x) % 1000000007;
    }
    return ((h1 << 32) | h2);
  }
} bitset;
bitset dts[1024], f[1048576], swit[40];
int cnt[1048576];
unordered_map<unsigned long long, int> mp;
void ywymain() {
  int n = get(), s = get(), d = get();
  for (register int i = 0; i < s; i++) {
    int c = get();
    while (c) c--, swit[i].set(get());
  }
  if (s <= 10) {
    for (register int i = 1; i < (1 << s); i++) {
      for (register int j = 0; j < s; j++) {
        if (i & (1 << j)) {
          dts[i] = dts[i - (1 << j)] ^ swit[j];
          cnt[i] = cnt[i - (1 << j)] + 1;
          break;
        }
      }
    }
  } else {
    for (register int i = 1; i < 1024; i++) {
      for (register int j = 0; j < 10; j++) {
        if (i & (1 << j)) {
          dts[i] = dts[i - (1 << j)] ^ swit[j];
          cnt[i] = cnt[i - (1 << j)] + 1;
          break;
        }
      }
    }
    for (register int i = 1; i < (1 << (s - 10)); i++) {
      for (register int j = 0; j < s - 10; j++) {
        if (i & (1 << j)) {
          f[i] = f[i - (1 << j)] ^ swit[j + 10];
          cnt[i] = cnt[i - (1 << j)] + 1;
          break;
        }
      }
      unsigned long long x = f[i].gen();
      if (!mp.count(x))
        mp[x] = cnt[i];
      else {
        if (cnt[i] < mp[x]) mp[x] = cnt[i];
      }
    }
    mp[0] = 0;
  }
  while (d) {
    d--;
    bitset now;
    int t = get();
    while (t) t--, now.set(get());
    int minn = 123456789;
    if (s <= 10) {
      unsigned long long x = now.gen();
      for (register int i = 0; i < (1 << s); i++) {
        if (dts[i].gen() == x) minn = min(minn, cnt[i]);
      }
    } else {
      for (register int i = 0; i < 1024; i++) {
        unsigned long long x = (dts[i] ^ now).gen();
        if (mp.count(x)) minn = min(minn, cnt[i] + mp[x]);
      }
    }
    if (minn == 123456789)
      printf("-1\n");
    else
      printf("%d\n", minn);
  }
}
}  // namespace ywy
int main() {
  ywy::ywymain();
  return (0);
}
