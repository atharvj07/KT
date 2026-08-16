import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Main m = new Main();
		m.run();
	}

	Scanner sc = new Scanner(System.in);

	void run() {
		for(;;){
			int n = sc.nextInt();
			int m = sc.nextInt();
			
			if(n ==0  && m == 0){
				break;
			}
			int map[][] = new int[n+2][m+2];
			
			for(int i = 0 ; i< n ;i++){
				char[] chs = sc.next().toCharArray();
				for(int j = 0;j < m;j++){
					map[i+1][j+1] = chs[j];
				}
			}
			
			int dx[] = {1,0,-1,0};
			int dy[] = {0,1,0,-1};
			int d = 0;
			int i = 1;
			int j = 1;
			int count = 100;
			for(int c = 0;c < n*m*4*2; c++){
				if(i==1&&j==1 && d!= 0){
					break;
				}
//				System.out.println(i+" "+j+" "+ map[i][j] +" -> "+(i+dx[d])+" " +(j+dy[d])+" "+map[i+dx[d]][j+dy[d]]);
				if(map[i + dx[d]][j + dy[d]] == '.'){
					i = i + dx[d];
					j = j + dy[d];
					d = (d+3)%4;
					count++;
					map[i][j] = count;
				}else if(map[i + dx[d]][j + dy[d]] == count-1){
					map[i][j] = '#';
					i = i + dx[d];
					j = j + dy[d];
					d = (d+3)%4;
					d %= 4;
					count--;
				}else{
					d++;
					d %= 4;
				}
			}
			
			boolean ans = true;
			ans &= map[1][1] != '.';
			ans &= map[1][m] != '.';
			ans &= map[n][1] != '.';
			ans &= map[n][m] != '.';
			ans &= map[1][1] != '#';
			ans &= map[1][m] != '#';
			ans &= map[n][1] != '#';
			ans &= map[n][m] != '#';
			
			for(int ii =0; ii<n;ii++ ){
				for(int jj = 0; jj<m;jj++ ){
//					System.out.printf("%4d", map[ii+1][jj+1]);
				}
//				System.out.println();
			}
			System.out.println(ans?"YES":"NO");
		}
		
	}
}

