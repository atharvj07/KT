import java.util.*;

public class Main {
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		boolean[] arr = new boolean[n];
		for (int i = 0; i < m; i++) {
		    arr[sc.nextInt() - 1] = true;
		}
		int left = 0;
		int right = n - 1;
		int count = 0;
		while (left < right) {
		    while(left < n && arr[left]) {
		        left++;
		    }
		    while(right >= 0 && !arr[right]) {
		        right--;
		    }
		    if (left < right) {
		        count++;
		        left++;
		        right--;
		    }
		}
		System.out.println(count);
	}
}

