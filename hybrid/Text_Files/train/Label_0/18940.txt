#include<stdio.h>
#include<math.h>
#define M(a,b) (a<b?a:b)
int main(){
	for(int a,b,c,n,r;scanf("%d%d%d",&a,&b,&c),a|b|c;){
		for(scanf("%d",&n);n--;){
			scanf("%d",&r);
			puts(
				(2*r>M(M(sqrt(a*a+b*b),sqrt(b*b+c*c)),sqrt(c*c+a*a)))?
				"OK":"NA"
			);
		}
	}
}