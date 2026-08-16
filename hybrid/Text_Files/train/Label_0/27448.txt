#include<cstdio>
#include<cstring>
#include<algorithm>
#define ll long long
#define int long long
#define MN 100005
using namespace std;
inline int in(){
    int x=0;bool f=0;char c;
    for (;(c=getchar())<'0'||c>'9';f=c=='-');
    for (x=c-'0';(c=getchar())>='0'&&c<='9';x=(x<<3)+(x<<1)+c-'0');
    return f?-x:x;
}
int c[MN<<2],d[MN],sum[MN],a[MN],b[MN];
int n,tot,l,r,res;
ll num;
inline void add(int x,int v){
	for (int i=x;i<=((n<<1)|1);i+=i&(-i)) c[i]+=v; 
}
inline int query(int x){
	int res=0;
	for (int i=x;i;i-=i&(-i)) res+=c[i];
	return res;
}
inline bool check(int x){
	for (int i=1;i<=n;++i) sum[i]=sum[i-1]+(a[i]>b[x]);
	for (int i=1;i<=n;++i) d[i]=(sum[i]<<1)-i+n+1;d[0]=n+1;
	memset(c,0,sizeof(c));
	add(d[0],1);num=0ll;
	for (int i=1;i<=n;++i)
	num+=1ll*(query(((n<<1)|1))-query(d[i])),add(d[i],1);
	return (num>1ll*(n*(n+1ll))/4ll);
}
signed main()
{
	n=in();
	for (int i=1;i<=n;++i) a[i]=b[i]=in();
	sort(b+1,b+n+1);
	tot=unique(b+1,b+n+1)-b-1;
	l=0,r=tot,res=0;
	while (l<=r){
		int mid=(l+r)>>1;
		if (check(mid)) res=mid,r=mid-1;
		else l=mid+1;
	}
	printf("%d",b[res]);return 0;
}