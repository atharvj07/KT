#include <bits/stdc++.h>
using namespace std;
double PI = 4.00 * (atan(1));
long long int gcd(long long int a, long long int b) {
  if (b == 0) {
    return a;
  }
  return gcd(b, a % b);
}
pair<long long int, long long int> makeline(long long int xdiff,
                                            long long int ydiff) {
  if ((xdiff * ydiff) >= 0) {
    xdiff = fabs(xdiff);
    ydiff = fabs(ydiff);
  } else {
    long long int temp = xdiff * ydiff;
    ydiff = fabs(ydiff);
    xdiff = temp / ydiff;
  }
  long long int val1 = gcd(fabs(xdiff), fabs(ydiff));
  xdiff = xdiff / val1;
  ydiff = ydiff / val1;
  return make_pair(xdiff, ydiff);
}
long long int sumsquare(vector<long long int> v1) {
  long long int size = v1.size();
  long long int sum = 0;
  for (long long int i = 0; i < size; i++) {
    sum += v1[i];
  }
  sum = sum * sum;
  for (long long int i = 0; i < size; i++) {
    sum -= (v1[i] * v1[i]);
  }
  sum = sum / 2;
  return sum;
}
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  long long int n;
  cin >> n;
  pair<long long int, long long int> points[n];
  for (long long int i = 0; i < n; i++) {
    cin >> points[i].first >> points[i].second;
  }
  map<pair<long long int, long long int>, set<long long int>> values;
  pair<long long int, long long int> temp;
  long long int diff = 0;
  long long int val;
  for (long long int i = 0; i < n; i++) {
    for (long long int j = 0; j < n; j++) {
      if (i == j) {
        continue;
      }
      temp = makeline(points[j].first - points[i].first,
                      points[j].second - points[i].second);
      val = temp.first * points[i].second;
      val -= (temp.second * points[i].first);
      values[temp].insert(val);
    }
  }
  vector<long long int> final;
  for (auto it : values) {
    val = it.second.size();
    final.push_back(val);
  }
  long long int result = sumsquare(final);
  cout << result;
  return 0;
}
