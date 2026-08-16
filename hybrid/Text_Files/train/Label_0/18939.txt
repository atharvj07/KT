#include<iostream>
#include<vector>
#include<cmath>
int main(){
	while(1){
		int a=0,b=0,c=0;
		std::cin>>a>>b>>c;
		if(a==0&&b==0&&c==0)break;
		int d=0;
		std::cin>>d;
		int p=0,q=0;
		if(a>b&&a>c){
			p=b*b+c*c;
		}else if(b>a&&b>c){
			p=a*a+c*c;
		}else if(c>a&&c>b){
			p=a*a+b*b;
		}
		q=sqrt(p);
		for(int i=0;i<d;i++){
			int n=0;
			std::cin>>n;
			if(2*n>q){
				std::cout<<"OK"<<std::endl;
			}else{
				std::cout<<"NA"<<std::endl;
			}
		}
	}
	return 0;
}