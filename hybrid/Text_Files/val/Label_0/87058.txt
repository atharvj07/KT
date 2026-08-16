import java.util.*;


public class Main {
    public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		//情報を読み込む
		int line = sc.nextInt();
		//配列を作る
		int data[][][] = new int[4][3][10];
		//データを読み込む
		for (int i = 0; i < line; i++) {
		    int b = sc.nextInt();
		    int f = sc.nextInt();
		    int r = sc.nextInt();
		    //部屋の人数
		    int v = sc.nextInt();
		    data[b - 1][f - 1][r -1] += v;
		}
		
		for (int i = 0; i < 4; i++) {
		    for (int t = 0; t < 3; t++) {
		        for (int j = 0; j < 10; j++) {
		            System.out.print(" " + data[i][t][j]);
		        }
		        System.out.println();
		    }
		    if (i != 3) 
		        System.out.println("####################");
		}
    }
}
