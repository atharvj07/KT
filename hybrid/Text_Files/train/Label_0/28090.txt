#include<bits/stdc++.h>
using namespace std;
int main()
{
int n;
cin>>n;
int k=n%10;
if(k==2 ||k==4 ||k==5||k==7||k==9)
cout<<"hon";
else if(k==3)
cout<<"bon";
else
cout<<"pon";
return 0;
}