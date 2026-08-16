import java.util.*;

public class Main {
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		char[] arr = sc.next().toCharArray();
		int[] counts = new int[26];
		for (char c : arr) {
		    if (c != '+') {
		        counts[c - 'a']++;
		    }
		}
		Arrays.sort(counts);
		int prev = counts[25];
		int cnt = 1;
		int total = 0;
		if (prev == 1) {
		    prev = 0;
		    total += 2;
		}
		for (int i = 24; i >= 0 && counts[i] > 0; i--) {
		    if (prev == counts[i]) {
		        cnt++;
		    } else {
		        if (prev == 0) {
		            total += 2;
		        } else {
		            if (cnt >= 2) {
		                total += 4 + cnt * 2;
		            } else {
		                total += 4;
		            }
		            cnt = 1;
		            if (counts[i] == 1) {
		                prev = 0;
		                total += 2;
		            } else {
		                prev = counts[i];
		            }
		        }
		    }
		}
		if (prev != 0) {
            if (cnt >= 2) {
                total += 4 + cnt * 2;
            } else {
                total += 4;
            }
		}
		System.out.println(total - 1);
	}
}

