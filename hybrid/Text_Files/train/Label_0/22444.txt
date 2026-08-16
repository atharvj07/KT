#include<iostream>
using namespace std;
int n,s,x,y,z;
int main(){
    cin>>n;
    for(int i=0;i<n;i++){
        cin>>s;
        if(s%4==0)x++;
        else if(s%2==0)y++;
        else z++;
    }
    if(x>=z)cout<<"Yes"<<"\n";
    else if(z-x==1 and y==0)cout<<"Yes"<<"\n";
    else cout<<"No"<<"\n";     
}