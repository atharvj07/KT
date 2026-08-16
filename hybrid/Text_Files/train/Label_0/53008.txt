import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main {
	
	private static int[] input = new int[130000];
	
	private static boolean check(int value , Map<Integer , Integer> map) {
		
		long current = 1;
		while (current <= (long) (1 << 30)) {
			if (current >= value) {
				int temp = (int) (current - value);
				if (map.containsKey(temp)) {
					if (temp == value) {
						if (map.get(value) >= 2) {
							return true;
						}
					} else {
						if (map.containsKey(temp)) {
							return true;
						}
					}
				}
			}
			current *= 2;
		}
		return false;
		
	}
	
	public static void main(String[] args) throws Exception {
		
		Scanner scan = new Scanner(System.in);

		Map<Integer , Integer> map = new HashMap<>();
		int i , n = scan.nextInt() , ans = 0;
		for (i = 0;i < n;i ++) {
			input[i] = scan.nextInt();
			if (!map.containsKey(input[i])) {
				map.put(input[i] , 1);
			} else {
				map.put(input[i] , map.get(input[i]) + 1);
			}			
		}
		for (i = 0;i < n;i ++) {
			int current = input[i];
			if (!check(current , map)) {
				ans ++;
			}
		}
		System.out.println(ans);
		
	}
	
    
}














