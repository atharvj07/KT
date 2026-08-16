#include<bits/stdc++.h>
int a,s,n;
std::bitset<1<<22>d;     
int main(){
    std::cin>>n;d[0]=1;
    while(n--)std::cin>>a,s+=a,d|=(d<<a);
	while(!d[++s/2]);std::cout<<s/2;
}