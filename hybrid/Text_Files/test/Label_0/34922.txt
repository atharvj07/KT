import java.util.Scanner;

//Dividing Students
public class Main{

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		while(true){
			int n = sc.nextInt();
			if(n==0)break;
			while(n--!=0){
				int m = sc.nextInt();
				int e = sc.nextInt();
				int j = sc.nextInt();
				char a = 'C';
				if((m==100||e==100||j==100)||((m+e)/2>=90)||(m+e+j)/3>=80)a='A';
				else if((m+e+j)/3>=70||(m+e+j)/3>=50&&(m>=80||e>=80))a='B';
				System.out.println(a);
			}
		}
	}
}