#include<bits/stdc++.h>
using namespace std;
using Int = long long;
template<typename T1,typename T2> void chmin(T1 &a,T2 b){if(a>b) a=b;};
template<typename T1,typename T2> void chmax(T1 &a,T2 b){if(a<b) a=b;};

signed main(){
  cin.tie(0);
  ios::sync_with_stdio(false);
  
  Int n;
  cin>>n;
  vector<string> vs(n+1);
  for(Int i=0;i<=n;i++) cin>>vs[i];

  const Int INF = 1e15;
  auto calc=[&](string s){
    vector<Int> res;
    Int n=s.size();
    for(Int i=0;i<n;i++){
      if(isalpha(s[i])){
	res.emplace_back(INF + Int(s[i]));
	continue;
      }
      Int tmp=0;
      while(isdigit(s[i])){
	tmp=tmp*10+s[i]-'0';
	i++;
      }
      i--;
      res.emplace_back(tmp);
    }
    return res;
  };
  
  string s=vs[0];
  auto check=[&](string t)->Int{
    if(s==t) return 1;
    if(s.size()<t.size())
      if(t.substr(0,s.size())==s) return 1;
    if(s.size()>t.size())
      if(s.substr(0,t.size())==t) return 0;
    
    auto x=calc(s);
    auto y=calc(t);
    for(Int i=0;i<(Int)min(x.size(),y.size());i++){
      if(x[i]<y[i]) return 1;
      if(x[i]>y[i]) return 0;
    }

    assert(0);
    return 0;
  };
  
  for(Int i=1;i<=n;i++){
    if(check(vs[i])) cout<<"+"<<endl;
    else cout<<"-"<<endl;    
  } 
  
  return 0;
}

