#include<iostream>
#include<algorithm>
#include<cstdio>
using namespace std;
long long n,a,b[1000000],c,p;
int main(){
	cin>>n;
	for(int i=0;i<n;i++){
		scanf("%d",&a);if(b[0]==1 || c>a){printf("No\n");continue;}
		if(c==a && p!=a){printf("No\n");continue;}p++;
		if(a>=1000000){printf("Yes\n");continue;}
		b[a]++;while(b[a]>=2){b[a]-=2;b[a-1]++;a--;p--;}
		while(c<=999998 && b[c+1]==1)c++;
		printf("Yes\n");
	}
	return 0;
}