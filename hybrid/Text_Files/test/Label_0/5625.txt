#include<iostream>
#include<vector>
#include<algorithm>
#include<cstring>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<ctime>
#include<queue>
#include<set>
#include<map>
#include<stack>
#include<bitset>
using namespace std;
typedef long long LL;
int gi() {
	int w=0;bool q=1;char c=getchar();
	while ((c<'0'||c>'9') && c!='-') c=getchar();
	if (c=='-') q=0,c=getchar();
	while (c>='0'&&c <= '9') w=w*10+c-'0',c=getchar();
	return q? w:-w;
}
const int N=2e5+100;
int a[N],b[N],c[N];
int fa[N];inline int find(int x) { return fa[x]==x?x:fa[x]=find(fa[x]); }
int main()
{
	int n=gi(),i,m=0;map<int,int>tot;
	for (i=1;i<=n;i++) a[0]^=a[i]=gi();
	for (i=1;i<=n;i++) b[0]^=b[i]=gi();
	for (i=0;i<=n;i++) if (a[i]^b[i]) tot[c[m++]=a[i]]++,tot[c[m++]=b[i]]--;
	
	for (auto p:tot) if (p.second) return puts("-1"),0;

	sort(c,c+m);
	m=unique(c,c+m)-c;

	for (i=0;i<m;i++) fa[i]=i;
	int ans=m;
	for (i=1;i<=n;i++)
		if (a[i]^b[i]) {
			a[i]=lower_bound(c,c+m,a[i])-c;
			b[i]=lower_bound(c,c+m,b[i])-c;
			if (find(a[i])==find(b[i])) ans++;
			else fa[find(a[i])]=find(b[i]);
		}
	for (i=0;i<m;i++) if (c[i]==a[0]) ans--;
	printf("%d\n",ans);
	return 0;
}
