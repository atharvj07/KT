#include <bits/stdc++.h>
using namespace std;
char s[1111111];
vector<string> v[333333];
int mxlvl = 0;
bool read_comment(int lvl) {
  mxlvl = max(mxlvl, lvl + 1);
  int c = 0;
  scanf("%c", &s[c]);
  if (s[c] == '\n') return false;
  if (s[c] == ',') c = -1;
  do scanf("%c", &s[++c]);
  while (s[c] != ',');
  s[c] = 0;
  v[lvl].push_back(string(s));
  int n;
  scanf("%d", &n);
  for (int i = 0; i < n; i++) (void)read_comment(lvl + 1);
  return true;
}
int main() {
  while (read_comment(0))
    ;
  printf("%d\n", mxlvl);
  for (int i = 0; i < mxlvl; i++) {
    for (const auto &j : v[i]) printf("%s ", j.c_str());
    printf("\n");
  }
  return 0;
}
