#include<iostream>
using namespace std;
int main(){
	int i,H,j,W;
	
	for(;;){
		cin>>H>>W;
		if(H==0 && W==0)break;
		for(i=1;i<=H;i++){
			for(j=1;j<=W;j++){
				if((i+j)%2==0){
				cout<<"#";
			    }
				else{
                cout<<".";
				}
			}
			cout<<endl;
		}
		cout<<endl;
	}
	return 0;
}