import java.util.*;
public class Solution{
	public static void main(String[] args){
		Scanner scan = new Scanner(System.in);
		String ans = "No";
		int equal = 0;
		String login = scan.nextLine().toLowerCase().trim();
		int num = scan.nextInt();
		scan.nextLine();
		for(int i = 0; i <  num; i++){
			String curr = scan.nextLine().toLowerCase().trim();
			boolean diff = false;
			if(login.length() == curr.length()){
				for (int j = 0; j < curr.length(); j++){
					if (curr.charAt(j) != login.charAt(j)){
						if (curr.charAt(j) != '0' && curr.charAt(j) != 'o' && curr.charAt(j) != '1' && curr.charAt(j) != 'i' && curr.charAt(j) != 'l'){
							diff = true;
						}else if ((curr.charAt(j) == '0' || curr.charAt(j) == 'o') && (login.charAt(j) != '0' && login.charAt(j) != 'o')){
							diff = true;
						}else if ((curr.charAt(j) == '1' || curr.charAt(j) == 'i' || curr.charAt(j) == 'l') && (login.charAt(j) != 'i' && login.charAt(j) != '1' && login.charAt(j) != 'l')){
							diff = true;
						}
					}
				}
			}else{
				diff = true;
			}
			if (diff){
				equal ++;
			}
		}
		if (equal == num){
			System.out.println("Yes");
		}else{
			System.out.println("No");
		}
	}
}