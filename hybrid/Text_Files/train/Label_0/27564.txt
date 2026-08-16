#include <bits/stdc++.h>
using namespace std;
#define rep(i,m,n) for((i)=(m);i<(n);i++)
typedef int long long ll;

int main(){
	int a,b,c;
	int ans=0;
	int d,e,f;
	scanf("%d %d %d",&a,&b,&c);
	while(a%2==0&&b%2==0&&c%2==0){
		d=a;e=b;
		a=b/2+c/2;b=c/2+d/2;c=d/2+e/2;ans++;
		if(a==b&&b==c){printf("%d\n",-1);return 0;}
	}
	printf("%d\n",ans);
	return 0;
}
