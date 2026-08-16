import java.util.*;
public class Main {
	static Scanner sc = new Scanner(System.in);

	//0500
	static class CardGame {
		void score() {
			for(;;) {
				int n = sc.nextInt();
				if(n==0) break;
				int scoreA=0, scoreB=0;
				for(int i=0; i<n; i++) {
					int ac = sc.nextInt(), bc = sc.nextInt();
					if(ac == bc) {
						scoreA += ac;
						scoreB += bc;
					}else if(ac > bc) {
						scoreA += ac+bc;
					}else {
						scoreB += ac+bc;
					}
				}
				System.out.println(scoreA + " " + scoreB);
			}
		}
	}

	public static void main(String[] args) {
		CardGame cg = new CardGame();
		cg.score();
	}
}