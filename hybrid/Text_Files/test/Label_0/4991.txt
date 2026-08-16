#include<iostream>
using namespace std;

class dice{	
public:
	int d[7];
	int set();
	int E();
	int W();
	int N();
	int S();
	int R();//?°´???????????¢
	int C(int *,int *,int *,int *);//??\??????????????????
};
int dice::set(){
	for(int i=1;i<=6;i++){
		cin>>d[i];
	}
	return 0;
}
int dice::C(int *w,int *x,int *y,int *z){
	int a[4];
	a[0]=*w;
	a[1]=*x;
	a[2]=*y;
	a[3]=*z;
	*w=a[3];
	*x=a[0];
	*y=a[1];
	*z=a[2];
	return 0;
}
int dice::E(){
	C(&d[1],&d[3],&d[6],&d[4]);
	return 0;
}
int dice::W(){
	C(&d[1],&d[4],&d[6],&d[3]);
	return 0;
}
int dice::N(){
	C(&d[1],&d[5],&d[6],&d[2]);
	return 0;
}
int dice::S(){
	C(&d[1],&d[2],&d[6],&d[5]);
	return 0;
}
int dice::R(){
	C(&d[2],&d[4],&d[5],&d[3]);
	return 0;
}
int main(){
	dice A,B;
	A.set();
	B.set();
	for(int i=0;i<4;i++){
		B.E();
		if(B.d[1]==A.d[1])break;
	}
	for(int i=0;i<4;i++){
		B.N();
		if(B.d[1]==A.d[1])break;
	}
	for(int i=0;i<4;i++){
		B.R();
		int l=0;
		for(int j=0;j<4;j++){
			if(A.d[j+1]==B.d[j+1]){
				l++;
			}
		}
		if(l==4){
			cout<<"Yes"<<endl;
			goto last;
		}
	}
	cout<<"No"<<endl;
	last:
	return 0;
}