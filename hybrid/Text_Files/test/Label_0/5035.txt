#include<iostream>
using namespace std;
int main(){
long n,m,i,j,h[500000],j2,j3,j5,x2,x3,x5,f;
while(cin>>m){
if(m==0)break;
cin>>n;
j2=j3=j5=0;
x2=x3=x5=1;
f=0;
for(i=0;;i++){
h[i]=min(min(x2,x3),x5);
if(f==0&&h[i]>=m){j=i;f=1;}
if(h[i]>n)break;
while(x2<=h[i])x2=2*h[j2++];
while(x3<=h[i])x3=3*h[j3++];
while(x5<=h[i])x5=5*h[j5++];
}
cout<<i-j<<endl;
}
return 0;
}