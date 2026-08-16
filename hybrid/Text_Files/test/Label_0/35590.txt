import java.util.Scanner;

public class Main {
	static Scanner sc = new Scanner(System.in);

	//0141
	static class SpiralPattern {
		//左から順に上移動(0)、右移動(1)、下移動(2)、左移動(3)
		// ()内の数字はsetDirectionNum
		int[][] xy_dir = {{0, -1}, {1, 0}, {0, 1}, {-1, 0}};
		int y, x; //現在位置を記録する

		void print_a_spiral() {
			int inputNum = sc.nextInt();
			int[] spiralLen = new int[inputNum];
			for(int i=0; i<inputNum; i++) {
				spiralLen[i] = sc.nextInt();
			}
			for(int i=0; i<inputNum; i++) {
				char[][] field = new char[spiralLen[i]][spiralLen[i]];
				for(int j=0; j<spiralLen[i]; j++) {		// 拡張for文だと半角スペースが無視される？
					for(int k=0; k<spiralLen[i]; k++) {
						field[j][k] = ' ';
					}
				}

				y = spiralLen[i]-1;
				x = 0;
				field[y][x] = '#';
				int setNum_dir = 0; //初期値は上移動
				int dirChangeNum = 0; // 方向転換した回数
				for(;;) {
					if(dirChangeNum >= spiralLen[i] || spiralLen[i] == 1){
						break;
					}else if(y + xy_dir[setNum_dir][1]*2 < 0 || y + xy_dir[setNum_dir][1]*2 > spiralLen[i]-1 ||
							 x + xy_dir[setNum_dir][0]*2 < 0 || x + xy_dir[setNum_dir][0]*2 > spiralLen[i]-1) {
						y += xy_dir[setNum_dir][1];
						x += xy_dir[setNum_dir][0];
						field[y][x] = '#';
						dirChangeNum++;
						setNum_dir = dirChangeNum % 4;
					}else if(field[y + xy_dir[setNum_dir][1] * 2]
								  [x + xy_dir[setNum_dir][0] * 2] == '#') {
						dirChangeNum++;
						setNum_dir = dirChangeNum % 4;
					}else {
						y += xy_dir[setNum_dir][1];
						x += xy_dir[setNum_dir][0];
						field[y][x] = '#';
					}
				}

				for(int j=0; j<spiralLen[i]; j++) {
					for(int k=0; k<spiralLen[i]; k++) {
						System.out.print(field[j][k]);
					}
					System.out.println("");
				}
				if(i != inputNum-1) System.out.println("");
			}
		}
	}

	public static void main(String[] args) {
		SpiralPattern sp = new SpiralPattern();
		sp.print_a_spiral();
	}
}