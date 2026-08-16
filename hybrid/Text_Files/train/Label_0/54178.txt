import java.util.Scanner;

public class Main{
	public static void main(String[] args){
		Scanner scan = new Scanner(System.in);
		while(scan.hasNext()){
			int n = scan.nextInt();
			if(n == -1){
				break;
			}
			String str = "0000000";
			String tStr = "";
			for(int i = 0;i < n;i++){
				int t = scan.nextInt();
				switch(t){
				case 0:
					tStr = "0111111";
					break;
				case 1:
					tStr = "0000110";
					break;
				case 2:
					tStr = "1011011";
					break;
				case 3:
					tStr = "1001111";
					break;
				case 4:
					tStr = "1100110";
					break;
				case 5:
					tStr = "1101101";
					break;
				case 6:
					tStr = "1111101";
					break;
				case 7:
					tStr = "0100111";
					break;
				case 8:
					tStr = "1111111";
					break;
				case 9:
					tStr = "1101111";
					break;
				}
				for(int j = 0;j < 7;j++){
					System.out.print(Integer.parseInt(str.charAt(j)+"")^Integer.parseInt(tStr.charAt(j)+""));
				}
				System.out.println();
				str = tStr;
			}
		}
	}
}