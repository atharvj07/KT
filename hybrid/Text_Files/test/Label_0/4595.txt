#include<iostream>
#include<stdio.h>
#include <algorithm>
#include<string.h>
#include <utility>
using namespace std;
int main(){
int m;
string in1,in2;
int a[1000],b[1000],ans[1000];
int f;
int alen,blen,mlen;
cin>>m;
while(m--){
for(int i=0;i<90;i++){
a[i]=b[i]=ans[i]=0;
}
in1="";
in2="";
cin>>in1;
cin>>in2;
alen=in1.size();
blen=in2.size();
mlen=max(alen,blen);
if(mlen>80){
cout<<"overflow"<<endl;
continue;
}
for(int i=0;i<alen;i++){
a[alen-1-i]=in1[i]-'0';
}
for(int i=0;i<blen;i++){
b[blen-1-i]=in2[i]-'0';
}
f=0;
for(int i=0;i<mlen+1;i++){
ans[i]=(a[i]+b[i]+f)%10;
f=(a[i]+b[i]+f)/10;
}
if(ans[mlen]!=0){
if(mlen>79){
cout<<"overflow"<<endl;
continue;
}
cout<<ans[mlen];
}
for(int i=0;i<mlen;i++){
cout<<ans[mlen-1-i];
}cout<<endl;
}
return 0;
}