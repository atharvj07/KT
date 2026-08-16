import java.util.*;
import java.lang.*;
import java.math.*;
import java.io.*;
import static java.lang.Math.*;
import static java.util.Arrays.*;
import static java.util.Collections.*;

// B2D
// 2013/09/19
public class Main{
	Scanner sc=new Scanner(System.in);

	int n;
	String s;

	void run(){
		n=sc.nextInt();
		s=sc.next();
		solve();
	}

	void solve(){
		int N=(1<<n)+2, l0=N-2, l1=N-1;
		int[] ch0=new int[N], ch1=new int[N];
		for(int i=0; i<N; i++){
			ch0[i]=i*2;
			ch1[i]=i*2+1;
		}
		for(int i=0; i<1<<(n-1); i++){
			int os=1<<(n-1);
			ch0[os+i]=s.charAt(i*2)=='0'?l0:l1;
			ch1[os+i]=s.charAt(i*2+1)=='0'?l0:l1;
		}
		make(N);
		int node=(1<<n)-1;
		for(int b=n-1; b>=0; b--){
			int s=1<<b, t=s*2;
			for(int i=s; i<t; i++){
				for(int j=s; j<t; j++){
					if(find(ch0[i])==find(ch0[j])&&find(ch1[i])==find(ch1[j])){
						if(union(i, j)){
							node--;
						}
					}
				}
			}
		}
		for(int i=1; i<1<<n; i++){
			if(find(i)==i&&find(ch0[i])==find(ch1[i])){
				node--;
			}
		}
		println(node+"");
	}

	int[] p;

	void make(int n){
		p=new int[n];
		fill(p, -1);
	}

	int find(int x){
		return p[x]<0?x:(p[x]=find(p[x]));
	}

	boolean union(int x, int y){
		x=find(x);
		y=find(y);
		if(x!=y){
			p[x]=y;
		}
		return x!=y;
	}

	void println(String s){
		System.out.println(s);
	}

	public static void main(String[] args){
		new Main().run();
	}
}