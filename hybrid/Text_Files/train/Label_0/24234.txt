#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
#define rep(i, n) for(ll i = 0; i < (n); i++)

int main() {
  string s,t;
  cin>>s>>t;
  vector<ll> v1(30, 0);
  vector<ll> v2(30, 0);
  rep(i,s.size()) {
    ll si = s[i]-'a';
    ll ti = t[i]-'a';
    v1[si]++;
    v2[ti]++;
    if(v1[si] != v2[ti]) {
      cout << "No" << endl;
      return 0;
    }
  }
  cout << "Yes" << endl;
}