
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;

public class Main {

	public static class Query{
		private int left;
		private int right;
		private int ans;

		public Query(int left, int right) {
			this.left = left;
			this.right = right;
			this.ans = 0;
		}

		public void execute(int num) {
			if(left <= num && right >= num) {
				ans++;
			}
		}

		public int getLeft() {
			return this.left;
		}

		public int getRight() {
			return this.right;
		}

		public int getAns() {
			return this.ans;
		}
	}


	public static void main(String[] args) throws IOException {
		// TODO 自動生成されたメソッド・スタブ
		Scanner in = new Scanner(System.in);

		int Q = in.nextInt();
		int min = 100000;
		int max = 0;

		ArrayList<Query> array = new ArrayList<Query>(Q);

		for(int i=0; i<Q; ++i) {
			int left = in.nextInt();
			int right = in.nextInt();
			array.add(new Query(left, right));
			if(min > left) {
				min = left;
			}
			if(max < right) {
				max = right;
			}
		}

		for(int i=min; i <= max; ++i) {
			if(checkLike2017(i)) {
				// System.out.println("numA: " + i + " numB: " + (i + 1) / 2);
				for(Query q : array) {
					q.execute(i);
				}
			}
		}


		for(Query q : array) {
			System.out.println(q.getAns());
		}
	}

	public static boolean checkLike2017(int numA) {
		if(numA < 3) {
			return false;
		}

		int numB = (numA + 1) / 2;
		if(checkPrimeNum(numB)) {
			return checkPrimeNum(numA);
		}else {
			return false;
		}
	}

	public static boolean checkPrimeNum(int num) {
		if(num == 2 || num == 3) {
			return true;
		}else if(num % 2 == 0 || num % 3 == 0) {
			return false;
		}

		int root = (int) Math.sqrt(num);
		for(int i=4; i<= root; ++i) {
			if(num % i == 0) {
				return false;
			}
		}

		return true;
	}

}
