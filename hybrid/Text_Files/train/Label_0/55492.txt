import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Scanner;

public class Main {
	
	public static final String[] hands = 
		{"Rock",
		 "Fire",
		 "Scissors",
		 "Snake",
		 "Human",
		 "Tree",
		 "Wolf",
		 "Sponge",
		 "Paper",
		 "Air",
		 "Water",
		 "Dragon",
		 "Devil",
		 "Lightning",
		 "Gun"
		};
	
	public static final int SIZE = 15;
			
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		HashMap<String, Integer> dict = new HashMap<String, Integer>();
		
		for(int i = 0; i < hands.length; i++){
			dict.put(hands[i], i);
		}
		
		boolean[][] win = new boolean[SIZE][SIZE];
		for(int i = 0; i < SIZE; i++){
			for(int j = 1; j <= 7; j++){
				win[i][(i + j) % SIZE] = true;
			}
		}
		
		HashSet<Integer> set = new HashSet<Integer>();
		
		while(true){
			final int N = sc.nextInt();
			
			if(N == 0){
				break;
			}
			
			set.clear();
			
			for(int i = 0; i < N; i++){
				set.add(dict.get(sc.next()));
			}
			
			boolean def = false;
			for(int hand : set){
				boolean flag = false;
				
				for(int other_hand : set){
					if(hand == other_hand){
						continue;
					}else if(win[hand][other_hand]){
						flag = true;
					}else if(!win[hand][other_hand]){
						flag = false;
						break;
					}
				}
				
				if(flag){
					System.out.println(hands[hand]);
					def = true;
					break;
				}
			}
			
			if(!def){
				System.out.println("Draw");
			}
		}
	}

}