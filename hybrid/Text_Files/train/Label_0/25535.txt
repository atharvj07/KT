#include<bits/stdc++.h>
using namespace std;
int main()
{
    string a;
    cin>>a;
    if(int(a.find('C'))!=-1 and int(a.rfind('F'))!=-1&&a.find('C')<a.rfind('F'))//个人码风问题，习惯用and而不是&&
        cout<<"Yes";
    else
        cout<<"No";
}