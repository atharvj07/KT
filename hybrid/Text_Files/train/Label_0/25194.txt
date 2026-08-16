#include <bits/stdc++.h>
using namespace std;
const int INF = (int)2e9 + 7;
const char noAns[] = "Incorrect sequence";
int n, m;
int a[100100];
int readInt(void) {
  char s[22];
  scanf("%s", s);
  if (s[0] == '?') return (INF);
  int val = 0;
  if (s[0] == '-') {
    for (int i = (1), _b = (strlen(s) - 1); i <= _b; i = i + 1)
      val = val * 10 + s[i] - '0';
    return (-val);
  } else {
    for (int i = 0, _n = (strlen(s)); i < _n; i = i + 1)
      val = val * 10 + s[i] - '0';
    return (val);
  }
}
void init(void) {
  n = readInt();
  m = readInt();
  for (int i = 0, _n = (n); i < _n; i = i + 1) a[i] = readInt();
}
void noAnswer(void) {
  printf("%s\n", noAns);
  exit(0);
}
void fillSeq(vector<int> &v, int l, int r) {
  int minVal = l == 0 ? -INF : v[l - 1] + 1;
  int maxVal = r == (int)v.size() - 1 ? INF : v[r + 1] - 1;
  if (r - l + 1 > 1LL + maxVal - minVal) noAnswer();
  if (minVal >= 0) {
    for (int i = (l), _b = (r); i <= _b; i = i + 1) v[i] = minVal++;
  } else if (maxVal <= 0) {
    for (int i = (r), _a = (l); i >= _a; i = i - 1) v[i] = maxVal--;
  } else {
    int pos = 0;
    int neg = -1;
    for (int i = (l), _b = (r); i <= _b; i = i + 1) {
      if (pos > maxVal)
        v[i] = neg--;
      else if (neg < minVal)
        v[i] = pos++;
      else if (-neg < pos)
        v[i] = neg--;
      else
        v[i] = pos++;
    }
    sort(v.begin() + l, v.begin() + r + 1);
  }
}
void process(void) {
  for (int i = 0, _n = (m); i < _n; i = i + 1) {
    vector<int> v, fst, lst;
    for (int j = i; j < n; j = j + m) v.push_back(a[j]);
    for (int j = 0, _n = (v.size()); j < _n; j = j + 1)
      if (v[j] >= INF) {
        if (j == 0 || v[j - 1] < INF) fst.push_back(j);
        if (j == (int)v.size() - 1 || v[j + 1] < INF) lst.push_back(j);
      }
    for (int j = 0, _n = (fst.size()); j < _n; j = j + 1)
      fillSeq(v, fst[j], lst[j]);
    int id = 0;
    for (int j = i; j < n; j = j + m) a[j] = v[id++];
  }
  for (int i = 0, _n = (n); i < _n; i = i + 1)
    if (i + m < n && a[i] >= a[i + m]) noAnswer();
  for (int i = 0, _n = (n); i < _n; i = i + 1) printf("%d ", a[i]);
  printf("\n");
}
int main(void) {
  init();
  process();
  return 0;
}
