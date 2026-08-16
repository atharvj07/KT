#include <bits/stdc++.h>
using namespace std;
const long nmax = 1e5 + 3;
deque<long> dq;
string s;
long m, c[nmax], a[28];
long cc(char x) { return (int(x) - int('a')); }
int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cin >> m;
  cin >> s;
  char mx = 'a';
  long i, j;
  i = 0;
  while (i + m - 1 < s.length()) {
    long t = i;
    for (j = i + 1; j < i + m; j++)
      if (s[j] <= s[t]) t = j;
    c[t] = 1;
    mx = max(mx, s[t]);
    a[cc(s[t])] += 1;
    i = t + 1;
  }
  for (i = 0; i < s.length(); i++)
    if (s[i] < mx && c[i] == 0) a[cc(s[i])] += 1;
  for (char ch = 'a'; ch <= 'z'; ch++)
    for (i = 1; i <= a[cc(ch)]; i++) cout << ch;
}
