import java.io.*;
import java.util.*;
public class Solution {
	static Scanner sc=new Scanner(System.in);
	static PrintWriter out=new PrintWriter(System.out);
	//Main
	public static void main(String args[]) {
		int test=1;
		//test=sc.nextInt();
		while(test-->0) {
			//Focus
			int n=sc.nextInt(),m=sc.nextInt(),ans[]=new int[n],l=0,r=100000+5;
			Arrays.fill(ans, -1);
			for(int i=0;i<m;i++) {
				int x=sc.nextInt()-1,y=sc.nextInt()-1;
				if(y-x<r-l) {
					l=x;
					r=y;
				}
			}
			for(int i=l;i<=r;i++) ans[i]=i-l;
			for(int i=r+1;i<n;i++) ans[i]=ans[i-(r-l+1)];
			for(int i=l-1;i>=0;i--) ans[i]=ans[i+(r-l+1)];
			out.println(r-l+1);
			for(int x: ans) out.print(x+" ");
			
		}
		out.flush();
		out.close();
	}
}
