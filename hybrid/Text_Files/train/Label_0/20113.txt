#include<bits/stdc++.h>
#define SIZE 130
using namespace std;


int main(){
  int n,q;
  string s;

  int index=0;  
  int num_span[SIZE],length[SIZE],ok_LOC[SIZE];
  int***table;
  
  cin>>n>>q;
  
  //約数を求める
  for(int i=2;i<=n/2;i++){
    if(n%i==0){
      num_span[index]=i;//区間の数
      length[index++]=n/i;//各区間の長さ
    }
  }
  num_span[index]=n;
  length[index++]=1;

  
  table = new int**[index];
    for(int i=0;i<index;i++){
      table[i]=new int*[length[i]];
      for(int k=0;k<length[i];k++){
	table[i][k]=new int[26];
	for(int a=0;a<26;a++){
	  table[i][k][a]=0;
	}
      }
    }

  for(int i=0;i<index;i++){
    ok_LOC[i]=0;
  }
  
  cin>>s;
  for(int i=0;i<n;i++){
    for(int k=0;k<index;k++){
      table[k][i%length[k]][s[i]-'a']++;
      if(table[k][i%length[k]][s[i]-'a'] == num_span[k]){
	ok_LOC[k]++;
      }
    }
  }

  
  char pre;
  int p;
  char c;
  
  for(int loop=0;loop<q;loop++){
    cin>>p>>c;
    p--;
    
    pre=s[p];
    s[p]=c;
    int minimum=n; 

    for(int i=0;i<index;i++){
      if(table[i][p%length[i]][pre-'a'] == num_span[i]){
	ok_LOC[i]--;
      }
      
      table[i][p%length[i]][pre-'a']--;
      table[i][p%length[i]][c-'a']++;
      
      if(table[i][p%length[i]][c-'a'] == num_span[i]){
	ok_LOC[i]++;
      }
      
      if(ok_LOC[i] == length[i]){
	minimum=min(minimum,length[i]);
      }
    }
    cout<<minimum<<"\n";    
  }

  return 0;
}

