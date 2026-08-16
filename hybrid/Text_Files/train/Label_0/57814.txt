import java.lang.reflect.Array;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Deque;
import java.util.HashSet;
import java.util.List;
import java.util.Scanner;
import java.util.Set;

public class Main {
	static int n;
	static int count = 0;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		System.out.println("0:");
		boolean[] array = new boolean[n + 1];
		int max = 0;
		while (max < n) {
			array[max] = true;
			System.out.print(++count + ": ");
			int index = 0;
			int count = 0;
			for (int i = 0; i < max; i++) {
				if (array[i]) {
					System.out.print(i + " ");
					++count;
				}
			}
			System.out.println(max);
			
			for (int i = 0; i < max; i++) {
				if (!array[i]) {
					array[i] = true;
					index = i;
					break;
				}
			}
			for (int j = 0; j < n - 2; j++) {
				for (int i = 0; i < index; i++) {
					if (array[i]) {
						array[i] = false;
						break;
					}
				}
			}
			if (count >= max) {
				++max;
				array = new boolean[n + 1];
			}
		}
	}
}

