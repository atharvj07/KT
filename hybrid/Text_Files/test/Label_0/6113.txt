#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>

#define rep(i,n) for(int i=0;i<n;i++)
#define rp(i,c) rep(i,(c).size())
#define fr(i,c) for(__typeof((c).begin()) i=(c).begin();i!=(c).end();i++)
#define mp make_pair
#define pb push_back
#define all(c) (c).begin(),(c).end()
#define dbg(x) cerr<<#x<<" = "<<(x)<<endl

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;
const int inf=1<<28;
const double INF=1e10,EPS=1e-9;

int n;
double dp[100001][30],ans[100001];

int main()
{
	double pw[30];
	pw[0]=1; rep(i,29)pw[i+1]=pw[i]*0.5;
	
	fill_n(ans,100001,0);
	rep(i,100001)rep(j,30)dp[i][j]=0;
	dp[0][0]=1;
	
	for(int i=1;i<100001;i++)
	{
		rep(j,30)
		{
			dp[i][0]+=dp[i-1][j]*(1-pw[j]);
			if(j<29)dp[i][j+1]+=dp[i-1][j]*pw[j];
		}
		ans[i]=ans[i-1];
		rep(j,29)ans[i]+=dp[i][j+1];
	}
	
	while(cin>>n,n)printf("%.3f\n",ans[n]);
	
	return 0;
}