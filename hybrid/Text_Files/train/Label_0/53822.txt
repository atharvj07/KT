import java.util.*;
public class Solution{
	public static void main(String[] args) {
		Scanner	sc = new Scanner(System.in);
		int t = sc.nextInt();
		while(t-->0){
			String b = sc.next();
			String s = "";
			int n = b.length();
			s = s + b.charAt(0);
			for(int i=1;i<n-1;i+=2)
				s = s + b.charAt(i);
			s = s + b.charAt(n-1);
			System.out.println(s);
		}
	}
}