#include <bits/stdc++.h>
using namespace std;
int n;
int ans[300003];
pair<int, int> A[300003];
vector<pair<int, int> > vec;
int state(int first) { return (first < 0) ? -1 : +1; }
int main() {
  scanf("%d", &n);
  for (int i = 0; i < n; i++) scanf("%d %d", &A[i].first, &A[i].second);
  for (int i = 0; i < n; i++) {
    int nxt = (i + 1) % n;
    int bck = (i - 1 + n) % n;
    if (state(A[i].first - A[bck].first) != state(A[nxt].first - A[i].first) ||
        state(A[i].second - A[bck].second) !=
            state(A[nxt].second - A[i].second))
      vec.push_back(A[i]);
  }
  int nn = vec.size();
  if (vec.size() <= 3) {
    for (int i = 0; i < nn; i++)
      ans[3] += abs(vec[i].first - vec[(i + 1) % nn].first) +
                abs(vec[i].second - vec[(i + 1) % nn].second);
    ans[4] = ans[3];
  } else {
    for (int i = 0; i < nn; i++)
      ans[4] += abs(vec[i].first - vec[(i + 1) % nn].first) +
                abs(vec[i].second - vec[(i + 1) % nn].second);
    for (int i = 0; i < nn; i++) {
      for (int j = i + 1; j < nn; j++) {
        for (int k = 0; k < n; k++) {
          if (A[k] == vec[i] || A[k] == vec[j])
            continue;
          else {
            int b1 = max({A[k].first, vec[i].first, vec[j].first}) -
                     min({A[k].first, vec[i].first, vec[j].first});
            int b2 = max({A[k].second, vec[i].second, vec[j].second}) -
                     min({A[k].second, vec[i].second, vec[j].second});
            ans[3] = max(ans[3], 2 * (b1 + b2));
          }
        }
      }
    }
  }
  for (int i = 5; i <= n; i++) ans[i] = ans[4];
  for (int i = 3; i <= n; i++) printf("%d%c", ans[i], (i == n) ? '\n' : ' ');
}
