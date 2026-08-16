#include<cstdio>
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
int main(){
    int num,flag=0;
    double tall,weight;
    while(scanf("%d,%lf,%lf",&num,&weight,&tall)!=EOF){
        if(weight/(tall*tall)>=25){cout<<num<<endl;flag=1;}
    }
    if(flag==0)cout<<"該当なし"<<endl;
    return 0;
}