import java.util.ArrayList;
import java.util.Scanner;

public class Tester{

	public static void main(String[] args) {

		Scanner input = new Scanner(System.in);
		String str  = input.nextLine();
		String temp[] = str.split(" ");
		ArrayList<String> a = new ArrayList<String>();
		int plus = 1;
		int min = 0;
		a.add("+");
		for(int i=1;i<temp.length;i=i+2){
			String s = temp[i];
			//System.out.println(s);
			if(s.equals("-"))
				min++;
			else if(s.equals("="))
				break;
			else
				plus++;
			a.add(s);
		}
	//	System.out.println(min + " "+ plus);
		int n = Integer.parseInt(temp[temp.length-1]);
		if(n*plus - min>=n && plus - min*n<=n){
			System.out.println("Possible");
			int sign = 1;
			int sum = 0;
			if(a.size()==1){
				System.out.println(n + " = " + n);
				return;
			}
			for(int i=0;i<a.size();i++){
				//System.out.println(i);
				if(a.get(i).equals("-")){
					sign = -1;
					min--;
				}else{
					sign = 1;
					plus--;
				}
				for(int j=1;j<=n;j++){
					if(sign*j + n*plus - min>=n-sum && sign*j + plus - min*n<=n-sum)
					{
						if(i!=a.size()-1)
							System.out.print(j + " " + a.get(i+1) + " ");
						else
							System.out.print(j + " = "+ n);
						sum = sum+(j*sign);
						break;
					}
				}
			
				
			}
		}else
			System.out.println("Impossible");
		
	}

}