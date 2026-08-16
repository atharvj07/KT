#include<bits/stdc++.h>
using namespace std;

int N,M;
int X[101];
int A[101],B[101],C[101];
int dp[111][111][11];
int solve(int l,int r,int x){
  if( dp[l][r][x] != -1 ) return dp[l][r][x];
  if( l == r && A[x] == X[l] ) return dp[l][r][x] = 1;
  for(int i=l;i<=r-1;i++){
    if( solve(l,i,B[x]) == 1 &&
	solve(i+1,r,C[x]) == 1 ) return dp[l][r][x] = 1;
  }
  return dp[l][r][x] = 0;
}

int main(){
  memset(dp,-1,sizeof(dp));
  cin >> N;
  for(int i=0;i<N;i++) cin >> X[i];
  cin >> M;
  for(int i=0;i<M;i++){
    cin >> A[i] >> B[i] >> C[i];
    --B[i]; --C[i];
  }
  if( solve(0,N-1,0) ) cout << "Yes" << endl;
  else cout << "No" << endl;
}