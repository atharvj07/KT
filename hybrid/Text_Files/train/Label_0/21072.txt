#include <bits/stdc++.h>
using namespace std;
int INF = std::numeric_limits<int>::max();
long long LLINF = std::numeric_limits<long long>::max();
int NINF = std::numeric_limits<int>::min();
int MOD = 1000000007;
int col[] = {1, 0, -1, 0, 1, 1, -1, -1};
int row[] = {0, 1, 0, -1, 1, -1, 1, -1};
int cc[] = {1, 2, 2, 1, -1, -1, -2, -2};
int rr[] = {-2, -1, 1, 2, -2, 2, 1, -1};
long long gcd(long long a, long long b) {
  if (b == 0) return a;
  return gcd(b, a % b);
}
int main() {
  long long x, y, dasha, masha;
  cin >> x >> y;
  long long z = (x * y) / gcd(x, y);
  dasha = z / x, masha = z / y;
  dasha--;
  masha--;
  if (masha < dasha)
    masha++;
  else
    dasha++;
  if (masha > dasha)
    cout << "Masha";
  else if (dasha > masha)
    cout << "Dasha";
  else
    cout << "Equal";
  return 0;
}
