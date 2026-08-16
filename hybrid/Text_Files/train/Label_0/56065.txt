import java.util.*;

public class Main {
    static int[] counts = new int[100];
    static int[] minValue;
    static int min = Integer.MAX_VALUE;
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		char[] arr = sc.next().toCharArray();
		for (int i = 0; i < arr.length - 1; i++) {
		    counts[(arr[i] - '0') * 10 + (arr[i + 1] - '0')]++;
		}
		check(0, new int[9]);
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < 9; i++) {
		    sb.append(minValue[i]);
		    if (i % 3 == 2) {
		        sb.append("\n");
		    }
		}
		System.out.print(sb);
	}
	
	static void check(int idx, int[] arr) {
	    if (idx == 9) {
	        int sum = 0;
	        for (int i = 0; i < 8; i++) {
	            for (int j = i + 1; j < 9; j++) {
	                int move = Math.abs(i / 3 - j / 3) + Math.abs(i % 3 - j % 3);
	                sum += move * (counts[arr[i] * 10 + arr[j]] + counts[arr[j] * 10 + arr[i]]);
	            }
	        }
	        if (min > sum) {
	            min = sum;
	            minValue = (int[])arr.clone();
	        }
	        return;
	    }
	    for (int i = 1; i <= 9; i++) {
	        boolean flag = false;
	        for (int j = 0; j < idx; j++) {
	            if (arr[j] == i) {
	                flag = true;
	                break;
	            }
	        }
	        if (flag) {
	            continue;
	        }
	        arr[idx] = i;
	        check(idx + 1, arr);
	    }
	}
}

