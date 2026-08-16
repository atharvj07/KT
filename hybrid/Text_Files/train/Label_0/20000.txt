#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<ll,ll> pll;

int main() {
  ll h,w;
  cin >> h >> w;
  map<char,ll> count;
  for(ll i=0;i<h;i++) {
    string temp;
    cin >> temp;
    for(ll j=0;j<w;j++) {
      count[temp[j]]++;
    }
  }
  ll g1=h%2*w%2;
  ll g2=w%2*h/2+h%2*w/2;
  ll g4=h/2*(w/2);
  while(g1--) {
    for(auto p:count) {
      if(p.second%2) {
        count[p.first]--;
        break;
      }
    }
  }
  while(g2--) {
    for(auto p:count) {
      if(p.second%4==2) {
        count[p.first]-=2;
        break;
      }
    }
  }
  for(auto p:count) {
    if(p.second%4) {
      cout << "No" << endl;
      return 0;
    }
  }
  cout << "Yes" << endl;
}