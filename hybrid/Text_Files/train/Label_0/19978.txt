#include <bits/stdc++.h>
using namespace std;
const int maxn = 2e5 + 100;
int n, m, p, number[maxn];
vector<int> ans;
map<int, int> result;
void compute(int start);
int main() {
  int num;
  scanf("%d%d%d", &n, &m, &p);
  for (int i = 1; i <= n; i++) scanf("%d", &number[i]);
  for (int i = 1; i <= m; i++) {
    scanf("%d", &num);
    result[num]++;
  }
  for (int i = 1; i <= p; i++) compute(i);
  sort(ans.begin(), ans.end());
  printf("%d\n", ans.size());
  for (int i = 0; i < ans.size(); i++) {
    if (i) printf(" ");
    printf("%d", ans[i]);
  }
  if (ans.size()) printf("\n");
  return 0;
}
void compute(int start) {
  map<int, int> now;
  queue<int> last;
  for (int i = start; i <= n; i += p) {
    last.push(number[i]);
    now[number[i]]++;
    if (last.size() == m) {
      if (now == result) ans.push_back(i - (m - 1) * p);
      int dark = last.front();
      last.pop();
      now[dark]--;
      if (!now[dark]) now.erase(dark);
    }
  }
}
