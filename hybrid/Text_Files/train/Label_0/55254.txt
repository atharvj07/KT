import java.util.Scanner;

/**
 * @author kawakami
 *
 */
class Main {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner as = new Scanner(System.in);
		
		int dice1[];
		int dice2[];
		String str = "";
		Boolean breakp = null;
		
		dice1 = new int[6];
		dice2 = new int[6];
		
		for(int i=0;i<6;i++){
			
			dice1[i] = as.nextInt();
			
		}
		
		for(int i=0;i<6;i++){
			
			dice2[i] = as.nextInt();
			
		}
		
		for(int i=0;i<3;i++){
		
			for (int j=0;j<4;j++){
				
				for(int k=0; k<j; k++){
					
					dice2 = Spin.diceSpin(dice2, "x");
					
				}
				
				breakp = Spin.Check(dice1, dice2, i);
				
				if(breakp == true){
					
					str = "Yes";
					break;
					
				}
				else{
					
					str = "No";
					
				}
				
			}
			
			if(breakp == true){
				
				break;
				
			}
		
		}
		
		System.out.println(str);

	}

}


class Spin{
	
	public static int[] diceSpin(int[] dice,String spn) {
	
		int tre = 0;	
			
		switch (spn){
		case "x":
			tre = dice[4];
			dice[4] = dice[0];
			dice[0] = dice[1];
			dice[1] = dice[5];
			dice[5] = tre;
			break;
			
		case "y":
			tre = dice[3];
			dice[3] = dice[0];
			dice[0] = dice[2];
			dice[2] = dice[5];
			dice[5] = tre;
			break;
			
		case "z":
			tre = dice[2];
			dice[2] = dice[1];
			dice[1] = dice[3];
			dice[3] = dice[4];
			dice[4] = tre;
			break;
					
		}
			
		return dice;
		
	  }
	
	public static Boolean Samecheck(int[] dice1,int[] dice2){
		
		Boolean flag = null;
		
		for(int i=0;i<6;i++){
			
			if(dice1[i] != dice2[i]){
				
				flag = false;
				break;
			}
			else{
				
				flag = true;
				
			}
			
		}
		
		return flag;
		
	}
	
	public static Boolean Check(int[] dice1,int[] dice2,int sp){
		
		Boolean flag = null;
		String spn = null;
		
		switch (sp){
		case 0:
			spn = "x";
			break;
			
		case 1:
			spn = "y";
			break;
			
		case 2:
			spn = "z";
			break;
			
		}
		
		for(int j=0;j<4;j++){		
			
			dice2 = Spin.diceSpin(dice2, spn);
			if(Spin.Samecheck(dice1, dice2)){
				
				flag = true;
				break;
			
			}
			
			flag = false;
			
		}
		
		return flag;
		
	}
	
}