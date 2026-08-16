#include<bits/stdc++.h>
using namespace std;

typedef long long LL;

const int N=100000,INF=(1<<30)-1;

int n,m,cm,a[N+9],b[N+9],c[N+9];
struct side{
  int y,next;
}e[N*2+9];
int lin[N+9],cs;

void Ins(int x,int y){e[++cs].y=y;e[cs].next=lin[x];lin[x]=cs;}
void Ins2(int x,int y){Ins(x,y);Ins(y,x);}

int deg[N+9][2];

void into(){
  scanf("%d%d",&n,&m);cm=m;
  for (int i=1;i<=m;++i){
	scanf("%d%d%d",&a[i],&b[i],&c[i]);
	Ins2(a[i],b[i]);
	cm-=a[i]==b[i];
	++deg[a[i]][0];++deg[b[i]][1];
  }
}

int vis[N+9],d[N+9],cd;

void Dfs_d(int k){
  vis[d[++cd]=k]=1;
  for (int i=lin[k];i;i=e[i].next)
	if (!vis[e[i].y]) Dfs_d(e[i].y);
}

int id[N+9],opt[N+9];
int cnt;

void Get_opt(){
  for (int i=1;i<=n;++i){
	if (vis[i]) continue;
	cd=0;
	Dfs_d(i);
	int now=cd>1;
	for (int j=1;j<=cd;++j)
	  if (deg[d[j]][0]^1||deg[d[j]][1]^1) now=2;
	if (now==1) ++cnt;
	for (int j=1;j<=cd;++j) id[d[j]]=now;
  }
  for (int i=1;i<=m;++i)
	switch (id[a[i]]){
	  case 0:opt[i]=0;c[i]-=2;break;
	  case 1:opt[i]=1;c[i]-=1;break;
	  case 2:opt[i]=2+(a[i]!=b[i]);c[i]-=1;break;
	}
}

vector<int>w[3];

int Get_ans(int x,int y){
  int res=INF,sum=x;
  for (int vs=w[0].size(),i=0;i<vs;++i) sum+=w[0][i];
  if (sum>=cnt) return cm+y+cnt;
  sum=cnt-sum;
  int now1=0,now2=0;
  for (int vs=w[2].size(),i=0;i<vs;++i)
	if ((now2+=w[2][i])>=sum) res=min(res,cm+cnt+y+(i+1<<1));
  for (int vs=w[1].size(),p1=0,p2=w[2].size()?w[2].size()-1:-1;p1<vs;++p1){
	now1+=w[1][p1];
	for (;p2>=0&&now1+now2-w[2][p2]>=sum;now2-=w[2][p2],--p2);
	if (now1+now2>=sum) res=min(res,cm+cnt+y+p1+1+(p2+1<<1));
  }
  return res;
}

int ans;

void Get_ans(){
  ans=INF;
  if (!cnt) {ans=cm;return;}
  for (int i=1;i<=m;++i)
	if (c[i]>0&&opt[i]>=2) w[opt[i]==2].push_back(c[i]);
  sort(w[0].begin(),w[0].end(),greater<int>());
  sort(w[1].begin(),w[1].end(),greater<int>());
  ans=min(ans,Get_ans(0,0));
  if (!w[0].size()&&!w[1].size()) return;
  int t=w[0].empty(),x=w[t][0];
  w[t].erase(w[t].begin());
  for (int i=1;i<=m;++i)
	if (c[i]>0&&opt[i]<=1) w[opt[i]?0:2].push_back(c[i]);
  sort(w[0].begin(),w[0].end(),greater<int>());
  sort(w[1].begin(),w[1].end(),greater<int>());
  sort(w[2].begin(),w[2].end(),greater<int>());
  //for (auto x:w[0]) printf("%d\n",x);
  //for (auto x:w[1]) printf("%d\n",x);
  //for (auto x:w[2]) printf("%d\n",x);
  ans=min(ans,Get_ans(x,t));
}

void work(){
  Get_opt();
  Get_ans();
}

void outo(){
  printf("%d\n",ans==INF?-1:ans);
}

int main(){
  into();
  work();
  outo();
  return 0;
}