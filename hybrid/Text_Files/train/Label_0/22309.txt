#include<stdio.h>
#include<algorithm>
#include<set>
#include<vector>
#include<queue>

using namespace std;
char in[5][5][5];
char tmp[5][5][5];
int bit[30][24];
int mw[30][24];
int md[30][24];
int mh[30][24];
int SZ[30];

int W,D,H;
int w,d,h;
const int D_MAX_V=30;
const int D_v_size=30;
struct D_wolf{
	int t,c,r;
	D_wolf(){t=c=r=0;}
	D_wolf(int t1,int c1,int r1){
		t=t1;c=c1;r=r1;
	}
};
vector<D_wolf>D_G[D_MAX_V];
int D_level[D_MAX_V];
int D_iter[D_MAX_V];

void add_edge(int from,int to,int cap){
	D_G[from].push_back(D_wolf(to,cap,D_G[to].size()));
	D_G[to].push_back(D_wolf(from,0,D_G[from].size()-1));
}
void D_bfs(int s){
	for(int i=0;i<D_v_size;i++)D_level[i]=-1;
	queue<int> Q;
	D_level[s]=0;
	Q.push(s);
	while(Q.size()){
		int v=Q.front();
		Q.pop();
		for(int i=0;i<D_G[v].size();i++){
			if(D_G[v][i].c>0&&D_level[D_G[v][i].t]<0){
				D_level[D_G[v][i].t]=D_level[v]+1;
				Q.push(D_G[v][i].t);
			}
		}
	}
}
int D_dfs(int v,int t,int f){
	if(v==t)return f;
	for(;D_iter[v]<D_G[v].size();D_iter[v]++){
		int i=D_iter[v];
		if(D_G[v][i].c>0&&D_level[v]<D_level[D_G[v][i].t]){
			int d=D_dfs(D_G[v][i].t,t,min(f,D_G[v][i].c));
			if(d>0){
				D_G[v][i].c-=d;
				D_G[D_G[v][i].t][D_G[v][i].r].c+=d;
				return d;
			}
		}
	}
	return 0;
}
int max_flow(int s,int t){
	int flow=0;
	for(;;){
		D_bfs(s);
		if(D_level[t]<0)return flow;
		for(int i=0;i<D_v_size;i++)D_iter[i]=0;
		int f;
		while((f=D_dfs(s,t,99999999))>0){flow+=f;}
	}
	return 0;
}
int dx[]={1,-1,0,0,0,0};
int dy[]={0,0,1,-1,0,0};
int dz[]={0,0,0,0,1,-1};
int check(int a){
	for(int i=0;i<D_MAX_V;i++){
		D_G[i].clear();D_level[i]=D_iter[i]=0;
	}
	int S=W*H*D;
	int T=W*H*D+1;
	for(int i=0;i<H;i++){
		for(int j=0;j<D;j++){
			for(int k=0;k<W;k++){
				if(a&(1<<(i*D*W+j*W+k)))continue;
				if((i+j+k)%2){
					add_edge(i*D*W+j*W+k,T,1);
					continue;
				}
				add_edge(S,i*D*W+j*W+k,1);
				for(int l=0;l<6;l++){
					int ti=i+dx[l];
					int tj=j+dy[l];
					int tk=k+dz[l];
					if(ti<0||ti>=H||tj<0||tj>=D||tk<0||tk>=W)continue;
					if(a&(1<<(ti*D*W+tj*W+tk)))continue;
					add_edge(i*D*W+j*W+k,ti*D*W+tj*W+tk,1);
				}
			}
		}
	}
	return max_flow(S,T);
}
void right(){
	for(int i=0;i<h;i++)for(int j=0;j<d;j++)for(int k=0;k<w;k++)
		tmp[i][k][d-1-j]=in[i][j][k];
	swap(d,w);
	for(int i=0;i<h;i++)for(int j=0;j<d;j++)for(int k=0;k<w;k++)
		in[i][j][k]=tmp[i][j][k];
}
void front(){
	for(int i=0;i<h;i++)for(int j=0;j<d;j++)for(int k=0;k<w;k++)
		tmp[d-1-j][i][k]=in[i][j][k];
	swap(h,d);
	for(int i=0;i<h;i++)for(int j=0;j<d;j++)for(int k=0;k<w;k++)
		in[i][j][k]=tmp[i][j][k];
}
int calc(){
	int ret=0;
	for(int i=0;i<h;i++)for(int j=0;j<d;j++)for(int k=0;k<w;k++){
		if(in[i][j][k]=='*')ret+=1<<(i*D*W+j*W+k);
	}
	return ret;
}
int n;
pair<int,int>ev[30];
set<int>vis;
int has[30];
int twos;
int ch[30];
int dfs(int a,int b){
	if(a==n){
		int mat=check(b);
	//	printf("%d %d\n",b,mat);
		if(mat>=twos)return 1;
		else return 0;
	}
	if(vis.count(b))return 0;
	int at=ev[a].second;
	if(SZ[at]==0)return 0;
	if(has[at]<=2){
		return dfs(a+1,b);
	}
	int black=0;
	int white=0;
	int pos=ch[a];
	for(int i=0;i<W*H*D;i++)if(!(b&(1<<i))){
		if((i/(W*H)+i%(W*H)/W+i%W)%2)black++;
		else white++;
	}
	for(int i=0;i<a;i++)if(has[ev[i].second]==1)pos++;
	if(max(black-white,white-black)>pos){vis.insert(b);return 0;}
	for(int i=0;i<SZ[at];i++){
		if(a==0&&W==H&&H==D&&i>0)break;
		if(i&&bit[at][i]==bit[at][i-1])continue;
		for(int j=0;j<=H-mh[at][i];j++){
			for(int k=0;k<=D-md[at][i];k++){
				for(int l=0;l<=W-mw[at][i];l++){
					int val=bit[at][i]<<(j*D*W+k*W+l);
					if(b&val)continue;
					if(dfs(a+1,b+val)){
						return 1;
					}
				}
			}
		}
	}
	vis.insert(b);
	return 0;
}
int main(){
	int a,b,c;
	while(scanf("%d%d%d%d",&a,&b,&c,&n),n){
		vis.clear();
		W=a;D=b;H=c;
		twos=0;
		for(int i=0;i<30;i++)for(int j=0;j<24;j++){
			bit[i][j]=mw[i][j]=md[i][j]=mh[i][j]=0;
		}
		for(int i=0;i<30;i++)has[i]=0;
		int tot=0;
		for(int i=0;i<n;i++){
			scanf("%d%d%d",&w,&d,&h);
			for(int j=0;j<h;j++){
				for(int k=0;k<d;k++){
					scanf("%s",in[j][k]);
					for(int l=0;l<w;l++)if(in[j][k][l]=='*')has[i]++;
				}
			}
			if(has[i]==2)twos++;
			while(1){
				bool chk=true;
				for(int j=0;j<d;j++)for(int k=0;k<w;k++)if(in[0][j][k]=='*')chk=false;
				if(!chk)break;
				for(int j=1;j<h;j++)for(int k=0;k<d;k++)for(int l=0;l<w;l++)in[j-1][k][l]=in[j][k][l];
				h--;
			}
			while(1){
				bool chk=true;
				for(int j=0;j<d;j++)for(int k=0;k<w;k++)if(in[h-1][j][k]=='*')chk=false;
				if(!chk)break;
				h--;
			}
			while(1){
				bool chk=true;
				for(int j=0;j<h;j++)for(int k=0;k<w;k++)if(in[j][0][k]=='*')chk=false;
				if(!chk)break;
				for(int j=0;j<h;j++)for(int k=1;k<d;k++)for(int l=0;l<w;l++)in[j][k-1][l]=in[j][k][l];
				d--;
			}
			while(1){
				bool chk=true;
				for(int j=0;j<h;j++)for(int k=0;k<w;k++)if(in[j][d-1][k]=='*')chk=false;
				if(!chk)break;
				d--;
			}
			while(1){
				bool chk=true;
				for(int j=0;j<h;j++)for(int k=0;k<d;k++)if(in[j][k][0]=='*')chk=false;
				if(!chk)break;
				for(int j=0;j<h;j++)for(int k=0;k<d;k++)for(int l=1;l<w;l++)in[j][k][l-1]=in[j][k][l];
				w--;
			}
			while(1){
				bool chk=true;
				for(int j=0;j<h;j++)for(int k=0;k<d;k++)if(in[j][k][w-1]=='*')chk=false;
				if(!chk)break;
				w--;
			}
			int sz=0;
			for(int j=0;j<4;j++){
				for(int k=0;k<4;k++){
					if(w<=W&&d<=D&&h<=H)bit[i][sz++]=calc();
					right();
				}
				front();
			}right();front();
			for(int j=0;j<4;j++){
				if(w<=W&&d<=D&&h<=H)bit[i][sz++]=calc();
				right();
			}
			front();front();
			for(int j=0;j<4;j++){
				if(w<=W&&d<=D&&h<=H)bit[i][sz++]=calc();
				right();
			}
			for(int j=0;j<sz;j++){
				//printf("%d ",bit[i][j]);
				while(bit[i][j]%(1<<(W*D))==0){
					bit[i][j]/=(1<<(W*D));
				}
				int td=0;for(int k=0;k<H;k++)td+=(((1<<W)-1)<<(k*D*W));
				while((td&bit[i][j])==0){
					bit[i][j]/=(1<<W);
				}
				int tw=0;for(int k=0;k<H;k++)for(int l=0;l<D;l++)tw+=(1<<(k*D*W+l*W));
			//	printf("%d\n",tw);
				while((tw&bit[i][j])==0){
					bit[i][j]/=2;
				}
			}//printf("\n");
			std::sort(bit[i],bit[i]+sz);
			for(int j=0;j<sz;j++){
				for(int k=0;k<H;k++)for(int l=0;l<D;l++)for(int o=0;o<W;o++)
					if(bit[i][j]&(1<<(k*D*W+l*W+o))){
						mh[i][j]=max(mh[i][j],k+1);
						md[i][j]=max(md[i][j],l+1);
						mw[i][j]=max(mw[i][j],o+1);
					}
			}
			SZ[i]=sz;
		}
		for(int i=0;i<n;i++){
			int sum=0;
			for(int j=0;j<SZ[i];j++){
				if(j&&bit[i][j]==bit[i][j-1])continue;
				//printf("%d ",bit[i][j]);
				sum+=(H-mh[i][j]+1)*(W-mw[i][j]+1)*(D-md[i][j]+1);
			}//printf("\n");
			ev[i]=make_pair(-has[i],i);
		}
	//	printf("do\n");
		std::sort(ev,ev+n);
		
		int bw=0;
		for(int i=n-1;i>=0;i--){
			if(SZ[i]==0)continue;
			int black=0;
			int white=0;
			for(int j=0;j<mh[i][0];j++)for(int k=0;k<md[i][0];k++)for(int l=0;l<mw[i][0];l++)
				if(bit[i][0]&(1<<(j*D*W+k*W+l))){
					if((j+k+l)%2)black++;
					else white++;
				}
			bw+=max(black-white,white-black);
			ch[i]=bw;
		}
		if(dfs(0,0))printf("Yes\n");
		else printf("No\n");
	}
}