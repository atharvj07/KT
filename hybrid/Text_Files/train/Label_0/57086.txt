import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

class Main {

	static class Comb implements Comparable<Comb> {
		private int[] array;
		private int dec; //十進数

		//コンストラクタ
		public Comb(int[] a) {
			array = new int[a.length];
			for (int i = 0; i < array.length; i++) {
				array[i] = a[i];
				dec += Math.pow(2, array[i]); //十進数にする
			}
		}

		public int[] getArray() { return array; }

		public int getDec() {
			return dec;
		}

		@Override
		public int compareTo(Comb c) { //比較の標準を作る
			return this.dec - c.getDec();
		}
	}

	public static void main(String[] args) {
		try (Scanner sc = new Scanner(System.in)) {
			//入力と配列準備
			sc.nextInt();
			int tLen = sc.nextInt();
			ArrayList<Integer> list = new ArrayList<Integer>();
			for (int i = 0; i < tLen; i++) {
				list.add(sc.nextInt());
			}
			System.out.println("0:");
			//--------------------------------------------------------
			ArrayList<Comb> arrayC = new ArrayList<Comb>();
			ArrayList<int[]> array = combination(tLen - 1);
			for (int[] arrayi : array) {
				int[] arrayNum = new int[arrayi.length];
				for (int i=0; i<arrayi.length; i++) arrayNum[i]=list.get(arrayi[i]);
				arrayC.add(new Comb(arrayNum));
			}
			Collections.sort(arrayC);
			for (Comb c : arrayC) {
				System.out.print(c.getDec() + ":");
				for (int i : c.getArray()) {
					System.out.print(" " + i);
				}
				System.out.print('\n');
			}
		}
	}

	static ArrayList<int[]> combination(int numbers) {
		ArrayList<int[]> a = new ArrayList<int[]>();
		for (int i = 1; i <= numbers + 1; i++) 	a.addAll(nCr(numbers, i));
		return a;
	}

	//組み合わせを配列に保存
		static ArrayList<int[]> nCr(int numbers, int target){  //保存用list、0～numbersから選べる、何個取る
			ArrayList<int[]> list = new ArrayList<int[]>();
			int[] keep = new int[target];
			int[] finalt = new int[target];
			for (int i=0; i<target; i++) {
				keep[i] = 0 + i;  //最初の組み合わせを作成
				finalt[i] = numbers + (i - target) + 1;  //最後の組み合わせを作成
			}
			int[] k = new int[target];
			System.arraycopy(keep,0,k,0,target);
			list.add(k);
			while (!Arrays.equals(keep, finalt)) { //最後の組み合わせではない場合
				if (keep[target-1] != numbers) {  //最後の桁がnumbersではない場合
					keep[target-1]++;
					k = new int[target];
					System.arraycopy(keep,0,k,0,target);
					list.add(k);
				} else {
					int now = target-2;
					while (now > 0) {
						if (keep[now+1] - keep[now] == 1) now--; //右の桁-1はnowの最大値
						else break;
					}
					keep[now]++;
					for (int i=now+1; i<target; i++) {
						keep[i] = keep[i-1]+1;
					}
					k = new int[target];
					System.arraycopy(keep,0,k,0,target);
					list.add(k);
				}
			}
			return list;
		}
}
