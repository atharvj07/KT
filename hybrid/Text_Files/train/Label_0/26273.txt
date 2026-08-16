#include <bits/stdc++.h>
using namespace std;
#define sz(x) ((int) (x).size())
typedef long long ll;
typedef pair<int,int> pii;
template<class T> void print(T & x){ cout << x; }
template<class T,class U> void print(pair<T,U> & p){cout << "("; print(p.first); cout << ", "; print(p.second); cout << ")"; }
template<class T> void print(vector<T> & v) {
  cout << "{";
  if (sz(v)) print(v[0]);
  for (int i = 1; i < sz(v); i++) cout << ", ", print(v[i]);
  cout << "}\n";
}

string S;

int solve(int m){
  vector<int> sm(sz(S));
  int cnt = 0;
  for(int i=0; i<sz(S); i++){
    if(S[i] == '1') cnt++;
    else cnt--;
    sm[i] = cnt;
  }
  for(int i=sz(S)-2; i>=0; i--)
    sm[i] = max(sm[i], sm[i+1]);
  int add = 0;
  int minim = 0;
  cnt = 0;
  for(int i=0; i<sz(S); i++){
    if(S[i] != '?')
      cnt += (S[i]-'0')*2-1;
    else{
      if(sm[i]+add+2 <= m)
        cnt++, add += 2;
      else
        cnt--;
    }
    minim = min(minim, cnt);
  }
  return m-minim;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cin >> S;
  int z = 0;
  int cnt = 0;
  for(int i=0; i<sz(S); i++){
    if(S[i] == '1') cnt++;
    else cnt--;
    z = max(z, cnt);
  }
  cout << min(solve(z), solve(z+1)) << endl;
}
