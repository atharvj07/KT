#include<iostream>
#include<algorithm>

using namespace std;

int main(){
	for(int w;cin>>w,~w;){
		int p=1150;			w-=min(w,10);
		p+=125*min(w,10);	w-=min(w,10);
		p+=140*min(w,10);	w-=min(w,10);
		p+=160*w;
		cout<<4280-p<<endl;
	}
	return 0;
}