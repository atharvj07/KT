#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
#include <string>
#include <algorithm>
#include <iostream>
#include <string>
#include <map>
#include <set>
#include <functional>
#include <iostream>
#define INF 10000007
using namespace std;
typedef long long ll;
typedef pair<int,int> P;

int n,m,W,t;
string str[101];
int v[8],p[8];

int l[8],x[8],y[8];
int r[8][8],w[8][8];
int dp[1<<8][10001];
int dp2[1<<8][8];
ll dp3[10001];

int main(void){
	scanf("%d%d%d%d",&n,&m,&W,&t);
	for(int i=0;i<m;i++){
		cin >> str[i] >> v[i] >> p[i];
	}
	for(int i=0;i<n;i++){
		scanf("%d%d%d",&l[i],&x[i],&y[i]);
		for(int j=0;j<l[i];j++){
			string s;
			cin >> s >> r[i][j];
			int id;
			for(id=0;id<m;id++){
				if(str[id]==s){
					break;
				}
			}
			r[i][j]=p[id]-r[i][j];
			w[i][j]=v[id];
		}
	}
	for(int bit=1;bit<(1<<n);bit++){
		for(int j=0;j<W;j++){
			dp[bit][j+1]=max(dp[bit][j+1],dp[bit][j]);
			for(int i=0;i<n;i++){
				if(!(bit>>i & 1))continue;
				for(int k=0;k<l[i];k++){
					if(j+w[i][k]<=W){
						dp[bit][j+w[i][k]]=max(dp[bit][j+w[i][k]],dp[bit][j]+r[i][k]);
					}
				}
			}
		}
	}
	for(int i=0;i<(1<<n);i++){
		for(int j=0;j<=n;j++){
			dp2[i][j]=INF;
		}
	}
	dp2[0][n]=0;
	for(int i=0;i<(1<<n);i++){
		for(int j=0;j<=n;j++){
			if(dp2[i][j]==INF)continue;
			for(int k=0;k<n;k++){
				int dist=abs(x[k]-x[j])+abs(y[k]-y[j]);
				dp2[i|(1<<k)][k]=min(dp2[i|(1<<k)][k],dp2[i][j]+dist);
			}
		}
	}
	for(int i=0;i<(1<<n);i++){
		for(int j=0;j<n;j++){
			dp2[i][n]=min(dp2[i][n],dp2[i][j]+abs(x[j])+abs(y[j]));
		}
	}
	for(int i=0;i<t;i++){
		dp3[i+1]=max(dp3[i+1],dp3[i]);
		for(int j=0;j<(1<<n);j++){
			if(dp2[j][n]+i<=t){
				dp3[i+dp2[j][n]]=max(dp3[i+dp2[j][n]],(ll)dp3[i]+dp[j][W]);
			}
		}
	}
	printf("%lld\n",dp3[t]);
	return 0;
}