#include<bits/stdc++.h>
using namespace std;
using Int = long long;
template<typename T1,typename T2> inline void chmin(T1 &a,T2 b){if(a>b) a=b;}
template<typename T1,typename T2> inline void chmax(T1 &a,T2 b){if(a<b) a=b;}


template<typename T,T MOD = 1000000007>
struct Mint{
  static constexpr T mod = MOD;
  T v;
  Mint():v(0){}
  Mint(signed v):v(v){}
  Mint(long long t){v=t%MOD;if(v<0) v+=MOD;}

  Mint pow(long long k){
    Mint res(1),tmp(v);
    while(k){
      if(k&1) res*=tmp;
      tmp*=tmp;
      k>>=1;
    }
    return res;
  }

  static Mint add_identity(){return Mint(0);}
  static Mint mul_identity(){return Mint(1);}

  Mint inv(){return pow(MOD-2);}

  Mint& operator+=(Mint a){v+=a.v;if(v>=MOD)v-=MOD;return *this;}
  Mint& operator-=(Mint a){v+=MOD-a.v;if(v>=MOD)v-=MOD;return *this;}
  Mint& operator*=(Mint a){v=1LL*v*a.v%MOD;return *this;}
  Mint& operator/=(Mint a){return (*this)*=a.inv();}

  Mint operator+(Mint a) const{return Mint(v)+=a;}
  Mint operator-(Mint a) const{return Mint(v)-=a;}
  Mint operator*(Mint a) const{return Mint(v)*=a;}
  Mint operator/(Mint a) const{return Mint(v)/=a;}

  Mint operator-() const{return v?Mint(MOD-v):Mint(v);}

  bool operator==(const Mint a)const{return v==a.v;}
  bool operator!=(const Mint a)const{return v!=a.v;}
  bool operator <(const Mint a)const{return v <a.v;}

  static Mint comb(long long n,int k){
    Mint num(1),dom(1);
    for(int i=0;i<k;i++){
      num*=Mint(n-i);
      dom*=Mint(i+1);
    }
    return num/dom;
  }
};
template<typename T,T MOD> constexpr T Mint<T, MOD>::mod;
template<typename T,T MOD>
ostream& operator<<(ostream &os,Mint<T, MOD> m){os<<m.v;return os;}


template<typename M>
M lagrange_interpolation(vector<M> &ys,M t){
  int n=ys.size()-1;
  if(t.v<=n) return ys[t.v];

  vector<M> dp(n+1,1),pd(n+1,1);
  for(int i=0;i<n;i++) dp[i+1]=dp[i]*(t-M(i));
  for(int i=n;i>0;i--) pd[i-1]=pd[i]*(t-M(i));

  vector<M> fact(n+1,1),finv(n+1,1);
  for(int i=1;i<=n;i++) fact[i]=fact[i-1]*M(i);
  finv[n]=M(1)/fact[n];
  for(int i=n;i>=1;i--) finv[i-1]=finv[i]*M(i);

  M res(0);
  for(int i=0;i<=n;i++){
    M tmp=ys[i]*dp[i]*pd[i]*finv[i]*finv[n-i];
    if((n-i)&1) res-=tmp;
    else res+=tmp;
  }
  return res;
}

//INSERT ABOVE HERE
using M = Mint<int>;
const int MAX = 6060;
M dp[2020][MAX]={};
M ad[2020][MAX]={};
signed main(){
  int n,m;
  while(cin>>n>>m,n||m){
    vector<int> as(m),bs(m),cs(m);
    vector< vector<int> > G(n+1);
    for(int i=0;i<m;i++){
      cin>>as[i]>>bs[i]>>cs[i];
      G[as[i]].emplace_back(i);
    }
    as.emplace_back(0);
    bs.emplace_back(1);
    cs.emplace_back(0);
    G[0].emplace_back(m);

    dp[0][0]=M(1);
    for(int v=0;v<=n;v++){
      for(int j=0;j<MAX;j++){
        if(j) ad[v][j]+=ad[v][j-1];
        dp[v][j]+=ad[v][j];
      }

      for(int i:G[v])
        for(int j=0;j+cs[i]<MAX;j++)
          ad[bs[i]][j+cs[i]]+=dp[as[i]][j];
    }

    int q;
    cin>>q;
    for(int i=0;i<q;i++){
      int d,e;
      cin>>d>>e;
      vector<M> ys(dp[d]+n+n,dp[d]+n+n+n+1);
      if(e<n+n+n) cout<<dp[d][e]<<"\n";
      else cout<<lagrange_interpolation(ys,M(e-n-n))<<"\n";
    }

    for(int v=0;v<=n;v++)
      for(int j=0;j<MAX;j++)
        dp[v][j]=ad[v][j]=M(0);
  }
  cout<<flush;
  return 0;
}

