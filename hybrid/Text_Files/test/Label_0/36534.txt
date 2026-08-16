import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main{
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int N = scan.nextInt();
		int K = scan.nextInt();
		int[]a = new int[N];
		Map<Integer, Integer> map = new HashMap<Integer, Integer>();
		for(int i = 0; i < N; i++) {
			a[i] = scan.nextInt();
		}
		scan.close();
		int min = Integer.MAX_VALUE;
		int right = 0;
		for(int left = 0; left < N; left++) {
			while(right < N && map.size() < K) {
				if(a[right] <= K) {
					map.merge(a[right], 1, (val1, val2) -> val1 + val2);
				}
				right++;
			}
			if(map.size() == K) {
				int l = right - left;
				min = Math.min(min, l);
			}
			if(right == left) {
				right ++;
			}else {
				if(a[left] <= K) {
					if(map.get(a[left]) == 1) {
						map.remove(a[left]);
					}else {
						map.merge(a[left], -1, (val1, val2) -> val1 + val2);
					}
				}
			}
		}
		if(min == Integer.MAX_VALUE) {
			System.out.println(0);
		}else {
			System.out.println(min);
		}
	}
}
