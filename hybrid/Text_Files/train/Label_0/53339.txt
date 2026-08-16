import java.util.*;
public class Problem7a{
	
	public static int countCols(char[][] sq){
		int cols = 0;
		for(int c = 0; c < sq[0].length; c++){
			if(sq[0][c] == 'B'){
				for(int r = 1; r < sq.length; r++){
					if((r == sq.length - 1) && (sq[r][c] == 'B')){
						cols++;
					}
					else if(sq[r][c] != 'B'){
						break;
					}
				}
			}
		}

		return cols;
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int count = 0;
		char[][] sq = new char[8][8];
		int r = 0;
		boolean all = true;
		while(sc.hasNextLine()){
			String line = sc.nextLine();
			if(line.indexOf('W') != -1){
				all = false;
			}
			char[] row = line.toCharArray();
			sq[r] = row;
			r++;
			
		}
		if(all){
			System.out.println(8);
		}
		else{
			int cols = countCols(sq);
			count += cols;
			for(int i = 0; i < sq.length; i++){
				int countr = 0;
				char[] row = sq[i];
				for(char p : row){
					if(p == 'B'){
						countr++;
					}
				}
				countr -= cols;
				if(countr == (8 - cols)){
					countr = 1;
				}
				count += countr;
			}

				System.out.println(count);

		}
		
		
	}
}