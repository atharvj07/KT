import java.util.*;
import java.io.*;
import java.math.*;

public class Main {

	private static int MAX = Integer.MAX_VALUE;
	private static int MIN = Integer.MIN_VALUE;
	private static int INF = Integer.MAX_VALUE;

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int T = Integer.parseInt(br.readLine());

		while (T-- != 0) {

			int n = Integer.parseInt(br.readLine());

			String[] input = br.readLine().trim().split(" ");

			int[] arr = new int[n];
			int index = 0;

			for (String ele : input)
				arr[index++] = Integer.parseInt(ele);

			int res = findSum(arr, n);

			System.out.println(res);

		}
	}
	static int findSum(int[] arr, int n) {

		int count = 0;

		for (int ele : arr) {
			if (ele == 1)
				count++;
		}

		if (count == 0 || count == 1) return 0;

		int left, right;

		for (left = 0; left < n; left++) {
			if (arr[left] == 1)
				break;
		}

		for (right = n - 1; right >= 0; right--) {
			if (arr[right] == 1)
				break;
		}

		count = 0;

		for (int i = left + 1; i < right && i < n; i++)
			if (arr[i] == 0)
				count++;

		return count;

	}
}