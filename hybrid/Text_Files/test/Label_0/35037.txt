import java.util.Scanner;

public class Main {
	//java11

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		String S = sc.next();
		String T = sc.next();

		StringBuilder sb = new StringBuilder(S);
		boolean matchAnswer = false;
		for(int i=S.length()-T.length(); i>=0; i--) {
			boolean isMatch = true;

			for(int j=i; j<i+T.length(); j++) {
				if(!(S.charAt(j) == T.charAt(j-i) || S.charAt(j) == '?')) {
					isMatch = false;
					break;
				}
			}

			if(isMatch) {
				sb.replace(i, i+T.length(), T);
				matchAnswer = true;
				break;
			}
		}

		String ans = "UNRESTORABLE";
		if(matchAnswer) {
			ans = sb.toString();
			ans = ans.replace("?", "a");
		}

		System.out.println(ans);
	}
}
