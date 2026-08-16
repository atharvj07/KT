#include<bits/stdc++.h>
using namespace std;
int dp[2][16][1<<16];
int c[16][1<<16][2];

int Max(int &a,int b){return a=max(a,b);}

int main(){

  int h,w;
  string s[128];

  cin>>h>>w;
  for(int i=0;i<h;i++)cin>>s[i];
  for(int i=0;i<w;i++)
    for(int j=0;j<1<<w;j++){
      int cnt=0;

      for(int k=0;k<i;k++)
	cnt+=bool(j&(1<<k));
      
      c[i][j][0]=cnt;
      c[i][j][1]=__builtin_popcount(j)-cnt;
    }


  for(int i=0;i<h;i++){
    
    for(int j=0;j<w;j++)
      for(int k=0;k<1<<w;k++){
	dp[(i+1)%2][j][k]=-1e9;
      }

    for(int j=0;j<w;j++)
      for(int k=0;k<(1<<w);k++){
	int cs=0;
	
	int idx = c[j][k][0],o=(int)s[i-1].size()-c[j][k][1];
	
	if(i && k&(1<<j) && idx <(int)s[i].size() && 0<=o && o < (int)s[i-1].size() && s[i][idx] == s[i-1][o]) cs+=2;


	if(j && idx && idx < (int)s[i].size() && (k & 1<<(j-1) ) && s[i][idx -1] == s[i][idx]) cs+=2;
	
	if( j!=w-1 || idx == (int)s[i].size() -1){
	  Max(dp[(i+(j==w-1))%2][(j+1)%w][k|(1<<j)],dp[i%2][j][k]+cs);

	}
	int nk=k;
	if(k&1<<j) nk^=1<<j;
	
	if( j!=w-1 || idx == (int)s[i].size() ) Max(dp[(i+(j==w-1))%2][(j+1)%w][nk],dp[i%2][j][k]);
	
      }
  }

  int ans=0;

  for(int i=0;i<1<<w;i++)
    if((int)s[h-1].size()==c[0][i][1]){
      ans=max(ans,dp[h%2][0][i]);
    }
  
  cout<<ans<<endl;
  return 0;
}