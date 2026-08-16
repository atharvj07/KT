#include <bits/stdc++.h>
using namespace std;
int n, pr[1 << 17], id, en[1 << 17];
char cmd[1 << 17], s[1 << 17];
string s1[1 << 17], s2[1 << 17], exc;
int st[1 << 17], ss;
int main() {
  scanf("%d\n", &n);
  int top = 0;
  for (int x = 0; x < n; x++) {
    gets(s);
    int i = 0;
    while (s[i] == ' ') i++;
    if (s[i] == 't' && s[i + 1] == 'r') {
      cmd[x] = 1;
    }
    if (s[i] == 't' && s[i + 1] == 'h') {
      id = x;
      i += 5;
      while (s[i] == ' ') i++;
      i++;
      while (s[i] == ' ') i++;
      int j = i;
      while (s[j] != ' ' && s[j] != ')' && s[j] != ',') j++;
      exc = string(s + i, s + j);
    }
    if (s[i] == 'c') {
      cmd[x] = 2;
      i += 5;
      while (s[i] == ' ') i++;
      i++;
      while (s[i] == ' ') i++;
      int j = i;
      while (s[j] != ' ' && s[j] != ')' && s[j] != ',') j++;
      s1[x] = string(s + i, s + j);
      i = j;
      while (s[i] != '"') i++;
      j = i + 1;
      while (s[j] != '"') j++;
      s2[x] = string(s + i + 1, s + j);
    }
  }
  for (int i = 0; i < n; i++) {
    if (!cmd[i]) continue;
    if (cmd[i] == 2) {
      ss--;
      en[st[ss]] = i;
    } else {
      if (ss)
        pr[i] = st[ss - 1];
      else
        pr[i] = -1;
      st[ss++] = i;
    }
  }
  int cp = id;
  while (cp >= 0 && (cmd[cp] != 1 || en[cp] <= id)) cp--;
  while (cp >= 0) {
    int end = en[cp];
    if (s1[end] == exc) {
      puts(s2[end].c_str());
      return 0;
    }
    cp = pr[cp];
  }
  puts("Unhandled Exception");
  return 0;
}
