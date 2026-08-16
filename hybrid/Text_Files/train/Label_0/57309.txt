import java.util.*;

public class Main {
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int s = sc.nextInt();
		int[] arr = new int[n];
		for (int i = 0; i < n; i++) {
		    arr[i] = sc.nextInt();
		}
		int right = 0;
		int sum = arr[0];
		int min = Integer.MAX_VALUE;
		for(int left = 0; left < n; left++) {
		    while(right < n && sum < s) {
		        right++;
		        if (right >= n) {
		            break;
		        }
		        sum += arr[right];
		    }
		    if (right >= n) {
		        break;
		    }
		    min = Math.min(min, right - left + 1);
		    sum -= arr[left];
		}
		if (min == Integer.MAX_VALUE) {
		    System.out.println(0);
		} else {
		    System.out.println(min);
		}
	}
}

