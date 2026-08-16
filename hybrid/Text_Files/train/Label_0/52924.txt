import java.util.*;
import java.lang.*;
import java.math.*;
import java.io.*;

import static java.lang.Math.*;
import static java.util.Arrays.*;

public class Main{

	Scanner sc;

	static final int INF=1<<28;
	static final double EPS=1e-9;

	void run(){
		sc=new Scanner(System.in);
		for(;;){
			int n=sc.nextInt();
			if(n==0)
				break;
			int[] s=new int[n];
			int[] c=new int[n];
			for(int i=0; i<n; i++)
				s[i]=sc.nextInt();
			for(int op=0;; op++){
				for(int j=0; j<n; j++){
					int cnt=0;
					for(int i=0; i<n; i++)
						if(s[i]==s[j])
							cnt++;
					c[j]=cnt;
				}
				boolean f=true;
				for(int i=0; i<n; i++)
					if(s[i]!=c[i])
						f=false;
				if(f){
					println(op+"");
					for(int i=0; i<n; i++)
						print(s[i]+(i==n-1?"":" "));
					println("");
					break;
				}
				System.arraycopy(c, 0, s, 0, n);
			}
		}
		sc.close();
	}

	void print(String s){
		System.out.print(s);
	}

	void println(String s){
		System.out.println(s);
	}

	public static void main(String[] args){
		new Main().run();
	}
}