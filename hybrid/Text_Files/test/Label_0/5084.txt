#include <bits/stdc++.h>
#pragma GCC target("pclmul")
using ul = std::uint32_t;
using ull = std::uint64_t;
using li = std::int32_t;
using ll = std::int64_t;
using uss = std::uint8_t;
const ul maxn = 1e5;
char str[maxn + 2];
ul scb[maxn + 1];
ul sca[maxn + 1];
ul tcb[maxn + 1];
ul tca[maxn + 1];
ul q;
int main() {
  std::scanf("%s", str + 1);
  for (ul i = 1; str[i]; ++i) {
    if (str[i] == 'A') {
      sca[i] = sca[i - 1] + 1;
      scb[i] = scb[i - 1];
    } else {
      scb[i] = scb[i - 1] + 1;
    }
  }
  std::scanf("%s", str + 1);
  for (ul i = 1; str[i]; ++i) {
    if (str[i] == 'A') {
      tca[i] = tca[i - 1] + 1;
      tcb[i] = tcb[i - 1];
    } else {
      tcb[i] = tcb[i - 1] + 1;
    }
  }
  std::scanf("%u", &q);
  for (ul i = 1; i <= q; ++i) {
    ul a, b, c, d;
    std::scanf("%u%u%u%u", &a, &b, &c, &d);
    ul sb = scb[b] - scb[a - 1];
    ul tb = tcb[d] - tcb[c - 1];
    ul sa = std::min(sca[b], b - a + 1);
    ul ta = std::min(tca[d], d - c + 1);
    if ((sb ^ tb) & 1) {
      std::putchar('0');
      continue;
    }
    if (sa < ta) {
      std::putchar('0');
      continue;
    }
    if ((sa - ta) % 3 == 0 && sb > tb) {
      std::putchar('0');
      continue;
    }
    if ((sa - ta) % 3 != 0 && sb + 2 > tb) {
      std::putchar('0');
      continue;
    }
    if (sb == 0 && tb != 0 && sa == ta) {
      std::putchar('0');
      continue;
    }
    std::putchar('1');
  }
  std::putchar('\n');
  return 0;
}
