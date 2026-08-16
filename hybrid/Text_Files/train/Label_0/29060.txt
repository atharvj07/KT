#include <bits/stdc++.h>
using namespace std;
int dp[201][201][2];
int main() {
  string s;
  cin >> s;
  int n=s.size();
  for(int i=0;i<n;i++){
    for(int j=0;j<n;j++)dp[i][j][0]=1<<29,dp[i][j][1]=-(1<<29);
    if(isdigit(s[i]))dp[i][i][0]=dp[i][i][1]=s[i]-'0';
  }
  for(int i=0; i<n; i++){
    for(int j=0;j<n-i;j++){
      if(s[j]=='(')dp[j][j+i][0]=min(dp[j][j+i][0],dp[j+1][j+i][0]),dp[j][j+i][1]=max(dp[j][j+i][1],dp[j+1][j+i][1]);
      if(s[j+i]==')')dp[j][j+i][0]=min(dp[j][j+i][0],dp[j][j+i-1][0]),dp[j][j+i][1]=max(dp[j][j+i][1],dp[j][j+i-1][1]);
    }
    for(int j=0;j<n-i;j++){
      if(s[j]=='+'||s[j]=='-'||s[j+i]=='+'||s[j+i]=='-')continue;
      for(int k=j+1;k<=j+i-1;k++){
        if((j+2<=k&&s[k-2]=='(')||(k<=j+i-2&&s[k+2]==')'))continue;
        if(s[k]=='+'||s[k]=='-'){
          for(int x=0;x<2;x++)for(int y=0;y<2;y++){
              if(abs(dp[j][k-1][x])>=(1<<29)||abs(dp[k+1][j+i][y])>=(1<<29))continue;
              dp[j][j+i][0]=min(dp[j][j+i][0],dp[j][k-1][x]+dp[k+1][j+i][y]*(s[k]=='+'?1:-1));
              dp[j][j+i][1]=max(dp[j][j+i][1],dp[j][k-1][x]+dp[k+1][j+i][y]*(s[k]=='+'?1:-1));
            }
        }
      }
    }
  }
  cout<<dp[0][n-1][1]<<endl;
  return 0;
}
