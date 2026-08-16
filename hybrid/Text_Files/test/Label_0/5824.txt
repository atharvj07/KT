#include <stdio.h>
int main(void){
	int t,n;
	int i;
	
	for(i=0;i<4;i++){
		scanf("%d %d",&t,&n);
		
		if(t==1){
			printf("%d\n",6000*n);
		}
		if(t==2){
			printf("%d\n",4000*n);
		}
		if(t==3){
			printf("%d\n",3000*n);
		}
		if(t==4){
			printf("%d\n",2000*n);
		}
	}
		
	
	
	return 0;
}