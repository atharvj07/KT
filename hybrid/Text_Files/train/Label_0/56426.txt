import java.util.Scanner;
public class Main {
	

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc=new Scanner(System.in);
		int wintervacation = sc.nextInt();
		int kokugo= sc.nextInt();
		int  math= sc.nextInt();
		int  kokugoday= sc.nextInt();
		int  mathday= sc.nextInt();
		int dayk=0,daym=0,freeday=0;
		
		int k=kokugo/kokugoday;
		int kk=kokugo%kokugoday;
		if(kk>0){
			dayk=k+1;
		}else if(kk==0){
			dayk=k;
		}
		int p=math/mathday;
		int pp=math%mathday;
		if(pp>0){
			daym=p+1;
		}else if(pp==0){
			daym=p;
		}
		if(dayk<daym){
			freeday=wintervacation-daym;
		}else if(dayk>daym){
			freeday=wintervacation-dayk;
		}else if(dayk==daym){
			freeday=wintervacation-dayk;
		}
		System.out.println(freeday);
	}

}