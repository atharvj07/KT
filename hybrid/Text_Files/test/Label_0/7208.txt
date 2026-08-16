#include <bits/stdc++.h>
using namespace std;
vector<pair<long double, int> > x;
const long double PI = 2 * acosl(0);
int main() {
  int(n);
  scanf("%d", &n);
  int A, B;
  for (int i = (0); i < (n); ++i) {
    int A, B;
    scanf("%d%d", &A, &B);
    x.push_back(make_pair(atan2l(B, A), i));
  }
  sort((x).begin(), (x).end());
  x.push_back(make_pair(PI * 2 + x[0].first, x[0].second));
  int ansxi;
  long double O = INFINITY;
  for (int i = (0); i < (n); ++i) {
    long double di = x[i + 1].first - x[i].first;
    if (di < 0) di = -di;
    if (di < O) {
      O = di;
      ansxi = i;
    }
  }
  cout << x[ansxi].second + 1 << ' ' << x[ansxi + 1].second + 1 << endl;
  return 0;
}
