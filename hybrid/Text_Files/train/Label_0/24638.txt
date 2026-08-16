#include <bits/stdc++.h>
using namespace std;
int cnt[200005], cn = 0;
vector<int> ara, s, fi, si;
void equilizer(int index) {
  int i = index;
  while (ara[++i] != ara[index] && i < ara.size()) {
    if (ara[i] < ara[index]) {
      s.push_back(1);
      fi.push_back(i + 1);
      si.push_back(i);
    } else {
      s.push_back(2);
      fi.push_back(i + 1);
      si.push_back(i);
    }
    cn++;
  }
  if (i != ara.size()) {
    equilizer(i);
  }
}
int main() {
  int n, a, mx = 0, mx1 = 0, mxi = 0;
  scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    scanf("%d", &a);
    if (mx < a) mx = a;
    cnt[a]++;
    ara.push_back(a);
  }
  for (int i = 0; i <= mx; i++) {
    if (mx1 < cnt[i]) {
      mx1 = cnt[i];
      mxi = i;
    }
  }
  int index = -1;
  while (ara[++index] != mxi)
    ;
  int i = index;
  while (--i >= 0) {
    if (ara[i] < ara[index]) {
      s.push_back(1);
      fi.push_back(i + 1);
      si.push_back(i + 2);
    } else {
      s.push_back(2);
      fi.push_back(i + 1);
      si.push_back(i + 2);
    }
    cn++;
  }
  equilizer(index);
  printf("%d\n", cn);
  for (int j = 0; j < cn; j++) {
    printf("%d %d %d\n", s[j], fi[j], si[j]);
  }
  return 0;
}
