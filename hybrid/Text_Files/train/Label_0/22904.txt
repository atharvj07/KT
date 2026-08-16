#include <bits/stdc++.h>
using namespace std;
long long bigmod(long long n, long long p) {
  if (p == 0) return 1;
  if (p == 1) return (n + 1000000007) % 1000000007;
  if (p % 2)
    return (bigmod(n, p - 1) * n + 1000000007) % 1000000007;
  else {
    long long x = bigmod(n, p / 2);
    return (x * x + 1000000007) % 1000000007;
  }
}
long long modinverse(long long n) {
  return bigmod(n, 1000000007 - 2) % 1000000007;
}
long long arr[100005];
int main() {
  long long n;
  scanf("%lld", &n);
  while (n--) {
    queue<char> even, odd;
    string s;
    cin >> s;
    for (long long i = 0; i < s.size(); i++) {
      long long fo = s[i] - '0';
      if (fo % 2)
        odd.push(s[i]);
      else
        even.push(s[i]);
    }
    while (!odd.empty() && !even.empty()) {
      long long a = even.front() - '0';
      long long b = odd.front() - '0';
      if (a < b) {
        cout << a;
        even.pop();
      } else {
        cout << b;
        odd.pop();
      }
    }
    while (!odd.empty()) {
      cout << odd.front();
      odd.pop();
    }
    while (!even.empty()) {
      cout << even.front();
      even.pop();
    }
    cout << endl;
  }
}
