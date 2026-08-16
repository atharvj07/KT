import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		// 「ABC → BCA」の置換はAとBCの交換とみなせるはず
		Scanner in = new Scanner(System.in);
		String base = in.next();
		base = base.replace("BC", "X");

		int cntA = 0;
		long answer = 0;
		
		char[] targ = base.toCharArray();
		for ( int i = 0; i < targ.length; i++ ) {
			if ( targ[i] == 'A' ) cntA++;
			else if ( targ[i] == 'X' ) answer += cntA;
			else cntA = 0;
		}

		System.out.println(answer);
		in.close();
	}
}