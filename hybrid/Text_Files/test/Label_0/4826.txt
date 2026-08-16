#include<cstdio>
#include<algorithm>

#define reps(i,f,n) for(int i = f; i < int(n); i++)
#define rep(i,n) reps(i,0,n)

using namespace std;

int p[66666];
int joint[66666];

int main(void){
	int n;
	while(scanf("%d", &n),n){
		rep(i,n)
			scanf("%d", &p[i]);
		rep(i,n-1)
			scanf("%d", &joint[i]);
		
		sort(joint, joint+n-1);
		reverse(joint, joint+n-1);
		
		long long leng = 0;
		rep(i,n)leng+=p[i];
		
		long long maxR = leng * n;
		
		rep(i,n-1){
			leng+=joint[i];
			maxR = max(maxR, leng*(n-i-1));
		}
		
		printf("%lld\n", maxR);
	}
	
	return 0;
}