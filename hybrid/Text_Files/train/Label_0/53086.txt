import java.util.*;
import java.lang.*;
import java.math.*;
import java.io.*;
import static java.lang.Math.*;
import static java.util.Arrays.*;
import static java.util.Collections.*;

public class Main{

	Scanner sc=new Scanner(System.in);

	int T;
	final int m=3, n=9;
	String[] ss;

	void run(){
		T=sc.nextInt();
		for(int k=0; k<T; k++){
			ss=new String[n];
			for(int i=0; i<n; i++){
				ss[i]=sc.next();
			}
			solve();
		}
	}

	int[] is, rot;
	boolean[] used;
	int answer;

	void solve(){
		is=new int[n];
		rot=new int[n];
		used=new boolean[n];
		answer=0;
		dfs(0);
		println(answer+"");
	}

	void dfs(int index){
		if(index==n){
			answer++;
			return;
		}
		for(int j=0; j<n; j++){
			if(used[j]){
				continue;
			}
			is[index]=j;
			used[j]=true;
			for(int i=0; i<4; i++){
				rot[index]=i;
				if(check(index)){
					dfs(index+1);
				}
			}
			used[j]=false;
		}
	}

	boolean check(int index){
		int x=index%m;
		int y=index/m;
		if(x>0){
			int index2=y*m+(x-1);
			char c1=ss[is[index]].charAt((3+rot[index])%4);
			char c2=ss[is[index2]].charAt((1+rot[index2])%4);
			if(Character.toLowerCase(c1)==Character.toLowerCase(c2)&&c1!=c2){}else{
				return false;
			}
		}
		if(y>0){
			int index2=(y-1)*m+x;
			char c1=ss[is[index]].charAt((0+rot[index])%4);
			char c2=ss[is[index2]].charAt((2+rot[index2])%4);
			if(Character.toLowerCase(c1)==Character.toLowerCase(c2)&&c1!=c2){}else{
				return false;
			}
		}
		return true;
	}

	void debug(Object... os){
		System.err.println(deepToString(os));
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