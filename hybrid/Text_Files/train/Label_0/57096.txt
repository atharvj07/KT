import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws FileNotFoundException {

		Scanner scan = new Scanner(System.in);
		// Scanner scan = new Scanner(new
		// File("D:\\UserArea\\J0124567\\Downloads\\0534-input.txt"));

		while (scan.hasNext()) {

			int n = scan.nextInt();
			if (n == 0)
				break;
			Chs chs = new Chs(n);
			for (int i = 0; i < n; i++)
				chs.add(scan.nextInt());
			System.out.println(chs.rem());
		}

		scan.close();
		System.exit(0);

	}
}

class Chs {
	public Chs(int n) {
		col = new int[n + 1];
		rep = new int[n + 1];
		N = n;
	}

	public int rem() {
		// this.print();

		int max = 0;
		for (int i = 1; i <= last; i++) {
			int x = this.erase(i);
			if (x > max)
				max = x;
		}
		return N - max;
	}

	private void print() {
		for (int i = 1; col[i] > 0; i++)
			System.out.println(i + ": Col " + col[i] + " Rep " + rep[i]);
	}

	private int erase(int i) {
		int max = 0;
		if (rep[i] == 1) {
			if (col[i - 1] == col[i + 1] && rep[i - 1] + rep[i + 1] >= 3) {
				int x = rep[i - 1] + rep[i + 1] + 1 + this.next(i - 2, i + 2);
				if (x > max)
					max = x;
			} else {
				if (rep[i - 1] >= 3) {
					int x = rep[i - 1] + 1 + this.next(i - 2, i + 1);
					if (x > max)
						max = x;
				}
				if (rep[i + 1] >= 3) {
					int x = rep[i + 1] + 1 + this.next(i - 1, i + 2);
					if (x > max)
						max = x;
				}
			}
		} else {
			if (rep[i - 1] >= 3) {
				int x = rep[i - 1] + 1;
				rep[i]--;
				x += this.next(i - 2, i);
				rep[i]++;
				if (x > max)
					max = x;
			}
			if (rep[i + 1] >= 3) {
				// System.out.print(i+" ");
				int x = rep[i + 1] + 1;
				rep[i]--;
				x += this.next(i, i + 2);
				rep[i]++;
				if (x > max)
					max = x;
			}
		}
		return max;
	}

	private int next(int low, int hi) {
		int x = 0;
		for (int i = 0; col[low - i] == col[hi + i] && col[low - i] > 0; i++)
			if (rep[low - i] + rep[hi + i] >= 4)
				x += rep[low - i] + rep[hi + i];
		return x;
	}

	public void add(int c) {
		if (col[last] == 0 || col[last] == c) {
			col[last] = c;
			rep[last]++;
		} else {
			col[++last] = c;
			rep[last]++;
		}
	}

	int last = 1;
	int[] col;
	int[] rep;
	int N;
}