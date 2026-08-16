#include <bits/stdc++.h>
using namespace std;
const int MAXN = 3e5 + 7;
pair<int, int> c[MAXN];
bool cmp(const pair<int, int> &p1, const pair<int, int> &p2) {
  return p1.second < p2.second;
}
int main() {
  int n, x1, x2;
  cin >> n >> x1 >> x2;
  for (int i = 1; i <= n; i++) {
    c[i].first = i;
    scanf("%d", &c[i].second);
  }
  sort(c + 1, c + n + 1, cmp);
  for (int i = 1; i <= n; i++) {
    int use1 = (x1 + c[i].second - 1) / c[i].second;
    if (i + use1 > n) continue;
    int use2 = (x2 + c[i + use1].second - 1) / c[i + use1].second;
    if (i + use1 + use2 > n + 1) continue;
    puts("Yes");
    cout << use1 << ' ' << use2 << endl;
    for (int j = i; j < i + use1; j++) {
      printf("%d ", c[j].first);
    }
    puts("");
    for (int j = i + use1; j < i + use1 + use2; j++) {
      printf("%d ", c[j].first);
    }
    puts("");
    return 0;
  }
  for (int i = 1; i <= n; i++) {
    int use2 = (x2 + c[i].second - 1) / c[i].second;
    if (i + use2 > n) continue;
    int use1 = (x1 + c[i + use2].second - 1) / c[i + use2].second;
    if (i + use1 + use2 > n + 1) continue;
    puts("Yes");
    cout << use1 << ' ' << use2 << endl;
    for (int j = i + use2; j < i + use1 + use2; j++) {
      printf("%d ", c[j].first);
    }
    puts("");
    for (int j = i; j < i + use2; j++) {
      printf("%d ", c[j].first);
    }
    puts("");
    return 0;
  }
  puts("No");
  return 0;
}
