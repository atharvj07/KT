#include <cstdio>
char S[1025];
char ch[10][6]={"",".,!? ","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};
int size[10]={1,5,3,3,3,3,3,4,3,4};
int main() {
	int n;
	scanf("%d",&n);
	for(int i=0;i<n;i++) {
		scanf("%s",S);
		int idx=0;
		while(S[idx]!='\0') {
			int nxt=idx;
			int len=0;
			while(S[nxt]==S[idx]) {
				nxt++;
				len++;
			}
			if(S[idx]>'0') {
				len--;
				len%=size[S[idx]-'0'];
				putchar(ch[S[idx]-'0'][len]);
			}
			idx=nxt;
		}
		putchar('\n');
	}
}