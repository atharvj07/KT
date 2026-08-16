import java.io.*;
import java.util.*;

public class ProblemE {
	
	public static int[][][] dp = new int[65536][2][257];
	public static int n = -1;
	public static ArrayList<Card> modCards = new ArrayList<Card>();
	public static int goal = -1;

	public static void main(String[] args) throws Exception {
		for(int i=0; i<65536; i++) {
			for(int j=0; j<257; j++) {
				dp[i][0][j] = -1;
				dp[i][1][j] = -1;
			}
		}
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		goal = (1 << n) - 1;
		
		String[][] cards = new String[n][3];
		for(int i=0; i<n; i++) {
			cards[i] = br.readLine().split(" ");
		}
		
		int minRedCost = 0;
		int minBlueCost = 0;
		
		for(int i=0; i<n; i++) {
			boolean isRed;
			int redCost;
			int blueCost;
			if(cards[i][0].equals("R"))
				isRed = true;
			else
				isRed = false;
			redCost = Integer.parseInt(cards[i][1]);
			blueCost = Integer.parseInt(cards[i][2]);
			
			if(redCost > n) {
				minRedCost += (redCost - n);
				redCost = n;
			}
			if(blueCost > n) {
				minBlueCost += (blueCost - n);
				blueCost = n;
			}
			
			modCards.add(new Card(isRed, redCost, blueCost));
		}
		
		long minTurns;
		long sol;
		
		if(minRedCost > minBlueCost) {
			minTurns = minRedCost;
			int otherAmount = Math.min(minRedCost - minBlueCost, 256);
			sol = solve(0, 1, otherAmount);
		} else {
			minTurns = minBlueCost;
			int otherAmount = Math.min(minBlueCost - minRedCost, 256);
			sol = solve(0, 0, otherAmount);
		}
		
		System.out.println(minTurns + sol);
	}
	
	public static int solve(int mask, int redIsZero, int otherCount) {
		if(dp[mask][redIsZero][otherCount] != -1)
			return dp[mask][redIsZero][otherCount];
		
		if(mask == goal)
			return 0;
		
		int selector = 1;
		int redDiscount = 0;
		int blueDiscount = 0;
		for(int i=0; i<n; i++) {
			if((mask & selector) > 0) {
				if(modCards.get(i).isRed)
					redDiscount++;
				else
					blueDiscount++;
			}
			selector = selector << 1;
		}
		
		int min = 1000000007;
		selector = 1;
		for(int i=0; i<n; i++) {
			if((mask & selector) == 0) {
				int cand;
				int redPrice = Math.max(modCards.get(i).redCost - redDiscount, 0);
				int bluePrice = Math.max(modCards.get(i).blueCost - blueDiscount, 0);
				int turns = 1;
				int curRed;
				int curBlue;
				if(redIsZero == 1) {
					curRed = 0;
					curBlue = otherCount;
				} else {
					curRed = otherCount;
					curBlue = 0;
				}
				
				if(redPrice - curRed > bluePrice - curBlue) {
					turns += redPrice - curRed;
					int remBlue = Math.min(curBlue + redPrice - curRed - bluePrice, 256);
					cand = turns + solve(mask | selector, 1, remBlue);
				} else {
					turns += bluePrice - curBlue;
					int remRed = Math.min(curRed + bluePrice - curBlue - redPrice, 256);
					cand = turns + solve(mask | selector, 0, remRed);
				}
				if(cand < min)
					min = cand;	
			}		
			selector = selector << 1;
		}
		dp[mask][redIsZero][otherCount] = min;
		return dp[mask][redIsZero][otherCount];
	}

}

class Card {
	public boolean isRed;
	public int redCost;
	public int blueCost;
	public Card(boolean col, int red, int blue) {
		isRed = col;
		redCost = red;
		blueCost = blue;
	}
}