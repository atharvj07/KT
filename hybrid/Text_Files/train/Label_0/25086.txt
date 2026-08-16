#include <bits/stdc++.h>
const long long MOD = 1000000007;
using namespace std;
char s[110];
vector<int> ans;
int main() {
  int n;
  scanf("%d", &n);
  scanf("%s", s);
  for (int i = 0; i < n;) {
    int x = 0;
    if (s[i] == 'B') {
      while (i < n && s[i] == 'B') ++i, ++x;
      ans.push_back(x);
    } else
      ++i;
  }
  printf("%d\n", ans.size());
  for (int i = 0; i < ans.size(); ++i) printf("%d ", ans[i]);
  printf("\n");
  return 0;
}
