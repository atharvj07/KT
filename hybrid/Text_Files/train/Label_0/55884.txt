import java.util.*;
import java.lang.*;
import java.math.*;
import java.io.*;

import static java.lang.Math.*;
import static java.util.Arrays.*;

// Everything Starts With Your Vote
// 2012/12/04
public class Main{
	Scanner sc=new Scanner(System.in);

	int n, m, k, p;
	R[] rs, fs;
	boolean[] isfav;

	void run(){
		for(;;){
			n=sc.nextInt();
			m=sc.nextInt();
			k=sc.nextInt();
			p=sc.nextInt();
			if((n|m|k|p)==0){
				return;
			}

			rs=new R[n];
			HashMap<String, Integer> map=new HashMap<String, Integer>();
			for(int i=0; i<n; i++){
				String name=sc.next();
				int x=sc.nextInt();
				rs[i]=new R(name, x);
			}
			sort(rs);
			for(int i=0; i<n; i++){
				map.put(rs[i].name, i);
			}

			fs=new R[m];
			isfav=new boolean[n];
			for(int i=0; i<m; i++){
				String fav=sc.next();
				int j=map.get(fav);
				fs[i]=rs[map.get(fav)];
				isfav[j]=true;
			}
			sort(fs);

			int left=0, right=m;
			for(int t=0; t<100; t++){
				int mid=(left+right)/2;
				if(ok(mid)){
					left=mid;
				}else{
					right=mid;
				}
			}

			if(left+1<=m&&ok(left+1)){
				println((left+1)+"");
			}else{
				println(left+"");
			}
		}
	}

	boolean ok(int c){
		if(k-c<0){
			return false;
		}
		int index=-1;
		int count=0;
		for(int i=0; i<n; i++){
			if(!isfav[i]){
				if(++count==k-c+1){
					index=i;
					break;
				}
			}
		}
		if(index==-1){
			return true;
		}

		int q=p;
		for(int i=0; i<c; i++){
			if(fs[i].name.compareTo(rs[index].name)<0){
				q-=max(rs[index].x-fs[i].x, 0);
			}else{
				q-=max(rs[index].x+1-fs[i].x, 0);
			}
			if(q<0){
				return false;
			}
		}
		return true;
	}

	class R implements Comparable<R>{
		String name;
		int x;

		R(String name, int x){
			this.name=name;
			this.x=x;
		}

		@Override
		public int compareTo(R r){
			if(r.x!=x){
				return r.x-x;
			}else{
				return name.compareTo(r.name);
			}
		}

		@Override
		public String toString(){
			return name+":"+x;
		}
	}

	void println(String s){
		System.out.println(s);
	}

	public static void main(String[] args){
		new Main().run();
	}
}