#include <bits/stdc++.h>
using namespace std;
const long long N = 100100;
const long long Inf = 1e18;
long long a[N];
long long Dp[N];
deque<long long> Min;
deque<long long> Max;
deque<long long> DpMin;
int main() {
  long long n, s, l;
  cin >> n >> s >> l;
  for (long long i = 0; i < n; ++i) scanf("%I64d", a + i);
  Dp[n] = 0;
  for (long long i = n - 1, p1 = i + l, p2 = n; ~i; --i, --p1) {
    Dp[i] = Inf;
    while (!Min.empty() && a[i] <= a[Min.front()]) Min.pop_front();
    Min.push_front(i);
    while (!Max.empty() && a[i] >= a[Max.front()]) Max.pop_front();
    Max.push_front(i);
    while (!DpMin.empty() && Dp[p1] <= Dp[DpMin.front()]) DpMin.pop_front();
    if (p1 <= p2) DpMin.push_front(p1);
    while (a[Max.back()] - a[Min.back()] > s) {
      if (Min.back() == p2 - 1) Min.pop_back();
      if (Max.back() == p2 - 1) Max.pop_back();
      if (!DpMin.empty() && DpMin.back() == p2) DpMin.pop_back();
      p2--;
    }
    if (p1 <= p2 && !DpMin.empty()) Dp[i] = 1 + Dp[DpMin.back()];
  }
  long long Ans = Dp[0];
  if (Ans > n) Ans = -1;
  cout << Ans;
}
