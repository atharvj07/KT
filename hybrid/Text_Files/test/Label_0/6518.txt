#include <bits/stdc++.h>
using namespace std;
double intersect(pair<double, double> a, pair<double, double> b, double pv) {
  if (a.first == b.first) {
    if (a.second < b.second)
      return -1;
    else
      return pv;
  }
  return (b.second - a.second) / (a.first - b.first);
}
int main() {
  int n;
  scanf("%d", &n);
  vector<pair<pair<double, double>, int> > points(n);
  for (int i = 0; i < n; i++) {
    int x, y;
    scanf("%d %d", &x, &y);
    points[i].first.first = 1.0 / x - 1.0 / y;
    points[i].first.second = 1.0 / y;
    points[i].second = i + 1;
  }
  sort(points.begin(), points.end());
  stack<pair<double, int> > st;
  for (int i = n - 1; i >= 0; i--) {
    double inter = 0.0;
    while (!st.empty()) {
      pair<double, int> P = st.top();
      inter = intersect(points[i].first, points[P.second].first, P.first);
      if (inter < P.first ||
          (inter <= 0 && points[i].first != points[P.second].first)) {
        st.pop();
      } else {
        break;
      }
    }
    if (st.empty()) {
      st.push(make_pair(0, i));
    } else if (1 - inter >= 0.0000000000001) {
      st.push(make_pair(inter, i));
    }
  }
  vector<int> r;
  while (!st.empty()) {
    if (st.top().first >= 1) {
      continue;
    } else {
      r.push_back(points[st.top().second].second);
    }
    st.pop();
  }
  sort(r.begin(), r.end());
  for (int i = 0; i < r.size(); i++) {
    printf("%d ", r[i]);
  }
  printf("\n");
}
