#include <bits/stdc++.h>
using namespace std;
double PI = 3.1415926536;
int dX[] = {1, -1, 0, 0};
int dY[] = {0, 0, 1, -1};
int s1Index = 0;
int s2Index = 0;
struct shit {
  shit(int x, int y) {
    this->x = x;
    this->y = y;
  }
  int x, y;
};
struct comparator {
  bool operator()(shit const &c, shit const &v) {
    return (c.x + c.y < v.x + v.y);
  }
};
bool sorted(vector<long long> v, int n) {
  for (int i = 0; i < n; i++)
    if (v[i] > v[i + 1]) return 0;
  return 1;
}
int main() {
  int a, b, c;
  cin >> a >> b >> c;
  if (b < a && c >= 0 || b > a && c <= 0) return puts("NO"), 0;
  if (b == a) return puts("YES"), 0;
  b = abs(a - b) % abs(c);
  cout << (b == 0 ? "YES" : "NO");
  return 0;
}
