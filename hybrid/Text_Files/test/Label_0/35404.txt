import java.util.ArrayList;
import java.util.Scanner;

public class Dvugramma {

	public class PairClass{
		String val;
		int count;
	};
	
	public static int[] getArray(int size) {
		int[] array = new int[size];
		for (int i = 0; i < size; i++) {
			array[i] = sr.nextInt();
		}
		return array;
	}

	public static int[][] getMatrix(int sizeI, int sizeJ) {
		int[][] array = new int[sizeI][sizeJ];
		for (int i = 0; i < sizeI; i++) {
			for (int j = 0; j < sizeJ; j++) {
				array[i][j] = sr.nextInt();
			}
		}
		return array;
	}

	static Scanner sr = new Scanner(System.in);

	public static void main(String[] args) {

		Dvugramma pr  = new Dvugramma();
		int len = sr.nextInt();
		sr.nextLine();
		String str = sr.nextLine();
		ArrayList<PairClass> a = new ArrayList<>();
		for (int i = 0; i < len-1; i++) {
			char[] b = { str.charAt(i), str.charAt(i+1)};
			String val = String.valueOf(b);
			PairClass p = pr.new PairClass();
			p.val = val;
			int count = 0;
			boolean isExist = false;
			for (int j = 0; j < a.size(); j++) {
				if(p.val.equals(a.get(j).val))
				{
					count = a.get(j).count + 1;
					p.count = count;
					a.set(j, p);
					isExist = true;
					break;
				}
			}
			if(!isExist){
				p.count = 1;
				a.add(p);
			}
		}
		int max = Integer.MIN_VALUE;
		int maxIndex = 0;
		for (int i = 0; i < a.size(); i++) {
			if(a.get(i).count > max){
				max = a.get(i).count;
				maxIndex = i;
			}
		}
		System.out.println(a.get(maxIndex).val);
	}
}