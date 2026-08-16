#include<bits/stdc++.h>
using namespace std;
using Int = long long;



struct RollingHash{
  typedef unsigned long long ull;
  string S;
  ull B;
  Int len;
  vector<ull> hash,p;
  RollingHash(){}
  RollingHash(string S_,ull B_ = 1e9+7):
    S(S_),B(B_),len(S.length()),hash(len+1),p(len+1){
    hash[0] = 0; p[0] = 1;
    for(Int i=0;i<len;i++){
      hash[i+1] = hash[i] * B + S[i];
      p[i+1] = p[i] * B;
    }
  }

  ull find(Int l,Int r){
    return hash[r] - hash[l] * p[r-l];
  }
};


signed main(){  
  cin.tie(0);
  ios::sync_with_stdio(0);
  Int n;
  cin>>n;
  vector<string> s(n);
  for(Int i=0;i<n;i++) cin>>s[i];
  
  string t;
  cin>>t;
  
  vector<RollingHash> rhs;
  for(Int i=0;i<n;i++) rhs.push_back(RollingHash(s[i]));
  using ull=RollingHash::ull;
  vector< vector<Int> > l(26);
  vector< vector<ull> > v(26);
  for(Int i=0;i<n;i++){
    l[s[i][0]-'a'].push_back(s[i].size());
    v[s[i][0]-'a'].push_back(rhs[i].find(0,s[i].size()));
  }
  
  RollingHash rht(t);
  vector<Int> dp(t.size()+1,0);
  dp[0]=1;
  const Int MOD=1e9+7;
  for(Int i=0;i<(Int)t.size();i++){
    if(!dp[i]) continue;
    for(Int j=0;j<(Int)l[t[i]-'a'].size();j++){
      if(i+l[t[i]-'a'][j]>(Int)t.size()) continue;
      if(rht.find(i,i+l[t[i]-'a'][j])==v[t[i]-'a'][j]){
	dp[i+l[t[i]-'a'][j]]+=dp[i];
	dp[i+l[t[i]-'a'][j]]%=MOD;
      }
    }
  }
  cout<<dp.back()<<endl;
  return 0;
}

