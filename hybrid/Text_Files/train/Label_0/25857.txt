#include<cstdio>
#include<vector>
#include<cmath>
#include<queue>
#include<cassert>
#include<utility>
#include<algorithm>

using namespace std;

typedef double Real;
typedef pair<int,int> P;

const Real eps=1e-7;
const Real inf=1e9;

template<class T> bool eq(T a,T b){
	return abs(a-b)<eps;
}
template<class T> int sgn(T a){
	if(eq(a,0.0)) return 0;
	if(a>0) return 1;
	return -1;
}

//vector<Real> vals;
Real vals[140];
int vals_id=0;
//vector<int> valid_vnum;
int valid_vnum[7000];
int valid_vnum_id=0;

int rev_valid_vnum[140*140*140];

int encode(Real x,Real y,Real z){
//	int xid = distance(vals.begin(),lower_bound(vals.begin(),vals.end(),x-eps));
//	int yid = distance(vals.begin(),lower_bound(vals.begin(),vals.end(),y-eps));
//	int zid = distance(vals.begin(),lower_bound(vals.begin(),vals.end(),z-eps));
	int xid=lower_bound(vals,vals+vals_id,x-eps)-vals;
	int yid=lower_bound(vals,vals+vals_id,y-eps)-vals;
	int zid=lower_bound(vals,vals+vals_id,z-eps)-vals;
//	int v=xid + vals.size()*yid + vals.size()*vals.size()*zid;
	int v=xid + vals_id*yid + vals_id*vals_id*zid;
//	int res = distance(valid_vnum.begin(),lower_bound(valid_vnum.begin(),valid_vnum.end(),v));
//	int res = lower_bound(valid_vnum,valid_vnum+valid_vnum_id,v)-valid_vnum;
	int res = rev_valid_vnum[v];
	return res;
}

const int V = 10000;// 140*140*140;

int head[V],to[500500],nxt[500500],m;
Real cost[500500];
void init_edge(){
	for(int i=0;i<V;i++) head[i]=-1;
	m=0;
}
void add_edge(int u,int v,Real c){
	nxt[m]=head[u];to[m]=v;cost[m]=c;head[u]=m;m++;
	nxt[m]=head[v];to[m]=u;cost[m]=c;head[v]=m;m++;
	if(m>500000) assert(0);
}

//vector<Real> as,bs,cs,ds;
Real as[2200],bs[2200],cs[2200],ds[2200];
int aid=0;
typedef pair<Real,Real> PR;
int gcd(int x,int y){
	if(x<y) return gcd(y,x);
	if(y==0) return x;
	return gcd(y,x%y);
}

PR tmp[30];

void genEdges(){
	for(int i=1;i<=12;i++) for(int j=1;j<=12;j++){
		if(gcd(i,j)!=1) continue;
	//	vector<PR> tmp;
		int tmp_id=0;
		for(int k=1;k<i;k++){
			Real y=(Real)k*j/i;
		//	tmp.push_back(PR(k,y));
			tmp[tmp_id++]=PR(k,y);
		}
		for(int k=1;k<j;k++){
			Real x=(Real)i*k/j;
		//	tmp.push_back(PR(x,k));
			tmp[tmp_id++]=PR(x,k);
		}
		//tmp.push_back(PR(0,0));
		//tmp.push_back(PR(i,j));
		tmp[tmp_id++]=PR(0,0);
		tmp[tmp_id++]=PR(i,j);
//		sort(tmp.begin(),tmp.end());
		sort(tmp,tmp+tmp_id);
/*		if(i == 3 && j == 4){
			for(int k = 0; k < tmp.size(); k++){
				printf("%f %f\n",tmp[k].first,tmp[k].second);
			}
//			exit(0);
		}*/
	//	for(int k=0;k+1<tmp.size();k++){
		for(int k=0;k+1<tmp_id;k++){
			Real a_=tmp[k].first;
			Real a=a_-(int)(a_+eps);
			Real b_=tmp[k].second;
			Real b=b_-(int)(b_+eps);
			Real c_=tmp[k+1].first;
			Real c=c_-(int)(c_-eps);
			Real d_=tmp[k+1].second;
			Real d=d_-(int)(d_-eps);
		/*	as.push_back(a);
			bs.push_back(b);
			cs.push_back(c);
			ds.push_back(d);
			as.push_back(1-a);
			bs.push_back(b);
			cs.push_back(1-c);
			ds.push_back(d);*/
			as[aid]=a;
			bs[aid]=b;
			cs[aid]=c;
			ds[aid]=d;
			aid++;
			as[aid]=1-a;
			bs[aid]=b;
			cs[aid]=1-c;
			ds[aid]=d;
			aid++;
//			if(i == 3 && j == 4){
//				printf("%f %f %f %f\n", a,b,c,d);
//			}
		}
	}
/*	for(int i=0;i<as.size();i++){
		printf("%.2f %.2f %.2f %.2f\n",as[i],bs[i],cs[i],ds[i]);
	}
	exit(0);*/
}
Real getDis(Real a,Real b,Real c,Real p,Real q,Real r){
	Real d1=a-p,d2=b-q,d3=c-r;
	return sqrt(d1*d1+d2*d2+d3*d3);
}

bool exi[5][5][5];
void genGraph(){
//	int cntOut=0;
/*	for(int i=0;i<140*140*140;i++){
		G[i].clear();
	}*/
	init_edge();
	for(int x=1;x<=4;x++){
		for(int y=1;y<=3;y++) for(int z=1;z<=3;z++){
			int cnt=0;
			if(exi[x-1][y][z]) cnt++;
			if(exi[x][y][z]) cnt++;
			if(cnt!=1) continue;
		//	for(int i=0;i<as.size();i++){
			for(int i=0;i<aid;i++){
				Real x1=x,y1_=y+as[i],z1=z+bs[i];
				Real x2=x,y2_=y+cs[i],z2=z+ds[i];
				int u=encode(x1,y1_,z1);
				int v=encode(x2,y2_,z2);
				Real d=getDis(x1,y1_,z1,x2,y2_,z2);
				add_edge(u,v,d);
		//		G[u].push_back(edge(v,d));
		//		G[v].push_back(edge(u,d));
		//		if(++cntOut<=20){
					//printf("%d %d\n",u,v);
//					printf("%.2f %.2f %.2f %.2f %.2f %.2f\n",
//					x1,y1_,z1,x2,y2_,z2);
		//		}
			}
		}
	}
	for(int y=1;y<=4;y++){
		for(int x=1;x<=3;x++) for(int z=1;z<=3;z++){
			int cnt=0;
			if(exi[x][y-1][z]) cnt++;
			if(exi[x][y][z]) cnt++;
			if(cnt!=1) continue;
		//	for(int i=0;i<as.size();i++){
			for(int i=0;i<aid;i++){
				Real x1=x+as[i],y1_=y,z1=z+bs[i];
				Real x2=x+cs[i],y2_=y,z2=z+ds[i];
				int u=encode(x1,y1_,z1);
				int v=encode(x2,y2_,z2);
				Real d=getDis(x1,y1_,z1,x2,y2_,z2);
				add_edge(u,v,d);
			//	G[u].push_back(edge(v,d));
			//	G[v].push_back(edge(u,d));
			}
		}
	}
	for(int z=1;z<=4;z++){
		for(int x=1;x<=3;x++) for(int y=1;y<=3;y++){
			int cnt=0;
			if(exi[x][y][z]) cnt++;
			if(exi[x][y][z-1]) cnt++;
			if(cnt!=1) continue;
		//	for(int i=0;i<as.size();i++){
			for(int i=0;i<aid;i++){
				Real x1=x+as[i],y1_=y+bs[i],z1=z;
				Real x2=x+cs[i],y2_=y+ds[i],z2=z;
				int u=encode(x1,y1_,z1);
				int v=encode(x2,y2_,z2);
				Real d=getDis(x1,y1_,z1,x2,y2_,z2);
				add_edge(u,v,d);
			//	G[u].push_back(edge(v,d));
			//	G[v].push_back(edge(u,d));
			}
		}
	}
	//TODO: add edges coincide with cubes' edges
	for(int y=1;y<=4;y++) for(int z=1;z<=4;z++){
		for(int x=1;x<=3;x++){
			int cnt=0;
			for(int y_=y-1;y_<=y;y_++) for(int z_=z-1;z_<=z;z_++){
				if(exi[x][y_][z_]) cnt++;
			}
			if(cnt==0||cnt==4) continue;
			int u=encode(x,y,z);
			int v=encode(x+1,y,z);
			add_edge(u,v,1);
		//	G[u].push_back(edge(v,1));
		//	G[v].push_back(edge(u,1));
		}
	}
	for(int z=1;z<=4;z++) for(int x=1;x<=4;x++){
		for(int y=1;y<=3;y++){
			int cnt=0;
			for(int z_=z-1;z_<=z;z_++) for(int x_=x-1;x_<=x;x_++){
				if(exi[x_][y][z_]) cnt++;
			}
			if(cnt==0||cnt==4) continue;
			int u=encode(x,y,z);
			int v=encode(x,y+1,z);
			add_edge(u,v,1);
		//	G[u].push_back(edge(v,1));
		//	G[v].push_back(edge(u,1));
		}
	}
	for(int x=1;x<=4;x++) for(int y=1;y<=4;y++){
		for(int z=1;z<=3;z++){
			int cnt=0;
			for(int x_=x-1;x_<=x;x_++) for(int y_=y-1;y_<=y;y_++){
				if(exi[x_][y_][z]) cnt++;
			}
			if(cnt==0||cnt==4) continue;
			int u=encode(x,y,z);
			int v=encode(x,y,z+1);
			add_edge(u,v,1);
		//	G[u].push_back(edge(v,1));
		//	G[v].push_back(edge(u,1));
		}
	}
}

bool checkInt(int id){
	Real x=vals[id];
	int x_=(int)(x+eps);
	return eq(x,(Real)x_);
}
void init(){
	for(int i=2;i<=12;i++){
		for(int j=1;j<i;j++){
			if(gcd(i,j)!=1) continue;
			Real x=(Real)j/i;
			for(int k=1;k<=3;k++){
		//		vals.push_back(x+k);
				vals[vals_id++]=x+k;
			}
		}
	}
//	for(int k=1;k<=4;k++) vals.push_back(k);
	for(int k=1;k<=4;k++) vals[vals_id++]=k;
//	sort(vals.begin(),vals.end());
	sort(vals,vals+vals_id);
	genEdges();
//	for(int i=0;i<vals.size();i++) for(int j=0;j<vals.size();j++) for(int k=0;k<vals.size();k++){
	for(int i=0;i<vals_id;i++) for(int j=0;j<vals_id;j++) for(int k=0;k<vals_id;k++){
		int cnt=0;
		if(checkInt(i)) cnt++;
		if(checkInt(j)) cnt++;
		if(checkInt(k)) cnt++;
		if(cnt<2) continue;
//		valid_vnum.push_back(i+vals.size()*j+vals.size()*vals.size()*k);
//		valid_vnum.push_back(i+vals_id*j+vals_id*vals_id*k);
		valid_vnum[valid_vnum_id++]=i+vals_id*j+vals_id*vals_id*k;
	}
	for(int i=0;i<valid_vnum_id;i++){
		rev_valid_vnum[valid_vnum[i]]=i;
	}
//	printf("%d\n",valid_vnum.size());
//	sort(valid_vnum.begin(),valid_vnum.end());
//	sort(valid_vnum,valid_vnum+valid_vnum_id);
}

Real dis[V];

typedef pair<Real,int> State;
priority_queue<State,vector<State>,greater<State> > que;

Real solve(int x1,int y1,int z1,int x2,int y2,int z2){
//	printf("%d %d %d %d %d %d\n",x1,y1,z1,x2,y2,z2);
	int u=encode(x1,y1,z1);
	int v=encode(x2,y2,z2);
	genGraph();
//	printf("u=%d,v=%d\n",u,v);
//	int V=140*140*140;
	for(int i=0;i<V;i++){
		dis[i]=inf;
	}
	dis[u]=0;
	que.push(State(0,u));
	while(!que.empty()){
		State state = que.top();
		que.pop();
		Real cd = state.first;
		int cv = state.second;
//		printf("cv=%d\n",cv);
		if(sgn(dis[cv]-cd)>0) continue;
//		for(int i=0;i<G[cv].size();i++){
		for(int e=head[cv];e!=-1;e=nxt[e]){
		//	int nv = G[cv][i].to;
			int nv=to[e];
		//	Real nd = cd + G[cv][i].cost;
			Real nd=cd+cost[e];
			if(sgn(dis[nv]-nd)<=0) continue;
			dis[nv]=nd;
			que.push(State(nd,nv));
		}
	}
	return dis[v];
}

int x1,y1_,z1,x2,y2_,z2;

void input(){
	scanf("%d%d%d%d%d%d",&x1,&y1_,&z1,&x2,&y2_,&z2);
	if(x1==0&&y1_==0&&z1==0&&x2==0&&y2_==0&&z2==0) exit(0);
	x1++;y1_++;z1++;x2++;y2_++;z2++;
	for(int i=1;i<=3;i++) for(int j=1;j<=3;j++) for(int k=1;k<=3;k++){
		exi[i][j][k]=false;
	}
	for(int z=1;z<=3;z++) for(int y=1;y<=3;y++){
		char ch[10];
		scanf("%s",ch+1);
		for(int x=1;x<=3;x++){
			exi[x][y][z]=ch[x]=='#';
		}
	}
}

int main(){
	init();
//	printf("%d %d\n",vals.size(),as.size());
//	int t = 0;
//	printf("as.size()=%d\n",as.size());
//	printf("valid_vnum.size()=%d\n",valid_vnum.size());
//	printf("vals.size()=%d\n",vals.size());
	while(true){
//		fprintf(stderr,"%d\n",t++);
		input();
		Real ans=solve(x1,y1_,z1,x2,y2_,z2);
		printf("%f\n",ans);
//		int s = encode(1,1,1);
//		int t = encode(4,4,4);
//		int mid = encode(1.5,1,2);
//		printf("[%d] = %f\n",s,dis[s]);
//		printf("[%d] = %f\n",t,dis[t]);
//		printf("[%d] = %f\n",mid,dis[mid]);
/*		int cnt = 0;
		for(int i = 0; i < 140*140*140;i++){
			if(dis[i] < 1e9){
				if(++cnt<=10){
					decodeAndPrint(i);
					printf("%d->%f\n",i,dis[i]);
				}
			}
		}
		exit(0);*/
	}
	return 0;
}