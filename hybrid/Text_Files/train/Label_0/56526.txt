import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO 自動生成されたメソッド・スタブ
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int array[] = new int[n];

		for(int i = 0; i < n; i++) {
			array[i] = sc.nextInt();
		}

		int q = sc.nextInt();

		for(int i = 0; i < q; i++) {
			int key = sc.nextInt();

			BinarySearch bi = new BinarySearch();
			System.out.println(bi.binarySearch(array, key));
		}
	}
}

class BinarySearch {
	public int binarySearch(int[] array, int key) {
		int pLeft = 0;
		int pRight = array.length - 1;

		do {
			int center = (pLeft + pRight) / 2;

			if (array[center] == key) {
				return 1;
			} else if (array[center] < key){
				pLeft = center + 1; //真ん中の一つ右側を左端とする
			} else {
				pRight = center - 1;
			}
		} while (pLeft <= pRight);

		return 0;
	}
}
