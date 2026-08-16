#include <bits/stdc++.h>
#define yabs(x) ((x<0)?(-(x)):(x))

using namespace std;
typedef long long LL;

const int N=1e5+10;

struct Edge{ int to,next;} way[N<<1];

int n,m,tot,num[N],col[N],d[N],X,Y,k[N],sum[N];
LL ans;

void Build(int a,int b) { way[++tot]=(Edge){b,num[a]}; num[a]=tot; }

void Init()
{
	scanf("%d%d",&n,&m);
	int a,b; tot=1;
	for (int i=1;i<=m;++i)
	{
		scanf("%d%d",&a,&b);
		Build(a,b); Build(b,a); 
		d[a]++; d[b]++;
	}
}

bool vis[N],fl,use[N];
int Dfs(int x,int fa,int c)
{
	vis[x]=1; col[x]=c;
	int cnt=c;
	for (int i=num[x];i;i=way[i].next)
	{
		int v=way[i].to;
		if (v==fa) continue;
		if (vis[v])
		{
			X=x; Y=v;
			if (col[x]==col[v]) fl=1;
			else fl=0;
		}
		else use[i>>1]=1,cnt+=Dfs(v,x,-c);
	}
	ans+=yabs(cnt);
	return cnt;
}

void Dp(int x,int fa)
{
	sum[x]=col[x];
	for (int i=num[x];i;i=way[i].next)
	{
		int v=way[i].to;
		if (v==fa || !use[i>>1]) continue;
		Dp(v,x);
		sum[x]+=sum[v]; k[x]+=k[v];
	}
}

int P[N];
void Solve()
{
	if (n==2) { printf("1\n"); return ; }
	int root=1;
	if (m==n-1) 
	{ 
		ans=0;
		int sum=Dfs(root,0,1); 
		if (sum!=0) printf("-1\n");
		else printf("%lld\n",ans);
	}else 
	{
		int summ=Dfs(root,0,1);
		if (fl)
		{
			Dp(root,0); ans=0;
			if (sum[root]%2) printf("-1\n");
			else 
			{
				int summ=sum[root];
				col[X]-=sum[root]/2; col[Y]-=sum[root]/2;
				Dp(root,0);
				for (int i=1;i<=n;++i) ans+=yabs(sum[i]);
				printf("%lld\n",ans+yabs(summ)/2);
			}
		}else
		{
			ans=0;
			k[X]++; k[Y]--;
			Dp(root,0);
			if (sum[1]) { printf("-1\n"); return ;}
			int top=0;
			for (int i=1;i<=n;++i)
				if (k[i]==-1) P[++top]=sum[i];
				else if (k[i]==1) P[++top]=-sum[i];
				else ans+=yabs(sum[i]);
			P[++top]=0;
			sort(P+1,P+top+1);
			int chose=P[(top+1)/2];
			for (int i=1;i<=top;++i) ans+=yabs(chose-P[i]);
			printf("%lld\n",ans);
		}
	}
}

int main()
{   
	Init();
	Solve();
	return 0;
}