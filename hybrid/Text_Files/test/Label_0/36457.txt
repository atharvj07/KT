import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner scn = new Scanner(System.in);
		int H = scn.nextInt();
		int W = scn.nextInt();
		H -= scn.nextInt();
		W -= scn.nextInt();
		System.out.println(H*W);
		scn.close();
	}
}