#include<stdio.h>
int main(void)
{
	int h1,h2,k1,k2,a,b,c,d,x,y;
	scanf("%d %d",&h1,&h2);
	scanf("%d %d",&k1,&k2);
	scanf("%d %d %d %d",&a,&b,&c,&d);
	x=(h1*a)+(h2*b)+((h1/10)*c)+((h2/20)*d); 
	y=(k1*a)+(k2*b)+((k1/10)*c)+((k2/20)*d);
	if(x>y){
		printf("hiroshi\n");
	}
	if(x<y){
		printf("kenjiro\n");
	}
	if(x==y){
		printf("even\n");
	}
	return 0;
}

