import java.util.*;
import java.io.*;

public class Solution{

	public static Integer INT(String s) {
		return Integer.parseInt(s);
	}

	public static Long LONG(String s) {
		return Long.parseLong(s);
	}

	public static String STR(int arr[]) {
		return Arrays.toString(arr);
	}

	public static long GCD(long a, long b) {
		if(b==0)
			return a;
		return GCD(b, a%b);
	}

	static int mod=1_000_000_007, oo=Integer.MAX_VALUE, _oo=Integer.MAX_VALUE;

	//==================================================================================================================================================

	public static boolean valid(char c[], char t[]) {

		int freq[]=new int[26];
		
		for(char item: c)
			freq[item-'a']+=1;
		for(char item: t)
			freq[item-'a']-=1;

		for(int item: freq)
			if(item!=0)
				return false;
		return true;
	}

	public static void main(String args[]) throws IOException {
 
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));	Scanner in=new Scanner(System.in); StringBuilder out=new StringBuilder();
		
		int q=in.nextInt();

		while(q--!=0) {

			int n=in.nextInt();

			char s[]=in.next().toCharArray(),
				 t[]=in.next().toCharArray();

			if(!valid(s, t))
				System.out.println(-1);
			else
				System.out.println(solve(s, t, n));
		}
	}

	public static int solve(char s[], char t[], int n) {

		for(int len=n; len>=1; len--)
			for(int i=0; i+len-1<n; i++)
				if(check(s, t, i, i+len-1, n))
					return n-len;

		return n;
	}

	public static boolean check(char s[], char t[], int i, int j, int n) {

		for(int k=0; k<n && i<=j; k++)
			if(s[k]==t[i])
				i+=1;

		if(i>j)
			return true;
		return false;
	}
}