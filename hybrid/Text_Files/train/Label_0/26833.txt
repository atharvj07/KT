#include <bits/stdc++.h>
#pragma GCC optimize("O3")
#pragma GCC target("sse4")
using namespace std;
const int maxn = 111;
int occ[maxn], en[maxn];
int main() {
  int b, d;
  scanf("%d %d", &b, &d);
  string a, c;
  cin >> a >> c;
  for (int e = 0; e < c.size(); e++) {
    int cur_c = e;
    int qtd = 0;
    for (int cur_a = 0; cur_a < a.size(); cur_a++) {
      if (a[cur_a] == c[cur_c]) {
        cur_c++;
      }
      if (cur_c == c.size()) {
        qtd++;
        cur_c = 0;
      }
    }
    occ[e] = qtd;
    en[e] = cur_c;
  }
  int tot = 0;
  int cur_c = 0;
  for (int e = 0; e < b; e++) {
    tot += occ[cur_c];
    cur_c = en[cur_c];
  }
  printf("%d\n", (tot / d));
  return 0;
}
