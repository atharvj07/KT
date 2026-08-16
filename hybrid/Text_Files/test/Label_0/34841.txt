import java.util.*;
import java.lang.*;
import java.math.*;
import java.io.*;
import static java.lang.Math.*;
import static java.util.Arrays.*;
import static java.util.Collections.*;

// Avant-garde Art
public class Main{
	Scanner sc=new Scanner(System.in);

	int INF=1<<28;

	int n, k;
	int[] a;

	void run(){
		n=sc.nextInt();
		k=sc.nextInt();
		a=new int[n];
		for(int i=0; i<n; i++){
			a[i]=sc.nextInt()-1;
		}
		solve();
	}

	void solve(){
		int clique=0;
		int[] last=new int[n];
		for(int i=0; i<n; i++){
			int s=min(i, a[i]), t=max(i, a[i]);
			int lis=0;
			fill(last, INF);
			for(int j=0; j<n; j++){
				if((s<j&&j<t)&&!(s<a[j]&&a[j]<t)){
					int v=(a[j]-s+n)%n;
					int k=binarySearch(last, v);
					if(k<0)
						k=-k-1;
					last[k]=v;
					lis=max(lis, k+1);
				}
			}
			clique=max(clique, lis+1);
		}
		int ans=clique+min(n/2-clique, k);
		println(ans+"");
	}

	void println(String s){
		System.out.println(s);
	}

	public static void main(String[] args){
		new Main().run();
	}
}