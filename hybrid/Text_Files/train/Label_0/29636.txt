#include <bits/stdc++.h>
using namespace std;
const int L = 6;
const int N = 1e5 + 5;
int A[L + 1];
int licz[N];
int main() {
  for (int i = 1; i <= L; i++) scanf("%d", &A[i]);
  int n;
  scanf("%d", &n);
  vector<pair<int, int>> broom;
  for (int i = 1; i <= n; i++) {
    int x;
    scanf("%d", &x);
    for (int j = 1; j <= L; j++) {
      if (x > A[j]) broom.push_back({x - A[j], i});
    }
  }
  sort(broom.begin(), broom.end());
  int not_covered = n;
  int i = 0;
  int j = -1;
  while (not_covered > 0) {
    j++;
    if (licz[broom[j].second] == 0) not_covered--;
    licz[broom[j].second]++;
  }
  int res = broom[j].first - broom[i].first;
  while (i < int(broom.size())) {
    licz[broom[i].second]--;
    while (j < int(broom.size()) - 1 && licz[broom[i].second] == 0) {
      j++;
      licz[broom[j].second]++;
    }
    if (licz[broom[i].second] == 0) break;
    i++;
    res = min(res, broom[j].first - broom[i].first);
  }
  printf("%d\n", res);
}
