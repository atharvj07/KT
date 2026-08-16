#include <bits/stdc++.h>
using namespace std;
int main() {
  cin.tie(0);
  ios::sync_with_stdio(false);
  int N;
  scanf("%d", &N);
  vector<int> A(N);
  for (int i = 0; i < N; ++i) scanf("%d", &A[i]);
  int res = 0;
  long long score = 0;
  vector<vector<int>> div(1, A);
  for (int d = 30; d >= 0; --d) {
    vector<vector<int>> nex;
    int mask = 1 << d;
    long long ok = 0, ng = 0;
    for (const auto &v : div) {
      vector<int> zero, one;
      for (auto val : v) {
        if (val & mask) {
          ok += zero.size();
          one.push_back(val);
        } else {
          ng += one.size();
          zero.push_back(val);
        }
      }
      if (!one.empty()) nex.emplace_back(one);
      if (!zero.empty()) nex.emplace_back(zero);
    }
    swap(div, nex);
    score += min(ok, ng);
    if (ok < ng) res += mask;
  }
  printf("%lld %d\n", score, res);
}
