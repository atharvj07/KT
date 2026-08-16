#include <bits/stdc++.h>
using namespace std;
int n, l;
vector<int> v;
int main() {
  scanf("%d %d", &n, &l);
  for (int i = 0; i < n; i++) {
    int x;
    scanf("%d", &x);
    if (x >= l) v.push_back(x);
  }
  sort(v.begin(), v.end());
  int ms = 0;
  for (int i = 0; i < v.size(); i++) {
    int count = 0;
    for (int j = i; j < v.size(); j++) count += v[j] / v[i];
    ms = max(ms, v[i] * count);
  }
  int count = 0;
  for (int j = 0; j < v.size(); j++) count += v[j] / l;
  ms = max(ms, l * count);
  printf("%d", ms);
  return 0;
}
