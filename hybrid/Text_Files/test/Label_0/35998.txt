import java.util.Scanner;

public class Code560B {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		int[] board = new int[2];
		
		board[0] = scanner.nextInt();
		board[1] = scanner.nextInt();
		
		int[][] painting = new int[2][2];
		int[] area = new int[2];
		int[] min = new int[2];
		int[] max = new int[2];
		
		for(int i = 0; i < 2; i++) {
			painting[i][0] = scanner.nextInt();
			painting[i][1] = scanner.nextInt();
			
			area[i] = painting[i][0] * painting[i][1];
			min[i] = Math.min(painting[i][0], painting[i][1]);
			max[i] = Math.max(painting[i][0], painting[i][1]);
		}
		
		int boardMax = Math.max(board[0], board[1]);
		int boardMin = Math.min(board[0], board[1]);
		
		boolean isPossible = true;
		
		if(max[0] > boardMin && max[0] + min[1] > boardMax && min[0] + min[1] > boardMin)
				isPossible = false;
		else if(max[1] > boardMin && max[1] + min[0] > boardMax && min[0] + min[1] > boardMin)
			isPossible = false;
		
		if(isPossible && board[0] * board[1] >= area[0] + area[1]) {
			if(min[0] + min[1] <= boardMax && Math.max(max[0], max[1]) <= boardMax) {
				System.out.println("YES");
			} else
				System.out.println("NO");
		} else
			System.out.println("NO");
		
		scanner.close();
	}

}
