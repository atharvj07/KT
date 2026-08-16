import java.util.Scanner;

public class Main{
	static String[] button = {".,!? ", "abc", "def",
							  "ghi", "jkl", "mno",
							  "pqrs", "tuv", "wxyz"};

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int data = sc.nextInt();
		
		for(int i=0; i<data; i++){
			String str = sc.next();
			for(int j=0; j<str.length(); j++){
				int count = -1;
				int index = str.charAt(j) - '1';
				while(str.charAt(j)!='0'){
					count++;
					j++;
				}
				if(count>=0){
					System.out.print(button[index].charAt(count%button[index].length()));
				}
			}
			System.out.println();
		}
	}
}