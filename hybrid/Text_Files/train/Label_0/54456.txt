import java.util.Scanner;
public class Solution {

	public static void main(String[] sachin32) {
		
		Scanner in = new Scanner(System.in);
		
		int a = in.nextInt();
		int b = in.nextInt();
		int c = in.nextInt();
		int d = in.nextInt();
		
		
		if(a!=d || (a==0&&c!=0)) System.out.println(0);
		else System.out.println(1);
	}

}

