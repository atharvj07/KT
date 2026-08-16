#include <bits/stdc++.h>
using namespace std;
char s[100020], t[100020];
int p[1 << 8];
inline int find(const int x) { return p[x] == x ? x : p[x] = find(p[x]); }
vector<pair<char, char> > v;
int main(void) {
  int n;
  int i;
  int o;
  scanf("%d", &n);
  scanf("%s", s);
  scanf("%s", t);
  for (i = 'a'; i <= 'z'; i++) p[i] = i;
  for (i = o = 0; i < n; i++)
    if (find(s[i]) != find(t[i])) {
      v.push_back(make_pair(s[i], t[i]));
      p[find(s[i])] = find(t[i]);
    }
  printf("%d\n", (signed)v.size());
  for (i = 0; i < (signed)v.size(); i++)
    printf("%c %c\n", v.at(i).first, v.at(i).second);
  return 0;
}
