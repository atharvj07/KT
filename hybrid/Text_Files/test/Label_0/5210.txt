#include <bits/stdc++.h>
using namespace std;
using Int = long long;

template<typename T1,typename T2> void chmin(T1 &a,T2 b){if(a>b)a=b;};
template<typename T1,typename T2> void chmax(T1 &a,T2 b){if(a<b)a=b;};

const Int MAX = 1010;

double dp[2][MAX][MAX];
double dfs(Int k,Int i,Int j){
  double &res=dp[k][i][j];
  //cout<<k<<" "<<i<<" "<<j<<endl;
  assert(i>=0&&j>=0);
  if(res>=0) return res;  
  res=0;
  if(i==0||(k==0&&i<=j*2)) return res;
  if(!k){
    if(j) res+=dfs(0,i-2,j-1)*double(j)/double(i-j);
    res+=dfs(1,i,j+1)*double(i-2*j)/double(i-j);
  }else{
    assert(j>=1);
    res+=dfs(0,i-2,j-1)*double(1)/double(i-j);
    res+=(dfs(0,i-2,j-1)+1.0)*double(j-1)/double(i-j);
    res+=(dfs(0,i,j+1)+1.0)*double(i-j*2)/double(i-j);
  }
  return res;
}

signed main(){
  cin.tie(0);
  ios::sync_with_stdio(0);
  for(Int i=0;i<MAX;i++)
    for(Int j=0;j<MAX;j++)
      dp[0][i][j]=dp[1][i][j]=-1;
  Int n;
  while(cin>>n,n){
    cout<<fixed<<setprecision(12)<<dfs(0,n,0)<<endl;
  }
}


