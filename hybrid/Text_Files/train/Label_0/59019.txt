import java.util.Scanner;

public class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		String s = sc.next();
		
		Main redOrBlue = new Main();
		System.out.println(redOrBlue.judgeRedOrBlue(N, s));
	}
	
	private String judgeRedOrBlue(int n, String s) {
		if(n < 1 || n > 100 || s == null || s.length() != n) return "No";
		
		char r = 'R', b = 'B';
		int countR = 0, countB = 0;
		for(char c : s.toCharArray()){
			if(c == r) countR++;
			if(c == b) countB++;
		}
		
		if(countR > countB) return "Yes";
		else return "No";
	}
}
