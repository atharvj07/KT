import java.util.Scanner;

/**
 * https://beta.atcoder.jp/contests/abc077/tasks/abc077_a
 */
public class Main {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		char[][] c = new char[2][3];
		for(int i=0; i<2; i++){
			c[i] = sc.next().toCharArray();
		}
		sc.close();
		
		String ans = "YES";
		if(c[0][0]!=c[1][2] || c[0][1]!=c[1][1] || c[0][2]!=c[1][0]){
			ans = "NO";
		}
		System.out.println(ans);

	}

}