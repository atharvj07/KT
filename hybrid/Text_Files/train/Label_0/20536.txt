#include<bits/stdc++.h>
using namespace std;
#define lp(i,n) for(int i=0;i<(int)n;i++)

template<unsigned mod>
struct RollingHash{
  vector<unsigned> hashed,power;

  inline unsigned mul(unsigned a,unsigned b) const{
    unsigned long long x = (unsigned long long)a*b;
    unsigned xh=unsigned(x>>32),xl=(unsigned)x,d,m;
    asm("divl %4; \n\t" : "=a"(d),"=d"(m):"d"(xh),"a"(xl),"r"(mod));
    return m;
  }

  RollingHash(const string &s, unsigned base=10007){
    int sz=(int)s.size();
    hashed.assign(sz+1,0);
    power.assign(sz+1,0);
    power[0]=1;
    for(int i=0;i<sz;i++){
      power[i+1]=mul(power[i],base);
      hashed[i+1]=mul(hashed[i],base)+s[i];
      if(hashed[i+1]>=mod)hashed[i+1] -=mod;
    }
  }
  unsigned get(int l,int r) const{
    unsigned ret=hashed[r]+mod-mul(hashed[l],power[r-l]);
    if(ret>=mod)ret-=mod;
    return ret;
  }
};

using RH = RollingHash<1000000181>;
using SH = RollingHash<1000000007>;

#define int long long

int calc(vector<string> &v,string s){
  int l=lower_bound(v.begin(),v.end(),s)-v.begin();
  s[s.size()-1]++;
  int r=lower_bound(v.begin(),v.end(),s)-v.begin();
  return abs(l-r);
}


signed main(){
  int n,q;
  cin>>n>>q;
  map<pair<int,int>,vector<string>> m;
  lp(i,n){
    string s;
    cin>>s;
    RH rh(s);
    SH sh(s);
    lp(i,s.size()){
      m[{(int)rh.get(i,s.size()),(int)sh.get(i,s.size())}].push_back(s);
    }
  }
  set<int> ch;
  lp(i,q){
    string a,b;
    cin>>a>>b;
    RH rh(b);
    SH sh(b);
    int hs=rh.get(0,b.size());
    int ss=sh.get(0,b.size());
    vector<string> &v=m[{hs,ss}];
    if(v.empty()){
      cout<<0<<endl;
      continue;
    }
    if(ch.find(hs)==ch.end()){
      sort(v.begin(),v.end());
      ch.insert(hs);
    }
    cout<<calc(v,a)<<endl;
  }
}

