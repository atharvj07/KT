import java.util.Scanner;


public class Restoringpassword {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner input = new Scanner(System.in);
		String z = input.next();
		String[] s = new String[10];
		String p = "";
		for(int i=0; i<10;i++)s[i] = input.next();
		int j=0;
		while(j+10<=80){
		for(int i=0; i<10;i++){
			if(z.substring(j,j+10).equals(s[i]))p+=Integer.toString(i);
		}
		j+=10;
	}
		System.out.println(p);
	}
	

}
