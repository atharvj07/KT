import java.util.Scanner;

public class Main {

	public static void main(String[] args) {

		Scanner scanner = new Scanner(System.in);
		int n = scanner.nextInt();
		int[] sArray = new int[n];
		for (int i = 0; i < n; i++) {
			sArray[i] = scanner.nextInt();
		}
		int p = scanner.nextInt();
		int[] tArray = new int[p];
		int cnt = 0;
		for (int i = 0; i < p; i++) {
			tArray[i] = scanner.nextInt();
			if(binarySearch(sArray, tArray[i], 0, n-1)){
				cnt++;
			}
		}
		System.out.println(cnt);
	}
	
	public static boolean binarySearch(int[] sArray, int tElement, int start,
			int end) {

		if (tElement == sArray[(start + end) / 2]) {
			return true;
		} else if (start == end) {
			return false;
		} else {
			if (tElement < sArray[(start + end) / 2]) {
				return binarySearch(sArray, tElement, start,
						(start + end) / 2);
			} else {
				return binarySearch(sArray, tElement, (start + end) / 2+1, end);
			}
		}
	}
}