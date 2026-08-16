import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[][][] ink = 
			{
				{
					{0,0,0,0,0},
					{0,0,1,0,0},
					{0,1,1,1,0},
					{0,0,1,0,0},
					{0,0,0,0,0}
				},
				{
					{0,0,0,0,0},
					{0,1,1,1,0},
					{0,1,1,1,0},
					{0,1,1,1,0},
					{0,0,0,0,0}
				},
				{
					{0,0,1,0,0},
					{0,1,1,1,0},
					{1,1,1,1,1},
					{0,1,1,1,0},
					{0,0,1,0,0}
				}
			};
		int[][] paper = new int[14][14];
		while(sc.hasNext()) {
			String s = sc.next();
			String[] sp = s.split(",");
			int x = Integer.valueOf(sp[0]);
			int y = Integer.valueOf(sp[1]);
			int size = Integer.valueOf(sp[2])-1;
			for(int i=0;i<5;i++) {
				for(int j=0;j<5;j++) {
					paper[x+i][y+j]+=ink[size][i][j];
				}
			}
		}
		int empty = 0;
		int max = 0;
		for(int i=2;i<12;i++) {
			for(int j=2;j<12;j++) {
				if (paper[i][j] == 0) {
					empty++;
				}
				max = Math.max(max,paper[i][j]);
			}
		}
		System.out.println(empty + "\n" + max);
	}

}