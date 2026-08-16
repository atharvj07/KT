#include<bits/stdc++.h>
using namespace std;
int N;
int main()
{
	while(true){
		scanf("%d",&N);
		if(N==0)return 0;
		int X[30][6];
		for(int i=0;i<N;i++){
			for(int j=0;j<6;j++){
				string SS;
				cin >> SS;
				if(SS=="Cyan")X[i][j]=0;
				if(SS=="Yellow")X[i][j]=1;
				if(SS=="Red")X[i][j]=2;
				if(SS=="Magenta")X[i][j]=3;
				if(SS=="Green")X[i][j]=4;
				if(SS=="Blue")X[i][j]=5;
			}
		}
		int cou=0;
		for(int i=0;i<N;i++){
			bool F=true;
			for(int j=i+1;j<N;j++){
				//equal->false
				for(int k=0;k<6;k++){
					for(int l=0;l<4;l++){
						bool FF=false;
						for(int m=0;m<6;m++){
							//if(i==0&&j==1)printf("%d ",X[i][m]);
							if(X[i][m]!=X[j][m])FF=true;
						}
						//if(i==0&&j==1)printf("\n");
						if(!FF)F=false;
						int t=X[i][1];
						X[i][1]=X[i][2];
						X[i][2]=X[i][4];
						X[i][4]=X[i][3];
						X[i][3]=t;
					}
					if(k==0){
						int t=X[i][0];
						X[i][0]=X[i][1];
						X[i][1]=X[i][5];
						X[i][5]=X[i][4];
						X[i][4]=t;
					}
					if(k==1){
						int t=X[i][0];
						X[i][0]=X[i][2];
						X[i][2]=X[i][5];
						X[i][5]=X[i][3];
						X[i][3]=t;
					}
					if(k==2){
						int t=X[i][2];
						X[i][2]=X[i][3];
						X[i][3]=t;
						t=X[i][5];
						X[i][5]=X[i][0];
						X[i][0]=t;
					}
					if(k==3){
						int t=X[i][0];
						X[i][0]=X[i][3];
						X[i][3]=X[i][5];
						X[i][5]=X[i][2];
						X[i][2]=t;
					}
					if(k==4){
						int t=X[i][0];
						X[i][0]=X[i][1];
						X[i][1]=X[i][5];
						X[i][5]=X[i][4];
						X[i][4]=t;
					}
					
				}
			}
			if(F)cou++;
		}
		printf("%d\n",N-cou);
	}
}