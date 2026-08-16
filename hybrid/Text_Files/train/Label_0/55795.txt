import java.util.Scanner;
public class Main{
	public static void main(String[] args){
		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();
		boolean[][] card = new boolean[4][13];
		for(int i = 0; i<4; i++){
			for(int j = 0; j<13 ;j++){
				card[i][j] = false;
			}
		}

		while(n-->0){
			String head = scan.next();
			int figure = 0;
			if(head.equals("S")){
				figure = 0;
			} else if(head.equals("H")){
				figure = 1;
			}else if(head.equals("C")){
				figure = 2;
			}else if(head.equals("D")){
				figure = 3;
			}
			int number = scan.nextInt();
			card[figure][number-1]=true;
		}
		for(int i = 0; i<4; i++){
			for(int j = 0; j<13; j++){
				if(card[i][j]!=true){
					if(i==0){
						System.out.println("S"+" "+(j+1));
					}else if(i==1){
						System.out.println("H"+" "+(j+1));
					}else if(i==2){
						System.out.println("C"+" "+(j+1));
					}else if(i==3){
						System.out.println("D"+" "+(j+1));
					}

				}
			}
		}
	}
}