#include<bits/stdc++.h>
using namespace std;
int main(){
	int a1=0,a2=0,a4=0,a;
	int n;
	scanf("%d",&n);
	for(int i=0;i<n;i++){
		scanf("%d",&a);
		if(a%4==0)	a4++;
		else if(a%2==0)	a2++;
		else a1++; 
	}
	if(a2==0&&a1<=a4+1){
		printf("Yes\n");return 0;
	}	
	if(a1<=a4&&a2>0){
		printf("Yes\n");return 0;
	}
	printf("No\n");
	return 0;
}