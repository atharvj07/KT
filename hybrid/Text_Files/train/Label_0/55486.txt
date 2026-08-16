import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String s = sc.next();
		int sLength = s.length();
		int count = 0;
		
		for(int i = 0; i < sLength; i++) {			
			//偶数番目の時'0'と一致
			boolean check1 = i % 2 == 0 && s.charAt(i) == '0';
			//奇数番目の時'1'と一致
			boolean check2 = i % 2 == 1 && s.charAt(i) == '1';

			// 0101...と一致する個数（1010...と一致しない個数）をカウント
			if(check1 || check2) {
				count++;
			}			
		}
		
		System.out.print(Math.min(count, sLength - count));
	}	
}