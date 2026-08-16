import java.util.*;
public class Main {
	static Scanner sc = new Scanner(System.in);

	//0502
	static class Dice {
		int[] ndice= {1,5,2,3,0,4}, edice= {3,1,0,5,4,2};
		int[] wdice= {2,1,5,0,4,3}, sdice= {4,0,2,3,5,1};
		int[] rdice= {0,2,4,1,3,5}, ldice= {0,3,1,4,2,5};
		int sum;
		void topSum() {
			for(;;) {
				int n = Integer.parseInt(sc.nextLine());
				if(n==0) break;
				int[] dice = {1,2,3,4,5,6};
				sum = 1; //dice[0]
				for(int i=0; i<n; i++) {
					dice = turn(sc.nextLine(), dice);
					sum += dice[0];
				}
				System.out.println(sum);
			}
		}

		int[] turn(String comd, int[] dice) {
			int[] nd = new int[6];
			if(comd.equals("North")) {
				for(int i=0; i<6; i++) {
					nd[i] = dice[ndice[i]];
				}
			}else if(comd.equals("East")) {
				for(int i=0; i<6; i++) {
					nd[i] = dice[edice[i]];
				}
			}else if(comd.equals("West")) {
				for(int i=0; i<6; i++) {
					nd[i] = dice[wdice[i]];
				}
			}else if(comd.equals("South")) {
				for(int i=0; i<6; i++) {
					nd[i] = dice[sdice[i]];
				}
			}else if(comd.equals("Right")) {
				for(int i=0; i<6; i++) {
					nd[i] = dice[rdice[i]];
				}
			}else if(comd.equals("Left")) {
				for(int i=0; i<6; i++) {
					nd[i] = dice[ldice[i]];
				}
			}
			return nd;
		}
	}

	public static void main(String[] args) {
		//0502
		Dice d = new Dice();
		d.topSum();
	}
}