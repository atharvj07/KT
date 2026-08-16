#include <cmath>
#include <cstdio>
#include <vector>
#include <algorithm>

#define rep(i,n) for(int i=0;i<(n);i++)

using namespace std;

const double EPS=1e-8;

const int N_MAX=252;

bool Gauss_Jordan(int n,const double A[N_MAX][N_MAX],const double *b,double *x){
	static double B[N_MAX][N_MAX+1];
	rep(i,n){
		rep(j,n) B[i][j]=A[i][j];
		B[i][n]=b[i];
	}

	rep(i,n){
		int piv=i;
		for(int j=i;j<n;j++) if(abs(B[j][i])>abs(B[piv][i])) piv=j;
		rep(j,n+1) swap(B[i][j],B[piv][j]);

		if(abs(B[i][i])<EPS) return false;

		for(int j=i+1;j<=n;j++) B[i][j]/=B[i][i];
		rep(j,n) if(i!=j) for(int k=i+1;k<=n;k++) B[j][k]-=B[j][i]*B[i][k];
	}

	rep(i,n) x[i]=B[i][n];
	return true;
}

int H,W;
char B0[5][6],B1[5][6];

struct state{
	char B[5][5];
	bool operator==(const state &s)const{
		rep(i,H) rep(j,W) if(B[i][j]!=s.B[i][j]) return false;
		return true;
	}
};

void dfs(int y,int x,state &s,vector<state> &S){
	if(x==-1){
		S.push_back(s);
		return;
	}

	for(int i=y;i<=H;i++){
		for(int k=0;k<i;k++) s.B[k][x]='?';
		if(i>y) s.B[i-1][x]='x';
		for(int k=i;k<H;k++) s.B[k][x]='o';
		dfs(i,x-1,s,S);
	}
}

state board_to_state(const char B[5][6]){
	state s;
	rep(i,H) rep(j,W) {
		if(B[i][j]==B1[i][j]) s.B[i][j]='o';
		else                  s.B[i][j]='x';
	}
	int len=7777777;
	for(int i=H-1;i>=0;i--){
		int j;
		for(j=W-1;j>=0;j--) if(s.B[i][j]=='x' || W-j>len) break;
		if(W-j<=len){
			len=W-j-1;
			j--;
		}
		for(;j>=0;j--) s.B[i][j]='?';
	}
	return s;
}

int main(){
	for(;scanf("%d%d",&H,&W),H;){
		rep(i,H) scanf("%s",B0[i]);
		rep(i,H) scanf("%s",B1[i]);

		vector<state> S; // set of possible states
		state s;
		dfs(0,W-1,s,S);

		int m=S.size();
		static double P[252][252]; // transition matrix, P[i][j] := (probability to transit from state i to j)
		static double C[252][252]; // coefficient for b
		rep(i,m) rep(j,m) P[i][j]=C[i][j]=0;
		rep(k,m){
			rep(i,H) rep(j,W) rep(c,2) { // operate (i, j) with color c
				char B[5][6];
				rep(y,H) rep(x,W) {
					if     (S[k].B[y][x]=='o') B[y][x]=B1[y][x];
					else if(S[k].B[y][x]=='x') B[y][x]=(B1[y][x]=='W'?'B':'W');
					else                       B[y][x]='?';
				}
				rep(y,i+1) rep(x,j+1) B[y][x]=(c==0?'W':'B');

				state s=board_to_state(B);
				int to=find(S.begin(),S.end(),s)-S.begin();
				P[k][to]+=1/(H*W*2.0);
				C[k][to]+=(i+1)*(j+1)/(H*W*2.0);
			}
		}

		int i0=find(S.begin(),S.end(),board_to_state(B0))-S.begin();
		int i1=find(S.begin(),S.end(),board_to_state(B1))-S.begin();

		static double A[252][252];
		double b[252]={},x[252];
		rep(i,m){
			if(i==i1){
				b[i]=0;
				rep(j,m) A[i][j]=(i==j?1:0);
			}
			else{
				rep(j,m){
					A[i][j]=(i==j?1:0)-P[i][j];
					b[i]+=C[i][j];
				}
			}
		}

		Gauss_Jordan(m,A,b,x);

		printf("%.9f\n",x[i0]);
	}

	return 0;
}