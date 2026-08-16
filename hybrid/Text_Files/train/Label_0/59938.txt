import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
	public static void main(String[] args) {
		try {
			BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

			int N = Integer.parseInt(br.readLine());
			int[] a = strToIntArray(br.readLine());
			Arrays.sort(a);
			int sum = 0;
			for (int i = 0; i < a.length; i = i + 2) {
				sum += a[i];
			}

			System.out.println(sum);
		} catch (Exception e) {
			System.err.println("Error:" + e.getMessage());
		}
	}

	// Stringで読みこんでスペースで分割されている数字を配列に入れるやつ
	// 利用法 int[] A = strTointArray(br.readLine());
	static int[] strToIntArray(String S) {
		String[] strArray = S.split(" ");
		int[] intArray = new int[strArray.length];
		for (int i = 0; i < strArray.length; i++) {
			intArray[i] = Integer.parseInt(strArray[i]);
		}
		return intArray;
	}
}
