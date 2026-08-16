
import java.util.*;
import java.math.*;
import static java.lang.Character.isDigit;
import static java.lang.Character.isLowerCase;
import static java.lang.Character.isUpperCase;
import static java.lang.Math.*;
import static java.math.BigInteger.*;
import static java.util.Arrays.*;
import static java.util.Collections.*;

public class Main{
	static void debug(Object...os){
		System.err.println(deepToString(os));
	}
	
	static final int M = 51123987;
	void run(){
		int n=nextInt();
		String s=next();
		int res=solve(s);
		System.out.println(res);
	}
	
	private int solve(String s){
		int n=s.length();
		int[] is=new int[n];
		for(int i=0;i<n;i++)is[i]=s.charAt(i)-'a';
		int[][][][] dp = new int[2][n][52][52];
		dp[0][0][0][0]=1;
		int[][] nxt=new int[n][3];
		for(int i=0;i<n;i++)for(int j=0;j<3;j++) {
			int i2=i;
			while(i2<n && is[i2]!=j)i2++;
			nxt[i][j]=i2;
		}
		for(int i=0;i<n;i++) {
			int i1=i%2,i2=(i+1)%2;
			for(int j=0;j<n;j++)for(int a=0;a<52;a++)fill(dp[i2][j][a],0);
			for(int j=0;j<n;j++)for(int a=0;a<52;a++)for(int b=0;b<52;b++)if(dp[i1][j][a][b]>0){
				for(int k=0;k<3;k++)if(nxt[j][k]<n) {
					int na = k==0 ? a+1 : a;
					int nb = k==1 ? b+1 : b;
					if(na>=52 || nb >= 52)continue;
					dp[i2][nxt[j][k]][na][nb] += dp[i1][j][a][b];
					if(dp[i2][nxt[j][k]][na][nb]>=M)dp[i2][nxt[j][k]][na][nb] -= M;
				}
			}
		}
		int res = 0;
		for(int j=0;j<n;j++)for(int a=0;a<52;a++)for(int b=0;b<52;b++) {
			int c=n-a-b;
			if(abs(a-b)<=1 && abs(b-c)<=1 && abs(c-a)<=1) {
				res += dp[n&1][j][a][b];
				if(res>=M)res-=M;
			}
		}
		return res;
	}

	int nextInt(){
		try{
			int c=System.in.read();
			if(c==-1) return c;
			while(c!='-'&&(c<'0'||'9'<c)){
				c=System.in.read();
				if(c==-1) return c;
			}
			if(c=='-') return -nextInt();
			int res=0;
			do{
				res*=10;
				res+=c-'0';
				c=System.in.read();
			}while('0'<=c&&c<='9');
			return res;
		}catch(Exception e){
			return -1;
		}
	}
	
	long nextLong(){
		try{
			int c=System.in.read();
			if(c==-1) return -1;
			while(c!='-'&&(c<'0'||'9'<c)){
				c=System.in.read();
				if(c==-1) return -1;
			}
			if(c=='-') return -nextLong();
			long res=0;
			do{
				res*=10;
				res+=c-'0';
				c=System.in.read();
			}while('0'<=c&&c<='9');
			return res;
		}catch(Exception e){
			return -1;
		}
	}
	
	double nextDouble(){
		return Double.parseDouble(next());
	}
	
	String next(){
		try{
			StringBuilder res=new StringBuilder("");
			int c=System.in.read();
			while(Character.isWhitespace(c))
				c=System.in.read();
			do{
				res.append((char)c);
			}while(!Character.isWhitespace(c=System.in.read()));
			return res.toString();
		}catch(Exception e){
			return null;
		}
	}
	
	String nextLine(){
		try{
			StringBuilder res=new StringBuilder("");
			int c=System.in.read();
			while(c=='\r'||c=='\n')
				c=System.in.read();
			do{
				res.append((char)c);
				c=System.in.read();
			}while(c!='\r'&&c!='\n');
			return res.toString();
		}catch(Exception e){
			return null;
		}
	}
	public static void main(String[] args){
		new Main().run();
	}
}
