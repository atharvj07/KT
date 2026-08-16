#include<stdio.h>

int table[14][14];

int main(){
	int a,b,c;
	while(~scanf("%d,%d,%d",&a,&b,&c)){
		a+=2;
		b+=2;
		switch(c){
			case 3:
				table[a-2][b]++;
				table[a+2][b]++;
				table[a][b-2]++;
				table[a][b+2]++;
			case 2:
				table[a+1][b+1]++;
				table[a-1][b-1]++;
				table[a+1][b-1]++;
				table[a-1][b+1]++;
			case 1:
				table[a][b+1]++;
				table[a][b-1]++;
				table[a-1][b]++;
				table[a+1][b]++;
				table[a][b]++;
		}
	}
	int max=0;
	int ans=0;
	for(int i=2;i<12;i++){
		for(int j=2;j<12;j++){
			if(table[i][j]>0)ans++;
			if(table[i][j]>max)max=table[i][j];
		}
	}
	printf("%d\n%d\n",100-ans,max);
}