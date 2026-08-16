#include<bits/stdc++.h>
using namespace std;
using UL=unsigned int;
using LL=long long;
using ULL=unsigned long long;
#define rep(i,n) for(UL i=0; i<(n); i++)

deque<char> X,Y;
LL A,E,S,R;
LL dp[101][101];

bool loop(){
 X.clear(); Y.clear();

 string SX,SY;
 cin>>SX; if(SX=="#") return false;
 cin>>SY;
 for(char c:SX) X.push_back(c);
 for(char c:SY) Y.push_back(c);
 cin>>A>>E>>S>>R;

 LL offset=0;
 LL ans=1000000000000000;

 rep(i,Y.size()){
  rep(x,X.size()+1) rep(y,Y.size()+1) dp[x][y]=1000000000000000;
  dp[0][0]=offset;
  rep(x,X.size()+1) rep(y,Y.size()+1){
   if(x!=X.size()) dp[x+1][y]=min(dp[x+1][y],dp[x][y]+E);
   if(y!=Y.size()){
    if(y<i) dp[x][y+1]=min(dp[x][y+1],dp[x][y]+A-R);
    else dp[x][y+1]=min(dp[x][y+1],dp[x][y]+A);
   }
   if(x!=X.size() && y!=Y.size()){
    if(X[x]==Y[y]) dp[x+1][y+1]=dp[x][y];
    else dp[x+1][y+1]=min(dp[x+1][y+1],dp[x][y]+S);
   }
  }

  ans=min(ans,dp[X.size()][Y.size()]);

  Y.push_front(Y.back()); Y.pop_back(); offset+=R;
 }
 cout<<ans<<endl;
 return true;
}

int main(){
 while(loop());

 return 0;
}

