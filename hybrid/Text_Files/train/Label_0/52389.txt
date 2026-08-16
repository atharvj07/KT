import java.util.*;
import java.io.*;
import java.lang.*;

public class cfrcs {

	static int gcd(int a, int b) {
		if (b == 0)
			return a;
		return gcd(b, a % b);
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t=Integer.parseInt(br.readLine());
		while(t-->0) {
			String s[]=br.readLine().split(" ");
			int n=Integer.parseInt(s[0]);
			int x=Integer.parseInt(s[1]);
			String ss[]=br.readLine().split(" ");
			int arr[]=new int[n];
			for(int i=0;i<n;i++) {
				arr[i]=Integer.parseInt(ss[i]);
			}
			
			Arrays.sort(arr);
			int v=0;
			int a=arr[0]-1;
			v=Math.min(x,a);
			x=x-v;
			if(v+1==arr[0])v=v+1;
		int f=0;
			for(int i=1;i<n;i++) {
				if(arr[i-1]==arr[i])continue;
				int d=arr[i]-arr[i-1]-1;
			 v=v+Math.min(d, x);
			 x=x-d;
			 if(v+1==arr[i])v=v+1;
			 else {
				 f=1;
				 break;
			 }
				
			}
			if(f==0) {
				v=v+x;
			}
			System.out.println(v);
			
		}
		
}
}