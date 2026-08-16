#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
ll gcd(ll a, ll b) {return b?gcd(b,a%b):a;}
ll lcm(ll a, ll b) {return a/gcd(a,b)*b;}
int main(){
ll a,b,c,d;
cin >>a>>b>>c>>d;
ll cc=b/c-(a-1)/c;
ll dd=b/d-(a-1)/d;
ll k=lcm(c,d);
ll cd=b/k-(a-1)/k;
cout <<b-a+1-cc-dd+cd<<endl;
}
