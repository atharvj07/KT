#include <cstdio>
#include <cstring>
#include <cctype>
#include <cmath>
#include <utility>
#include <vector>
#include <algorithm>
using namespace std;
typedef pair<int,int> P;
#define DIST(X,Y)(abs((X).first-(Y).first)+abs((X).second-(Y).second))
int dp[6][1000];
vector<P> location[7];
char M[1000][1001];
int main() {
	int x,y;
	while(scanf("%d %d",&x,&y),x) {
		for(int i=0;i<y;i++) {
			scanf("%s",M[i]);
		}
		for(int i=0;i<=6;i++) location[i].clear();
		for(int i=0;i<y;i++) {
			for(int j=0;j<x;j++) {
				if(M[i][j]=='S') location[0].push_back(P(j,i));
				else if(M[i][j]=='G') location[6].push_back(P(j,i));
				else if(isdigit(M[i][j])) location[M[i][j]-'0'].push_back(P(j,i));
			}
		}
		int A,B=1<<30;
		for(int i=1;i<=5;i++) {
			vector<int> V;
			V.push_back(0);
			for(int j=1;j<=4;j++) {
				if((i+j)<=5) V.push_back(i+j);
				else V.push_back((i+j)-5);
			}
			V.push_back(6);
			fill((int*)dp,(int*)(dp+6),1<<30);
			dp[0][0]=0;
			for(int j=1;j<=5;j++) {
				for(int k=0;k<location[V[j]].size();k++) {
					for(int l=0;l<location[V[j-1]].size();l++) {
						dp[j][k]=min(dp[j][k],dp[j-1][l]+DIST(location[V[j]][k],location[V[j-1]][l]));
					}
				}
			}
			if(B>dp[5][0]) A=i,B=dp[5][0];
		}
		if(B==(1<<30))printf("NA\n");
		else printf("%d %d\n",A,B);
	}
}