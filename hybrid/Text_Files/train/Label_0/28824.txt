#include <cassert>

#include <cctype>
#include <cerrno>
#include <cfloat>
#include <ciso646>
#include <climits>
#include <clocale>
#include <cmath>
#include <csetjmp>
#include <csignal>
#include <cstdarg>
#include <cstddef>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <ccomplex>
#include <cfenv>
#include <cinttypes>
#include <cstdbool>
#include <cstdint>
#include <ctgmath>
#include <cwchar>
#include <cwctype>

// C++
#include <algorithm>
#include <bitset>
#include <complex>
#include <deque>
#include <exception>
#include <fstream>
#include <functional>
#include <iomanip>
#include <ios>
#include <iosfwd>
#include <iostream>
#include <istream>
#include <iterator>
#include <limits>
#include <list>
#include <locale>
#include <map>
#include <memory>
#include <new>
#include <numeric>
#include <ostream>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <stdexcept>
#include <streambuf>
#include <string>
#include <typeinfo>
#include <utility>
#include <valarray>
#include <vector>
#include <array>
#include <atomic>
#include <chrono>
#include <condition_variable>
#include <forward_list>
#include <future>
#include <initializer_list>
#include <mutex>
#include <random>
#include <ratio>
#include <regex>
#include <scoped_allocator>
#include <system_error>
#include <thread>
#include <tuple>
#include <typeindex>
#include <type_traits>
#include <unordered_map>
#include <unordered_set>
//#include <boost/foreach.hpp>
//#include <boost/range/algorithm.hpp>
#define rep(i,j,k) for(int i=(int)j;i<(int)k;i++)
#define ll long long
#define Sort(v) sort(all(v))
#define INF 1000000000
#define END return 0
#define pb push_back
#define se second
#define fi first
#define pb push_back
#define all(v) (v).begin() , (v).end()
#define MP make_pair
#define MOD 1000000007LL
using namespace std;
int day[12]={31,28,31,30,31,30,31,31,30,31,30,31};

bool All(string s){
    rep(i,0,s.size())if(s[i]=='0')return 0;
    return 1;
}

bool any(string s){
    rep(i,0,s.size())if(s[i]=='1')return 1;
    return 0;
}

bool none(string s){
    rep(i,0,s.size())if(s[i]=='1')return 0;
    return 1;
}

int Count(string s){
    int ret=0;
    rep(i,0,s.size())if(s[i]=='1')ret++;
    return ret;
}

unsigned long long val(string s){
    //reverse(all(s));
    unsigned long long ret=0;
    rep(i,0,s.size()-1){
        unsigned long long n=1;
        for(ll j=0;j<i;j++)n*=(unsigned long long)(2);
        if(s[i]=='1')ret+=n;
    }
    return ret;
}

int main (){
    string s(64,'0');
    int q;cin>>q;
    rep(i,0,q){
        int cmd;cin>>cmd;
        if(cmd==0){
            int i;cin>>i;
            cout<<s[i]<<endl;
        }else if(cmd==1){
            int i;cin>>i;
            s[i]='1';
        }else if(cmd==2){
            int i;cin>>i;
            s[i]='0';
        }else if(cmd==3){
            int i;cin>>i;
            s[i]=(s[i]=='0')?'1':'0';
        }else if(cmd==4){
            cout<<All(s)<<endl;
        }else if(cmd==5){
            cout<<any(s)<<endl;
        }else if(cmd==6){
            cout<<none(s)<<endl;
        }else if(cmd==7){
            cout<<Count(s)<<endl;
        }else {
            string ss=s;
            reverse(all(ss));
            bitset<64> gotutiyan(ss);
            cout<<gotutiyan.to_ullong()<<endl;
        }
        // cout<<cmd<<endl;
        // cout<<s<<endl;
    }
    
}


/*
14
1 0
1 1
1 2
2 1
0 0
0 1
0 2
0 3
3 3
4
5
6
7
8
*/

