#include <bits/stdc++.h>
using namespace std;
bool check(long long n, long long pos) { return n & (1LL << pos); }
long long Set(long long n, long long pos) { return n = n | (1LL << pos); }
int main() {
  long long i, j, k, l, m, n, o, r, q;
  long long testcase;
  long long input, flag, tag, ans;
  scanf("%lld", &testcase);
  for (long long cs = 1; cs <= testcase; cs++) {
    scanf("%lld", &n);
    cout << n / 2 << '\n';
  }
}
