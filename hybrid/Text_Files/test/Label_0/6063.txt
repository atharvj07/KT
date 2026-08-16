#include<bits/stdc++.h>
using namespace std;

int main() {
  long n, x;
  cin >> n >> x;

  vector<long long> a(n+1);
  a.at(0) = 0ll;
  long long t;
  for(int i = 0; i < n; ++i){cin >> t; a.at(i+1) = a.at(i) + t;}

  long long ans = 1ll << 62;
  long long tans = 0ll;
  long long b;
  long long coef;
  for(long k = 1; k <= n; ++k) {
    tans = 0ll;
    b = 1ll*(n+k)*x;
    for(long i = 0; i < (n+(k-1))/k; ++i){
      coef = i?2ll*i+3ll:5ll;
      tans += coef * (a.at(n - i * k) - a.at(max(n - (i + 1) * k, 0l)));
      if (tans<0) tans = 1ll << 62;
    }
    ans = min(ans, tans+b);
  }
  cout << ans << endl;
}