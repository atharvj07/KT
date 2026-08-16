#include<iostream>
using namespace std;
long gcd(long a,long b){return b?gcd(b,a%b):a;}
int H,h,m,s;
bool check(long H,long h,long m,long s)
{
    for(int r=-1;r<=1;r++)
    {
        long A=r*360*10*H+60*m*(H+1)+3600*h;
        long B=119*H-1;
        long d=gcd(A,B);
        A/=d;
        B/=d;
        if(!(A>=60*B||s*B>A)&&!(h==0&&m==0&&A==0))
        {
            cout<<h<<" "<<m<<" "<<A<<" "<<B<<endl;
            return true;
        }
    }
    return false;
}
int main()
{
    while(cin>>H>>h>>m>>s,H)
    {
        while(!check(H,h,m,s))
        {
            s++;
            if(s==60)m++,s=0;
            if(m==60)h++,m=0;
            if(h==H)h=0;
        }
    }
}
