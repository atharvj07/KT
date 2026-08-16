import java.util.Scanner;

//Surrounding Area
public class Main{

	int w, h;
	char[][] m;
	int[][] move = {{-1,0}, {0,1}, {1,0}, {0,-1}};
	boolean[][] white, black;

	void fw(int i, int j){
		if(white[i][j]||m[i][j]!='.')return;
		white[i][j] = true;
		for(int k=0;k<4;k++){
			int ni = i+move[k][0], nj = j+move[k][1];
			if(0<=ni&&ni<h&&0<=nj&&nj<w)fw(ni, nj);
		}
	}
	void fb(int i, int j){
		if(black[i][j]||m[i][j]!='.')return;
		black[i][j] = true;
		for(int k=0;k<4;k++){
			int ni = i+move[k][0], nj = j+move[k][1];
			if(0<=ni&&ni<h&&0<=nj&&nj<w)fb(ni, nj);
		}
	}

	void run(){
		Scanner sc = new Scanner(System.in);
		for(;;){
			w = sc.nextInt(); h = sc.nextInt();
			if((w|h)==0)break;
			m = new char[h][];
			for(int i=0;i<h;i++)m[i]=sc.next().toCharArray();
			white = new boolean[h][w]; black = new boolean[h][w];
			for(int i=0;i<h;i++)for(int j=0;j<w;j++){
				if(m[i][j]=='W'){
					for(int k=0;k<4;k++){
						int ni = i+move[k][0], nj = j+move[k][1];
						if(0<=ni&&ni<h&&0<=nj&&nj<w)fw(ni, nj);
					}
				}
				if(m[i][j]=='B'){
					for(int k=0;k<4;k++){
						int ni = i+move[k][0], nj = j+move[k][1];
						if(0<=ni&&ni<h&&0<=nj&&nj<w)fb(ni, nj);
					}
				}
			}
			int cw = 0, cb = 0;
			for(int i=0;i<h;i++)for(int j=0;j<w;j++){
				if(m[i][j]!='.'||white[i][j]&&black[i][j]||!white[i][j]&&!black[i][j])continue;
				if(white[i][j])cw++;
				else cb++;
			}
			System.out.println(cb+" "+cw);
		}
	}

	public static void main(String[] args) {
		new Main().run();
	}
}