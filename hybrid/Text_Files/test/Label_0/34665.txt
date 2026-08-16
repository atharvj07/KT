import java.util.*;
import java.lang.*;
import java.math.*;
import java.io.*;

import static java.lang.Math.*;
import static java.util.Arrays.*;
import static java.util.Collections.*;

// Substring
// 2012/09/19
public class Main{
	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));

	int n, m;
	String s;
	String[] queries;

	void run(){
		try{
			String[] ss=br.readLine().split(" ");
			n=Integer.parseInt(ss[0]);
			m=Integer.parseInt(ss[1]);
			s=br.readLine();
			queries=new String[m];
			for(int i=0; i<m; i++){
				queries[i]=br.readLine();
			}
			solve();
		}catch(IOException e){}
	}

	void solve(){
		RollingHash rh=new RollingHash(s);
		HashSet<Long> set=new HashSet<Long>();
		rh.addRight();
		for(int i=0; i<m; i++){
			if(queries[i].equals("L++")){
				rh.removeLeft();
			}else if(queries[i].equals("L--")){
				rh.addLeft();
			}else if(queries[i].equals("R++")){
				rh.addRight();
			}else if(queries[i].equals("R--")){
				rh.removeRight();
			}
			set.add(rh.hash);
		}
		println(set.size()+"");
	}

	class RollingHash{
		String s;
		int left, right; // [left, right)
		long hash, c=(int)1e9+7, ci;
		long[] cm;

		RollingHash(String s){
			this.s=s;
			ci=1;
			long x=c;
			// c^(-1)=c^(2^63-1)
			for(int i=0; i<63; i++){
				ci*=x;
				x*=x;
			}
			cm=new long[s.length()+1];
			cm[0]=1;
			for(int i=1; i<cm.length; i++)
				cm[i]=c*cm[i-1];
		}

		void init(int left, int right){
			this.left=left;
			this.right=right;
			hash=0;
			for(int i=left; i<right; i++)
				hash=hash*c+s.charAt(i);
		}

		void moveRight(){
			hash=c*hash+s.charAt(right)-cm[right-left]*s.charAt(left);
			left++;
			right++;
		}

		void moveLeft(){
			hash=(hash+cm[right-left]*s.charAt(left-1)-s.charAt(right-1))*ci;
			left--;
			right--;
		}

		void addRight(){
			hash=c*hash+s.charAt(right);
			right++;
		}

		void addLeft(){
			hash=hash+cm[right-left]*s.charAt(left-1);
			left--;
		}

		void removeRight(){
			hash=(hash-s.charAt(right-1))*ci;
			right--;
		}

		void removeLeft(){
			hash=hash-cm[right-left-1]*s.charAt(left);
			left++;
		}
	}

	void println(String s){
		System.out.println(s);
	}

	public static void main(String[] args){
		new Main().run();
	}
}