import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		char[] s=sc.next().toCharArray();

		int k=s.length;
		for(int i=1;i<s.length;i++){
			if(s[i]!=s[i-1]) k=Math.min(k, Math.max(i,s.length-i));
		}
				
		System.out.println(k);
	}
}
