#include<stdio.h>
#include<algorithm>
#include<vector>
#include<queue>
using namespace std;
int p[110];
int q[110];
int r[110];
vector<int>g[110];
int g2[110][110];
int UF[110];
int FIND(int a){
	if(UF[a]<0)return a;
	return UF[a]=FIND(UF[a]);
}
void UNION(int a,int b){
	a=FIND(a);b=FIND(b);if(a==b)return;UF[a]+=UF[b];UF[b]=a;
}
int dp[110][11000];
int jk[110];
int sz;
int top[110];
int rep[110];
int v[110];
int cnt;
void dfs(int a){
	v[a]=1;
	for(int i=0;i<sz;i++){
		if(i!=a&&g2[rep[a]][rep[i]]&&!v[i]){
			dfs(i);
		}
	}
	top[cnt--]=a;
}
int main(){
	int a,b,c;
	while(scanf("%d%d%d",&a,&b,&c),a){
		for(int i=0;i<a;i++)jk[i]=0;
		for(int i=0;i<a;i++){
			scanf("%d%d%d",p+i,q+i,r+i);
		}
		for(int i=0;i<a;i++)for(int j=0;j<a;j++)g2[i][j]=0;
		for(int i=0;i<a;i++)g2[i][i]=1;
		for(int i=0;i<a;i++)g[i].clear();
		for(int i=0;i<b;i++){
			int s,t;scanf("%d%d",&s,&t);s--;t--;
			if(s==t)jk[s]=1;
			g[s].push_back(t);
			g2[s][t]=1;
		}
		for(int k=0;k<a;k++)for(int i=0;i<a;i++)for(int j=0;j<a;j++){
			g2[i][j]|=(g2[i][k]&g2[k][j]);
		}
		for(int i=0;i<a;i++)UF[i]=-1;
		for(int i=0;i<a;i++)for(int j=i+1;j<a;j++){
			if(g2[i][j]&&g2[j][i])UNION(i,j);
		}
		sz=0;
		for(int i=0;i<a;i++){
			if(UF[i]<0){
				rep[sz++]=i;
			}
		}
		cnt=sz-1;
		for(int i=0;i<sz;i++){
			v[i]=0;
		}
		for(int i=0;i<sz;i++){
			if(v[i]==0){
				dfs(i);
			}
		}
		for(int i=0;i<sz;i++)for(int j=0;j<=c;j++)dp[i][j]=-999999999;
		for(int i=0;i<sz;i++)dp[i][0]=0;
		for(int i=0;i<sz;i++){
			for(int j=0;j<i;j++){
				if(g2[rep[top[j]]][rep[top[i]]]){
					for(int k=0;k<=c;k++)dp[i][k]=max(dp[i][k],dp[j][k]);
				}
			}
			if(UF[rep[top[i]]]==-1&&jk[rep[top[i]]]==0){
				for(int j=c;j>=q[rep[top[i]]];j--){
					dp[i][j]=max(dp[i][j],dp[i][j-q[rep[top[i]]]]+p[rep[top[i]]]);
				}
			}else{
				for(int j=0;j<a;j++){
					if(FIND(j)==rep[top[i]]){
						for(int k=0;k<q[j];k++){
							deque<pair<int,int> >Q;
							for(int l=k;l<=c;l+=q[j]){
								while(Q.size()&&dp[i][l]-p[j]*(l/q[j])>=Q.back().second){
									Q.pop_back();
								}
								Q.push_back(make_pair(l,dp[i][l]-p[j]*(l/q[j])));
								dp[i][l]=max(dp[i][l],Q.front().second+p[j]*(l/q[j]));
								if(Q.front().first<=l-r[j]*q[j])Q.pop_front();
							}
						}
					}
				}
			}
		//	printf("%d %d %d\n",rep[top[i]],UF[rep[top[i]]],jk[rep[top[i]]]);
	//		for(int j=0;j<=c;j++)printf("%d ",dp[i][j]);
//			printf("\n");
		}
		int ret=0;
		for(int i=0;i<sz;i++)for(int j=0;j<=c;j++)ret=max(ret,dp[i][j]);
		printf("%d\n",ret);
	}
}