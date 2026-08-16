import java.util.Scanner;

public class Main {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		String S = sc.next();

		String leftS = S.substring(0, (S.length()-1)/2);
		String rightS = S.substring(((S.length() + 3)/2) - 1);

		StringBuffer sb = new StringBuffer(leftS);
		String reverseLeftS = sb.reverse().toString();
		sb = new StringBuffer(rightS);
		String reverseRightS = sb.reverse().toString();
		sb = new StringBuffer(S);
		String reverseS = sb.reverse().toString();
		if (leftS.equals(reverseLeftS) && rightS.equals(reverseRightS) && S.equals(reverseS)){
			System.out.println("Yes");
		} else {
			System.out.println("No");
		}

	}
}