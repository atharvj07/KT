#include <cstdio>
#include <algorithm>
using namespace std;
const int N=100010;
const int INF=1e9;
const int MOD=1e9+7;
int n,m;
int a[N],b[N];
struct Point{
	int x,y;
	friend bool operator == (const Point &a,const Point &b){
		return a.x==b.x&&a.y==b.y;
	}
}p[N];
int d[N],dcnt;
int f[N];
void readData(){
	scanf("%d%d",&n,&m);
	for(int i=1;i<=n;i++) scanf("%d",&a[i]);
	for(int i=1;i<=m;i++) scanf("%d",&b[i]);
}
void initDis(){
	int cnt=1;
	p[1]=(Point){0,0};
	for(int i=1,j;i<=n;i++){
		j=upper_bound(b+1,b+1+m,a[i])-b;
		if(1<j&&j<=m)
			p[++cnt]=(Point){a[i]-b[j-1],b[j]-a[i]};
	}
	p[++cnt]=(Point){INF,INF};
	n=cnt;
}
void Diz(){
	for(int i=1;i<=n;i++)
		d[++dcnt]=p[i].y;
	sort(d+1,d+1+dcnt);
	dcnt=unique(d+1,d+1+dcnt)-d-1;
	for(int i=1;i<=n;i++)
		p[i].y=lower_bound(d+1,d+1+dcnt,p[i].y)-d;
}
namespace BIT{
	int n;
	int a[N];
	void setup(int _n){
		n=_n;
	}
	void add(int u,int x){
		for(;u&&u<=n;u+=u&-u)
			(a[u]+=x)%=MOD;
	}
	int que(int u){
		int res=0;
		for(;u;u-=u&-u)
			(res+=a[u])%=MOD;
		return res;
	}
}
bool cmpByX(const Point &a,const Point &b){
	if(a.x!=b.x)
		return a.x<b.x;
	return a.y<b.y;
}
void solve(){
	sort(p+1,p+1+n,cmpByX);
	n=unique(p+1,p+1+n)-p-1;
	BIT::setup(dcnt);
	BIT::add(p[1].y,1);
	for(int i=2,j;i<=n;i=j){
		for(j=i;j<=n&&p[j].x==p[i].x;j++);
		for(int k=i;k<j;k++)
			f[k]=BIT::que(p[k].y-1);
		for(int k=i;k<j;k++)
			BIT::add(p[k].y,f[k]);
	}
	printf("%d\n",f[n]);
}
int main(){
	readData();
	initDis();
	Diz();
	solve();
	return 0;
}
