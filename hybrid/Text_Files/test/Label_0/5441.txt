#include<cstdio>
int N,ans;
int main(){
	scanf("%d",&N);
	for(int h=0,a;N--;){
		scanf("%d",&a);
		if(a>1<<h)while(1<<h<a)h++,ans++;
		else while(1<<h>a)h--;
	}
	printf("%d\n",ans);
}