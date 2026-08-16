#include <bits/stdc++.h>
using namespace std;
template <class t, class u>
void chmax(t& first, u second) {
  if (first < second) first = second;
}
template <class t, class u>
void chmin(t& first, u second) {
  if (second < first) first = second;
}
vector<pair<int, int> > first;
int n;
set<int> cand;
void factorise(long long int x) {
  for (int i = 2; i * i < x + 1; i++) {
    if (x % i) continue;
    while (!(x % i)) x /= i;
    cand.insert(i);
  }
  if (x > 1) cand.insert(x);
}
int main() {
  scanf("%d", &n);
  for (int i = int(0); i < int(n); i++) {
    int u, v;
    scanf("%d", &u);
    scanf("%d", &v);
    first.push_back(make_pair(u, v));
  }
  factorise(first[0].first);
  factorise(first[0].second);
  for (int p : cand) {
    bool flag = 1;
    for (int i = int(0); i < int(n); i++)
      if (first[i].first % p != 0 && first[i].second % p != 0) flag = 0;
    if (flag) return !printf("%d\n", p);
  }
  return !printf("-1\n");
}
