#include <bits/stdc++.h>
using namespace std;

int solve(int A,int B,int C){
	if(A&1 || B&1 || C&1)return 0;
	if(A==B && B==C)return -1;
	return 1+solve((B+C)/2,(A+C)/2,(A+B)/2);
}

int main(void){
	int A,B,C;
	cin>>A>>B>>C;
	cout<<solve(A,B,C)<<endl;
	return 0;
}
