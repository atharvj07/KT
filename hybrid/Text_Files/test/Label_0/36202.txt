import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		char[] s = sc.next().toCharArray();
		boolean lastWrong = false;
		int ans = n;
		for(int i=0;i<n;i++) {
			if (s[i] == 'o') {
				lastWrong = false;
			}else{
				if (lastWrong) {
					ans = i;
					break;
				}
				lastWrong = true;
			}
		}
		System.out.println(ans);
	}

}

