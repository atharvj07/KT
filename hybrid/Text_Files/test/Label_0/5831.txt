#include<cstdio>
#include<algorithm>
#include<functional>
using namespace std;
int main(void)
{
	int n,m,a,cnt,i;
	scanf("%d %d",&n,&m);
	cnt=0;
	for(i=0;i<m;i++)	{
		scanf("%d",&a);
		if(a>m)	cnt++;
	}
	printf("%d\n",cnt);
	return 0;
}
