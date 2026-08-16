#include<cstdio>
#include<algorithm>
#include<queue>

#define INF 1<<29

using namespace std;

int main(){
	while(1){
		int n,m;
		scanf("%d%d",&m,&n);
		if(m==0 && n==0){
			break;
		}
		int cost[101][101];
		int time[101][101];
		
		for(int i=0;i<101;i++)
		for(int j=0;j<101;j++)
		cost[i][j]=time[i][j]=INF;
		
		for(int i=0;i<m;i++){
			int a,b,c,d;
			scanf("%d%d%d%d",&a,&b,&c,&d);
			cost[a][b]=cost[b][a]=c;
			time[a][b]=time[b][a]=d;
		}
		
		for(int k=1;k<=n;k++){
			for(int i=1;i<=n;i++){
				for(int j=1;j<=n;j++){
					cost[i][j]=min(cost[i][j],cost[i][k]+cost[k][j]);
					time[i][j]=min(time[i][j],time[i][k]+time[k][j]);
				}
			}
		}
		
		scanf("%d",&m);
		for(int i=0;i<m;i++){
			int a,b,c;
			scanf("%d%d%d",&a,&b,&c);
			if(c==0){
				printf("%d\n",cost[a][b]);
			}else{
				printf("%d\n",time[a][b]);
			}
		}
	}
}