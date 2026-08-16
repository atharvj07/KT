#include <bits/stdc++.h>
using namespace std;
const int maxn = 107;
char str[maxn];
set<char> s;
int main() {
  s.insert('A');
  s.insert('E');
  s.insert('I');
  s.insert('O');
  s.insert('U');
  s.insert('Y');
  while (~scanf("%s", str + 1)) {
    int len = strlen(str + 1);
    int pos = 0;
    int ans = -1;
    for (int i = 1; i <= len; ++i) {
      if (s.count(str[i])) {
        ans = max(ans, i - pos);
        pos = i;
      }
    }
    ans = max(ans, len + 1 - pos);
    printf("%d\n", ans);
  }
  return 0;
}
