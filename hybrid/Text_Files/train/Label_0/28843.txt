#include<bits/stdc++.h>
using namespace std;
int main(){
  int n,k,c,g;
  vector<int> book[11];
  cin >> n >> k;
  for(int i=0;i<n;i++){
    cin >> c >> g;
    book[g].push_back(c);
  }
  int dp[11][2001]={};
  for(int i=1;i<=10;i++){
    sort(book[i].begin(),book[i].end(),greater<int>());
    for(int j=1;j<book[i].size();j++) book[i][j] += book[i][j-1];
    
    for(int j=1;j<=k;j++){
      dp[i][j] = max(dp[i][j],dp[i-1][j]);
      for(int l=0;l<book[i].size();l++){
	int sum = l+1;
	if(j >= sum) dp[i][j] = max(dp[i][j],dp[i-1][j-sum]+book[i][l]+(sum)*l);
      }
    }    
  }
  cout << dp[10][k] << endl;
  return (0);
}