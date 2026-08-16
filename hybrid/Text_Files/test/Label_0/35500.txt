import java.util.Scanner;

//Puzzle
public class Main{

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		boolean f = true;
		while(t--!=0){
			if(!f)System.out.println();
			f = false;
			int[][] a = new int[9][9];
			for(int i=0;i<9;i++)for(int j=0;j<9;j++)a[i][j]=sc.nextInt();
			boolean[][] b = new boolean[9][9];
			for(int i=0;i<9;i++){
				int[] c = new int[10];
				for(int j=0;j<9;j++)c[a[i][j]]++;
				for(int j=0;j<9;j++)if(c[a[i][j]]>=2)b[i][j]=true;
			}
			for(int j=0;j<9;j++){
				int[] c = new int[10];
				for(int i=0;i<9;i++)c[a[i][j]]++;
				for(int i=0;i<9;i++)if(c[a[i][j]]>=2)b[i][j]=true;
			}
			for(int si=0;si<9;si+=3){
				for(int sj=0;sj<9;sj+=3){
					int[] c = new int[10];
					for(int i=0;i<3;i++){
						for(int j=0;j<3;j++){
							c[a[si+i][sj+j]]++;
						}
					}
					for(int i=0;i<3;i++){
						for(int j=0;j<3;j++){
							if(c[a[si+i][sj+j]]>=2)b[si+i][sj+j]=true;
						}
					}
				}
			}
			for(int i=0;i<9;i++){
				for(int j=0;j<9;j++){
					System.out.print((b[i][j]?"*":" ")+a[i][j]);
				}
				System.out.println();
			}
		}
	}
}