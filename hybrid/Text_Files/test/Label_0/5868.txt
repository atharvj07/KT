#include<bits/stdc++.h>
using namespace std;
int main()
{
    char str;
    while(scanf("%c",&str)!=EOF){
        if(islower(str)!=0)str=toupper(str);
        cout<<str;
    }
}