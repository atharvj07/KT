import java.util.*;

public class Main {

	int[][] board;
	int d, M, N, S;
	int[][] matrix;

	void run(){
		Scanner in = new Scanner(System.in);
		for(;;){
			M = in.nextInt();
			N = in.nextInt();
			d = in.nextInt();
			if(M==0 && N==0 && d==0) return ;
			board = new int[N][M];
			for(int i=0; i<N; i++){
				for(int j=0; j<M; j++){
					board[i][j] = in.nextInt();
				}
			}
			System.out.println(solve()?1:0);
		}
	}

	void setMatrix(){
		S = M*N;
		matrix = new int[S][S+1];
		for(int i=0; i<N; i++){
			for(int j=0; j<M; j++){
				if(board[i][j] == 1){
					matrix[i*M+j][S] = 1;
				}
			}
		}

		for(int i=0; i<N; i++){
			for(int j=0; j<M; j++){
				matrix[i*M+j][i*M+j] = 1;
				for(int k=0; k<=d; k++){
					for(int l=0; l<4; l++){
						int ny = i + ((l&1)==1?k:-k),
							nx = j + (((l>>1)&1)==1?d-k:k-d);
						if(0<=ny && ny<N && 0<=nx && nx<M){
							matrix[ny*M+nx][i*M+j] = 1;
						}
					}
				}
			}
		}

	}

	boolean solve(){
		setMatrix();
		for(int i=0; i<S; i++){
			boolean found = false;
			int key = -1;
			for(int k=i; k<S; k++){
				if(matrix[k][i] == 1){
					found = true;
					key = k;
					break;
				}
			}
			if(found){
				int[] tmp = matrix[i].clone();
				matrix[i] = matrix[key].clone();
				matrix[key] = tmp;
				for(int k=i+1; k<S; k++)if(matrix[k][i] == 1){
					for(int j=i; j<=S; j++){
						matrix[k][j] ^= matrix[i][j];
					}
				}
			}
		}
		
		for(int i=S-1; i>=0; i--){
			if(matrix[i][i] == 1){
				for(int k=i-1; k>=0; k--)if(matrix[k][i] == 1){
					for(int j=S; j>=i; j--){
						matrix[k][j] ^= matrix[i][j];
					}
				}
			}
		}
		
		for(int i=0; i<S; i++){
			if(matrix[i][i] == 0 && matrix[i][S] == 1){
				return false;
			}
		}
		return true;
	}

	public static void main(String args[]){
		new Main().run();
	}
}