/**
 *    author:  Naina Nair
**/
#include <cstdio>
#include <cstring>
#include <iostream>
#include <vector>
#include <algorithm>
 
using namespace std;
 
const int MaxN = 200002;
 
void Run_Case(void);
 
int main (void)
{
  int test, tests=1;
  scanf ("%d", &tests);
 
  for (test = 0; test < tests; test++)
  {
    Run_Case();
        
  }
}
long long dp[MaxN][2];
int b[MaxN];
void Run_Case(void){
	string s;
	cin>>s;
	int n=s.size();
	for(int i=0;i<n;i++){
		b[i]=0;
		dp[i][0]=0;
		dp[i][1]=0;
	}
	if(s[0]=='0'){
		dp[0][0]=1;
		dp[0][1]=0;
	}
	else if(s[0]=='1'){
		dp[0][0]=0;
		dp[0][1]=1;
	}
	else{
		dp[0][0]=1;
		dp[0][1]=1;
	}
	long long answer=max(dp[0][0],dp[0][1]);
	b[0]=answer;
	for(int i=1;i<n;i++){
		if(s[i]=='0'){
			dp[i][1]=0;
			dp[i][0]=1+dp[i-1][1];
			b[i]=max(dp[i][0],dp[i][1]);
		}
		else if(s[i]=='1'){
			dp[i][0]=0;
			dp[i][1]=1+dp[i-1][0];
			b[i]=max(dp[i][0],dp[i][1]);
		}
		else{
			dp[i][0]=1+dp[i-1][1];
			dp[i][1]=1+dp[i-1][0];
			b[i]=b[i-1]+1;
		}
		answer+=b[i];
	}
	printf("%lld\n",answer);
	
	
	
	
		
}
